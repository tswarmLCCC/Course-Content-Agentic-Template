"""
COSC 2060 — Unit 7 Lab: Orchestration, DAGs, & Dead-Letter Queues
"""

import time
from typing import Dict, List, Any, Callable

class PipelineNode:
    def __init__(self, name: str, func: Callable, dependencies: List[str] = None, max_retries: int = 2):
        self.name = name
        self.func = func
        self.dependencies = dependencies or []
        self.max_retries = max_retries
        self.status = "PENDING"
        self.result = None
        self.error = None

class DAGOrchestrator:
    def __init__(self):
        self.nodes: Dict[str, PipelineNode] = {}
        self.context: Dict[str, Any] = {}
        self.dlq: List[Dict[str, Any]] = []

    def add_node(self, node: PipelineNode):
        self.nodes[node.name] = node

    def get_execution_order(self) -> List[str]:
        in_degree = {name: 0 for name in self.nodes}
        adj = {name: [] for name in self.nodes}
        
        for name, node in self.nodes.items():
            for dep in node.dependencies:
                if dep not in self.nodes:
                    raise ValueError(f"Dependency '{dep}' does not exist in DAG.")
                adj[dep].append(name)
                in_degree[name] += 1
                
        queue = [name for name, deg in in_degree.items() if deg == 0]
        order = []
        
        while queue:
            curr = queue.pop(0)
            order.append(curr)
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(order) != len(self.nodes):
            raise ValueError("Cycle detected in DAG! Pipeline execution blocked.")
            
        return order

    def execute_node_with_retry(self, node: PipelineNode, base_delay: float = 0.05) -> bool:
        for attempt in range(1, node.max_retries + 2):
            try:
                node.status = "RUNNING"
                node.result = node.func(self.context)
                node.status = "SUCCESS"
                self.context[node.name] = node.result
                return True
            except Exception as e:
                node.error = str(e)
                if attempt <= node.max_retries:
                    delay = base_delay * (2 ** (attempt - 1))
                    time.sleep(delay)
                else:
                    node.status = "FAILED"
                    return False

    def run_pipeline(self):
        order = self.get_execution_order()
        for name in order:
            node = self.nodes[name]
            
            deps_ok = True
            for dep in node.dependencies:
                if self.nodes[dep].status != "SUCCESS":
                    deps_ok = False
                    break
                    
            if not deps_ok:
                node.status = "SKIPPED"
                print(f"Skipping node '{name}' because upstream dependencies were not successful.")
                continue
                
            self.execute_node_with_retry(node)

FINAL_FEATURE_STORE = {}

_transient_attempts = 0
def task_ingest_fuel(ctx):
    global _transient_attempts
    _transient_attempts += 1
    if _transient_attempts < 2:
        raise ConnectionError("Transient network timeout connecting to fuel gateway.")
    return [
        {"tx_id": "TX-01", "truck_id": "TRUCK-101", "gallons": 120.0, "status": "VALID"},
        {"tx_id": "TX-02", "truck_id": "TRUCK-219", "gallons": 240.0, "status": "VALID"},
        {"tx_id": "TX-03", "truck_id": "TRUCK-304", "gallons": -50.0, "status": "POISON_PILL"},
        {"tx_id": "TX-04", "truck_id": "TRUCK-219", "gallons": 180.0, "status": "VALID"}
    ]

def task_clean_and_dlq(ctx):
    raw_data = ctx["ingest_fuel"]
    clean_batch = []
    for row in raw_data:
        if row["gallons"] <= 0.0 or row["status"] == "POISON_PILL":
            orchestrator.dlq.append({
                "record": row,
                "reason": "Invalid gallon measurement: negative or zero quantity.",
                "quarantined_at": time.time()
            })
        else:
            clean_batch.append(row)
    return clean_batch

def task_write_features(ctx):
    clean_data = ctx["clean_fuel"]
    date_partition = "2024-10-24"
    
    FINAL_FEATURE_STORE[date_partition] = {}
    for row in clean_data:
        tid = row["truck_id"]
        if tid not in FINAL_FEATURE_STORE[date_partition]:
            FINAL_FEATURE_STORE[date_partition][tid] = 0.0
        FINAL_FEATURE_STORE[date_partition][tid] += row["gallons"]
    return FINAL_FEATURE_STORE[date_partition]

if __name__ == "__main__":
    print("=== Step 1: Building DAG & Checking Topological Order ===")
    orchestrator = DAGOrchestrator()
    orchestrator.add_node(PipelineNode("ingest_fuel", task_ingest_fuel, dependencies=[], max_retries=2))
    orchestrator.add_node(PipelineNode("clean_fuel", task_clean_and_dlq, dependencies=["ingest_fuel"]))
    orchestrator.add_node(PipelineNode("write_features", task_write_features, dependencies=["clean_fuel"]))

    order = orchestrator.get_execution_order()
    print(f"Topological Execution Order: {order}")
    assert order == ["ingest_fuel", "clean_fuel", "write_features"]

    print("\n=== Step 2: Testing Cycle Detection ===")
    cycle_dag = DAGOrchestrator()
    cycle_dag.add_node(PipelineNode("A", lambda ctx: None, dependencies=["B"]))
    cycle_dag.add_node(PipelineNode("B", lambda ctx: None, dependencies=["A"]))
    try:
        cycle_dag.get_execution_order()
        assert False, "Failed to detect circular dependency!"
    except ValueError as e:
        print(f"[PASS] Cycle detected successfully: {e}")

    print("\n=== Step 3: Executing Resilient Pipeline (With Retries & DLQ) ===")
    orchestrator.run_pipeline()

    assert orchestrator.nodes["ingest_fuel"].status == "SUCCESS"
    assert orchestrator.nodes["clean_fuel"].status == "SUCCESS"
    assert orchestrator.nodes["write_features"].status == "SUCCESS"
    print("[PASS] All pipeline nodes completed with SUCCESS.")

    print("\n=== Step 4: Verifying Dead-Letter Queue (DLQ) Quarantine ===")
    print(f"DLQ contains {len(orchestrator.dlq)} quarantined records.")
    assert len(orchestrator.dlq) == 1
    assert orchestrator.dlq[0]["record"]["tx_id"] == "TX-03"
    print(f"[PASS] Poison pill TX-03 correctly isolated in DLQ.")

    print("\n=== Step 5: Verifying Idempotent Execution ===")
    orchestrator.run_pipeline()
    partition = FINAL_FEATURE_STORE["2024-10-24"]
    print(f"Aggregated Totals: {partition}")
    assert partition["TRUCK-219"] == 420.0
    assert partition["TRUCK-101"] == 120.0
    print("[PASS] Idempotency confirmed: Re-run produced zero duplicate gallons.")

    print("\n[SUCCESS] All Unit 7 Lab challenges verified successfully!")
