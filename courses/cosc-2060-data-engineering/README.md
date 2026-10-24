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
| Unit | Weeks | Title | Core Technology | Reading Guide | Applied Lab Guide | Code Deliverables |
|---|---|---|---|---|---|---|
| **Unit 1** | 1–2 | The Relational Foundation | DuckDB, Advanced SQL | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_01_relational_foundation.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_01_feature_matrix_lab.md) | [Postgres Ref](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/reference/postgres_temporal_joins_reference.md) |
| **Unit 2** | 3–4 | The Anomaly Engine | Polars, Scikit-Learn | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_02_anomaly_engine.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_02_anomaly_pipeline_lab.md) | [1M Row Gen](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/generate_fuel_data.py), [Benchmark](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/reference/pandas_vs_polars_memory_benchmark.md) |
| **Unit 3** | 5–6 | The Visual Sensor Layer | OpenCV, Python OS | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_03_visual_sensor_layer.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_03_fleet_vision_manifest_lab.md) | Letterbox & YOLO Conversion Suite |
| **Unit 4** | 7–8 | Unstructured Text & RAG | Sentence-Transformers, Chroma | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_04_unstructured_text_rag.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_04_maintenance_rag_lab.md) | [Starter Script](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/lab4_starter.py) |
| **Unit 5** | 9–10 | Data as a Service (API Layer) | FastAPI, Pydantic v2 | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_05_data_as_a_service.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_05_logistics_api_lab.md) | [Starter Script](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/lab5_starter.py) |
| **Unit 6** | 11–12 | The Agentic Interface (MCP) | Model Context Protocol, JSON-RPC | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_06_agentic_interface_mcp.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_06_mcp_server_lab.md) | [Starter Script](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/lab6_starter.py) |
| **Unit 7** | 13–14 | Orchestration & Automation | Dagster / Asset DAGs | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_07_orchestration_automation.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_07_unsleeping_pipeline_lab.md) | [Starter Script](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/lab7_starter.py) |
| **Unit 8** | 15–16 | Capstone Defense & Handoff | Docker, Blind Evaluation Batch | [Reading](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/readings/unit_08_capstone_defense.md) | [Lab Guide](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/unit_08_capstone_defense_lab.md) | [Starter Script](file:///c:/dev/Course-Content-Agentic-Template/courses/cosc-2060-data-engineering/content/labs/lab8_starter.py) |

---

## Lab Hardware & Local Environment
- **Runtime**: Local Python 3.10+ virtual environment (`venv` or `conda`).
- **Engines**: DuckDB (in-process OLAP), Polars (Rust DataFrame), FastAPI, Sentence-Transformers.
- **Local AI**: Ollama running small parameter instruction models (e.g. `qwen2.5:0.5b` or `qwen2.5:1.5b` or `llama3.2:1b/3b`).

