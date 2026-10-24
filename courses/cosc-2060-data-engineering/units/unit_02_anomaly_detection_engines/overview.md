# Unit 02 Overview: Real-Time Anomaly Detection & Schema Enforcement

In Unit 02, we transition from static batch transformations to dynamic, defensive data quality pipelines. In production data engineering, unvalidated data is a silent disaster. This week focuses on implementing defensive schema validation with Pydantic and building streaming anomaly detection algorithms over sliding temporal windows.

---

## Weekly Contact Hour Budget (300 Minutes Total)
- **Conceptual Study & Readings (150 min)**: Master defensive typing, streaming window semantics (tumbling vs sliding), and statistical outlier gates (Z-Score & IQR).
- **Asynchronous Preparation & Drills (60 min)**: Work through schema contract edge cases, null-handling traps, and temporal order verifications.
- **Hands-on Engineering Lab (90 min)**: Build the Streaming Anomaly Detection Engine pipeline processing real-time sensor streams.

---

## Measurable Learning Objectives
By the end of this unit, you will be able to:
1. **Enforce** strict schema contracts and type safety using Pydantic models to reject malformed records before ingestion.
2. **Implement** sliding temporal window aggregations to compute rolling statistics over timestamped telemetry.
3. **Construct** defensive anomaly filters using statistical thresholds (Z-score and interquartile range) to isolate sensor spikes.
4. **Route** corrupted or anomalous records to dead-letter quarantine queues with audit metadata.

---

## Weekly Milestones & Deliverables
- [ ] Read [Unit 02 Required Readings & Concepts](reading.md).
- [ ] Complete [Unit 02 Asynchronous Preparation & Drills](drills.md).
- [ ] Implement and test [Unit 02 Applied Lab Assignment](lab_guide.md).
- [ ] Complete [Unit 02 Knowledge Check](quiz.md) (10 questions, 3 attempts).
