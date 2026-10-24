"""
COSC 2060 — Unit 8 Lab: Capstone Defense & Blind Batch Verification
"""

import json
import time
from typing import Dict, List, Any

BLIND_TEST_BATCH = {
    "fuel_transactions": [
        {"tx_id": "TX-901", "truck_id": "TRUCK-101", "gallons": 140.0, "state": "OH"},
        {"tx_id": "TX-902", "truck_id": "TRUCK-219", "gallons": 340.0, "state": "IN"},
        {"tx_id": "TX-903", "truck_id": "TRUCK-304", "gallons": -12.5, "state": "IL"},
        {"tx_id": "TX-904", "truck_id": "TRUCK-405", "gallons": 95.0,  "state": "OH"}
    ],
    "vision_inspections": [
        {"truck_id": "TRUCK-219", "image": "img_blind_01.jpg", "defect": "sidewall_crack", "confidence": 0.94},
        {"truck_id": "TRUCK-101", "image": "img_blind_02.jpg", "defect": "none", "confidence": 0.99}
    ],
    "maintenance_logs": [
        {"truck_id": "TRUCK-219", "wo": "WO-9901", "notes": "Engine whistling noise under high acceleration. Recall notice Part #TC-884."},
        {"truck_id": "TRUCK-101", "wo": "WO-9902", "notes": "Wiper blade replacement completed."}
    ]
}

class CapstoneDefenseSystem:
    def __init__(self, system_name: str = "Midwest-Logistics-Autonomous-Core"):
        self.system_name = system_name
        self.feature_store = {}
        self.dlq = []
        self.active_alerts = []
        self.grounded_fleet = set()
        print(f"[{self.system_name}] Initializing Capstone Defense Ecosystem...")

    def ingest_blind_fuel_transactions(self, transactions: List[Dict[str, Any]]):
        for tx in transactions:
            if tx["gallons"] <= 0.0:
                self.dlq.append({
                    "record": tx,
                    "reason": "Corrupted numeric measurement (gallons <= 0)",
                    "timestamp": time.time()
                })
                continue
                
            if tx["gallons"] > 300.0:
                self.active_alerts.append({
                    "alert_type": "FUEL_FRAUD",
                    "truck_id": tx["truck_id"],
                    "detail": f"Transaction {tx['tx_id']}: {tx['gallons']} gallons exceeds tank capacity."
                })
                
            tid = tx["truck_id"]
            if tid not in self.feature_store:
                self.feature_store[tid] = {"total_gallons": 0.0, "transaction_count": 0}
            self.feature_store[tid]["total_gallons"] += tx["gallons"]
            self.feature_store[tid]["transaction_count"] += 1

    def evaluate_operational_clearance(self, truck_id: str, vision_data: List[Dict], rag_data: List[Dict]) -> Dict[str, Any]:
        findings = []
        is_grounded = False
        
        truck_vision = [v for v in vision_data if v["truck_id"] == truck_id]
        for v in truck_vision:
            if v["defect"] == "sidewall_crack" and v["confidence"] >= 0.80:
                findings.append(f"Vision Alert: Tire sidewall crack detected ({v['confidence']*100:.1f}% confidence).")
                is_grounded = True
                
        truck_rag = [r for r in rag_data if r["truck_id"] == truck_id]
        for r in truck_rag:
            if "recall" in r["notes"].lower() or "whistling" in r["notes"].lower():
                findings.append(f"RAG Alert: Unresolved safety bulletin in work order {r['wo']}.")
                is_grounded = True
                
        if is_grounded:
            self.grounded_fleet.add(truck_id)
            return {
                "truck_id": truck_id,
                "status": "GROUNDED",
                "risk_tier": "CRITICAL",
                "findings": findings
            }
        else:
            return {
                "truck_id": truck_id,
                "status": "CLEARED",
                "risk_tier": "NORMAL",
                "findings": ["All automated safety checks passed."]
            }

if __name__ == "__main__":
    print("================================================================================")
    print("COSC 2060 CAPSTONE TECHNICAL DEFENSE: LIVE SIMULATION")
    print("================================================================================")
    
    defense = CapstoneDefenseSystem()

    print("\n--- Phase 1: Ingesting Blind Fuel Transactions ---")
    defense.ingest_blind_fuel_transactions(BLIND_TEST_BATCH["fuel_transactions"])
    
    print(f"Clean records processed for trucks: {list(defense.feature_store.keys())}")
    print(f"Quarantined DLQ count: {len(defense.dlq)}")
    print(f"Active fraud alerts: {len(defense.active_alerts)}")

    assert len(defense.dlq) == 1, f"Expected 1 DLQ record, got {len(defense.dlq)}"
    assert defense.dlq[0]["record"]["tx_id"] == "TX-903"
    print("[PASS] Poison pill TX-903 successfully routed to DLQ without crashing pipeline.")

    assert len(defense.active_alerts) == 1
    assert defense.active_alerts[0]["truck_id"] == "TRUCK-219"
    print("[PASS] Fuel tank anomaly detected on TRUCK-219.")

    print("\n--- Phase 2: Multimodal Cross-Engine Diagnostics ---")
    
    res_101 = defense.evaluate_operational_clearance(
        "TRUCK-101", BLIND_TEST_BATCH["vision_inspections"], BLIND_TEST_BATCH["maintenance_logs"]
    )
    print(f"TRUCK-101 Status: {res_101['status']}")
    assert res_101["status"] == "CLEARED"
    assert res_101["risk_tier"] == "NORMAL"
    print("[PASS] TRUCK-101 cleared for highway operation.")

    res_219 = defense.evaluate_operational_clearance(
        "TRUCK-219", BLIND_TEST_BATCH["vision_inspections"], BLIND_TEST_BATCH["maintenance_logs"]
    )
    print(f"TRUCK-219 Status: {res_219['status']}")
    print(f"TRUCK-219 Findings: {res_219['findings']}")
    assert res_219["status"] == "GROUNDED"
    assert res_219["risk_tier"] == "CRITICAL"
    assert len(res_219["findings"]) == 2
    assert "TRUCK-219" in defense.grounded_fleet
    print("[PASS] TRUCK-219 correctly grounded with 2 independent safety violations.")

    print("\n================================================================================")
    print("CAPSTONE AUDIT VERDICT: 100% PASS - READY FOR ENTERPRISE DEPLOYMENT")
    print("================================================================================")
