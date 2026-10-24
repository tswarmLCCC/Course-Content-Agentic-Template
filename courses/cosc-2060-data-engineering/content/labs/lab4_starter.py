"""
COSC 2060 — Unit 4 Lab: Unstructured Text & RAG Ingestion Pipeline
"""

import re
import numpy as np
from sentence_transformers import SentenceTransformer

RAW_MAINTENANCE_DUMP = """
--- LOG_START ---
WORK_ORDER: WO-10023
TRUCK_ID: TRUCK-104
DATE: 2024-08-14
MILEAGE: 142050
CATEGORY: BRAKES
NOTES: Driver complained of soft brake pedal when descending steep grades. Replaced front steer axle brake pads and bled air from hydraulic lines. System pressurized to spec. Test drive completed with normal stopping distance.
--- LOG_END ---
--- LOG_START ---
WORK_ORDER: WO-10045
TRUCK_ID: TRUCK-219
DATE: 2024-09-28
MILEAGE: 184200
CATEGORY: ENGINE
NOTES: Driver reported loud whistling sound when revving up to 1800 rpm on mountain pass. Drained engine oil and inspected bottom pan, noticed fine brass glitter in sediment. Inspected trbo oil line, factory clamp appears intact. Topped off 15W-40 oil. Advised driver to report if whistling worsens.
--- LOG_END ---
--- LOG_START ---
WORK_ORDER: WO-10088
TRUCK_ID: TRUCK-302
DATE: 2024-10-02
MILEAGE: 215300
CATEGORY: ELECTRICAL
NOTES: Alternator output dropping below 12.8 volts under heavy AC load. Replaced internal voltage regulator and tightened serpentine belt tensioner. Battery bank tested at 98% health.
--- LOG_END ---
--- LOG_START ---
WORK_ORDER: WO-10112
TRUCK_ID: TRUCK-219
DATE: 2024-10-10
MILEAGE: 186500
CATEGORY: TIRES
NOTES: Routine pre-trip tire tread depth measurement. Steer tires at 8/32nds, drive tires at 6/32nds. Adjusted inflation to 105 PSI cold.
--- LOG_END ---
"""

def parse_maintenance_logs(raw_text: str) -> list[dict]:
    records = []
    blocks = re.findall(r"--- LOG_START ---(.*?)--- LOG_END ---", raw_text, re.DOTALL)
    for block in blocks:
        wo_match = re.search(r"WORK_ORDER:\s*(\S+)", block)
        truck_match = re.search(r"TRUCK_ID:\s*(\S+)", block)
        date_match = re.search(r"DATE:\s*(\S+)", block)
        mileage_match = re.search(r"MILEAGE:\s*(\d+)", block)
        cat_match = re.search(r"CATEGORY:\s*(\S+)", block)
        notes_match = re.search(r"NOTES:\s*(.*)", block, re.DOTALL)
        
        if wo_match and truck_match and notes_match:
            records.append({
                "work_order": wo_match.group(1).strip(),
                "truck_id": truck_match.group(1).strip(),
                "date": date_match.group(1).strip() if date_match else "UNKNOWN",
                "mileage": int(mileage_match.group(1).strip()) if mileage_match else 0,
                "category": cat_match.group(1).strip() if cat_match else "GENERAL",
                "notes": notes_match.group(1).strip()
            })
    return records

def create_overlapping_chunks(records: list[dict], chunk_words: int = 25, overlap_words: int = 8) -> list[dict]:
    chunks = []
    for rec in records:
        words = rec["notes"].split()
        if not words:
            continue
            
        start = 0
        idx = 0
        while start < len(words):
            end = min(start + chunk_words, len(words))
            chunk_str = " ".join(words[start:end])
            chunks.append({
                "chunk_id": f"{rec['work_order']}_chk_{idx}",
                "truck_id": rec["truck_id"],
                "work_order": rec["work_order"],
                "date": rec["date"],
                "text": chunk_str
            })
            idx += 1
            if end == len(words):
                break
            start += (chunk_words - overlap_words)
            
    return chunks

class LocalVectorIndex:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        print(f"Loading local embedding model: {model_name}...")
        self.model = SentenceTransformer(model_name)
        self.chunks = []
        self.embeddings = None

    def index_chunks(self, chunks: list[dict]):
        self.chunks = chunks
        texts = [c["text"] for c in chunks]
        raw_vecs = self.model.encode(texts, convert_to_numpy=True)
        norms = np.linalg.norm(raw_vecs, axis=1, keepdims=True)
        norms[norms == 0] = 1e-12
        self.embeddings = raw_vecs / norms
        print(f"Indexed {len(chunks)} chunks into vector space shape: {self.embeddings.shape}")

    def search(self, query: str, truck_filter: str = None, top_k: int = 3) -> list[dict]:
        query_vec = self.model.encode([query], convert_to_numpy=True)
        q_norm = np.linalg.norm(query_vec)
        if q_norm > 0:
            query_vec = query_vec / q_norm
            
        similarities = np.dot(self.embeddings, query_vec.T).squeeze()
        
        candidates = []
        for idx, score in enumerate(similarities):
            chunk = self.chunks[idx]
            if truck_filter and chunk["truck_id"] != truck_filter:
                continue
            candidates.append({
                "chunk_id": chunk["chunk_id"],
                "work_order": chunk["work_order"],
                "truck_id": chunk["truck_id"],
                "date": chunk["date"],
                "text": chunk["text"],
                "similarity_score": float(score)
            })
            
        candidates.sort(key=lambda x: x["similarity_score"], reverse=True)
        return candidates[:top_k]

if __name__ == "__main__":
    print("=== Step 1: Parsing Raw Logs ===")
    parsed = parse_maintenance_logs(RAW_MAINTENANCE_DUMP)
    print(f"Extracted {len(parsed)} structured work orders.")
    assert len(parsed) == 4
    assert parsed[1]["truck_id"] == "TRUCK-219"
    assert parsed[1]["work_order"] == "WO-10045"
    
    print("\n=== Step 2: Creating Overlapping Chunks ===")
    chunks = create_overlapping_chunks(parsed, chunk_words=20, overlap_words=5)
    print(f"Created {len(chunks)} chunks across all work orders.")
    assert len(chunks) >= 6
    assert all("truck_id" in c and "text" in c for c in chunks)
    
    print("\n=== Step 3: Indexing Vector Embeddings ===")
    index = LocalVectorIndex()
    index.index_chunks(chunks)
    assert index.embeddings.shape[1] == 384
    
    print("\n=== Step 4: Hybrid Safety Recall Retrieval ===")
    nhtsa_query = "turbocharger whining noise and metallic debris in engine oil"
    results = index.search(nhtsa_query, top_k=2)
    
    print("\nTop Retrieved Results:")
    for r in results:
        print(f"[{r['similarity_score']:.4f}] {r['work_order']} ({r['truck_id']}): {r['text'][:80]}...")
        
    top_hit = results[0]
    assert top_hit["truck_id"] == "TRUCK-219"
    assert top_hit["work_order"] == "WO-10045"
    assert top_hit["similarity_score"] > 0.35, f"Expected similarity > 0.35, got {top_hit['similarity_score']}"
    
    print("\n[SUCCESS] All Unit 4 Lab challenges verified successfully!")
