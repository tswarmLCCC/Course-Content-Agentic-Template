# COSC 2060: Modern Data Engineering & AI Infrastructure

- **Format**: 16 Weeks (8 Units)
- **Target Audience**: College Sophomores (2nd-year undergraduates)
- **Prerequisites**: Beginning SQL (relational basics) & Beginning Machine Learning (familiar with features, labels, and train/test splits)
- **Pedagogical Model**: Backward Design (Target-Driven Architecture) with deliberate cognitive scaffolding ("I Do, We Do, You Do")
- **Philosophy**: 100% open-source, local-first lab environment, free of vendor lock-in.


---

## Course Terminal Outcomes
By the end of week 16, students will have built a functional, production-ready AI data ecosystem:
1. **Target-Driven Pipelines**: Transform raw multimodal data backward from downstream ML schema requirements.
2. **Prevent Model Sabotage**: Implement defensive tactics (point-in-time joins, temporal splitting) to eliminate look-ahead bias.
3. **Data as a Service (DaaS)**: Serve production data products via secured, validated FastAPI REST endpoints.
4. **Agentic Bridges (MCP)**: Expose databases and APIs to autonomous LLMs using the Model Context Protocol.
5. **Orchestration**: Automate ingestion-to-inference pipelines using DAG orchestrators (Dagster / Prefect).

---

## 16-Week / 8-Unit Progression & Deliverables
| Unit | Weeks | Title | Core Technology | DS → DE Transition Notebook | Slot 2 Slide Deck (.pptx) | Flipped Guide & Video Scripts | Reading Guide | Applied Lab Guide |
|---|---|---|---|---|---|---|---|---|
| **Unit 1** | 1–2 | The Relational Foundation | DuckDB, Advanced SQL | [Unit 1 Notebook](content/notebooks/unit_01_ds_to_engine.ipynb) | [Unit 1 Deck (.pptx)](content/slides/unit_01_coding_clinic.pptx) | [Unit 1 Flipped Guide](content/flipped_classroom/unit_01_guide.md) | [Reading](content/readings/unit_01_relational_foundation.md) | [Lab Guide](content/labs/unit_01_feature_matrix_lab.md) |
| **Unit 2** | 3–4 | The Anomaly Engine | Polars, Scikit-Learn | [Unit 2 Notebook](content/notebooks/unit_02_ds_to_engine.ipynb) | [Unit 2 Deck (.pptx)](content/slides/unit_02_coding_clinic.pptx) | [Unit 2 Flipped Guide](content/flipped_classroom/unit_02_guide.md) | [Reading](content/readings/unit_02_anomaly_engine.md) | [Lab Guide](content/labs/unit_02_anomaly_pipeline_lab.md) |
| **Unit 3** | 5–6 | The Visual Sensor Layer | OpenCV, Python OS | [Unit 3 Notebook](content/notebooks/unit_03_ds_to_engine.ipynb) | [Unit 3 Deck (.pptx)](content/slides/unit_03_coding_clinic.pptx) | [Unit 3 Flipped Guide](content/flipped_classroom/unit_03_guide.md) | [Reading](content/readings/unit_03_visual_sensor_layer.md) | [Lab Guide](content/labs/unit_03_fleet_vision_manifest_lab.md) |
| **Unit 4** | 7–8 | Unstructured Text & RAG | Sentence-Transformers, Chroma | [Unit 4 Notebook](content/notebooks/unit_04_ds_to_engine.ipynb) | [Unit 4 Deck (.pptx)](content/slides/unit_04_coding_clinic.pptx) | [Unit 4 Flipped Guide](content/flipped_classroom/unit_04_guide.md) | [Reading](content/readings/unit_04_unstructured_text_rag.md) | [Lab Guide](content/labs/unit_04_maintenance_rag_lab.md) |
| **Unit 5** | 9–10 | Data as a Service (API Layer) | FastAPI, Pydantic v2 | [Unit 5 Notebook](content/notebooks/unit_05_ds_to_engine.ipynb) | [Unit 5 Deck (.pptx)](content/slides/unit_05_coding_clinic.pptx) | [Unit 5 Flipped Guide](content/flipped_classroom/unit_05_guide.md) | [Reading](content/readings/unit_05_data_as_a_service.md) | [Lab Guide](content/labs/unit_05_logistics_api_lab.md) |
| **Unit 6** | 11–12 | The Agentic Interface (MCP) | Model Context Protocol, JSON-RPC | [Unit 6 Notebook](content/notebooks/unit_06_ds_to_engine.ipynb) | [Unit 6 Deck (.pptx)](content/slides/unit_06_coding_clinic.pptx) | [Unit 6 Flipped Guide](content/flipped_classroom/unit_06_guide.md) | [Reading](content/readings/unit_06_agentic_interface_mcp.md) | [Lab Guide](content/labs/unit_06_mcp_server_lab.md) |
| **Unit 7** | 13–14 | Orchestration & Automation | Dagster / Asset DAGs | [Unit 7 Notebook](content/notebooks/unit_07_ds_to_engine.ipynb) | [Unit 7 Deck (.pptx)](content/slides/unit_07_coding_clinic.pptx) | [Unit 7 Flipped Guide](content/flipped_classroom/unit_07_guide.md) | [Reading](content/readings/unit_07_orchestration_automation.md) | [Lab Guide](content/labs/unit_07_unsleeping_pipeline_lab.md) |
| **Unit 8** | 15–16 | Capstone Defense & Handoff | Docker, Blind Evaluation Batch | [Unit 8 Notebook](content/notebooks/unit_08_ds_to_engine.ipynb) | [Unit 8 Deck (.pptx)](content/slides/unit_08_coding_clinic.pptx) | [Unit 8 Flipped Guide](content/flipped_classroom/unit_08_guide.md) | [Reading](content/readings/unit_08_capstone_defense.md) | [Lab Guide](content/labs/unit_08_capstone_defense_lab.md) |

---

## Lab Hardware & Local Environment
- **Runtime**: Local Python 3.10+ virtual environment (`venv` or `conda`).
- **Engines**: DuckDB (in-process OLAP), Polars (Rust DataFrame), FastAPI, Sentence-Transformers.
- **Local AI**: Ollama running small parameter instruction models (e.g. `qwen2.5:0.5b` or `qwen2.5:1.5b` or `llama3.2:1b/3b`).

