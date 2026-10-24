# [Institution Name] [Department Name]
## Live Demonstration Contingency Runbook & Flight Plan
**Project Name:** [Capstone Project Title]  
**Target Execution Window:** Exactly 3 Minutes (180 Seconds)  
**Host Workstation Pre-Flight Window:** T-Minus 15 Minutes  

---

## 1. Pre-Flight Workstation Checklist (T-Minus 15 Minutes)
- [ ] 1. Clean workstation reboot (terminate orphan threads and clear memory allocations).
- [ ] 2. Launch background services / containers: confirm active process table.
- [ ] 3. Verify Health Endpoint: `curl -f http://localhost:8000/health` -> HTTP 200 OK.
- [ ] 4. Open terminal windows with high-contrast fonts (Consolas 18pt minimum).
- [ ] 5. Open presentation and markdown scratchpad side-by-side.
- [ ] 6. Enable "Do Not Disturb"; disable Slack, email popups, and sleep timers.

---

## 2. The 3-Minute Live Demo Flight Script
```
[ 00:00 - 00:30 ]: Scenario Framing & Input Injection
  - Narrative: "Let us observe the system in action under live operational telemetry."
  - Action: Copy-paste Query 1 from scratchpad into prompt interface.
  - Expected Telemetry: Boundary airlock logs [PASS], input sanitized.

[ 00:30 - 01:15 ]: Core System Execution & Processing
  - Narrative: "Notice the supervisor coordinating tasks and updating shared state."
  - Action: Point to live console logs showing component telemetry.
  - Expected Telemetry: Core engine returns structured data; auditor verifies bounds.

[ 01:15 - 02:00 ]: Intentional Fault Injection (The Chaos Demonstration)
  - Narrative: "In the real world, hardware drops. Watch what happens when we pull the sensor offline."
  - Action: Execute fault trigger or simulate sensor drop.
  - Expected Telemetry: Tool timeout caught -> Circuit breaker trips to OPEN -> Fallback engaged.

[ 02:00 - 02:45 ]: Safe Output Delivery & Resilience Verification
  - Narrative: "The UI remains responsive, clearly labeling results as an offline fallback."
  - Action: Highlight final output schema and zero data leakage.

[ 02:45 - 03:00 ]: Conclusion & Transition to Cross-Examination
  - Narrative: "Our system has proven resilient under live chaos. We welcome your questions."
```

---

## 3. The 3-Tier Failover Contingency Matrix
| Failure Scenario | Immediate Action | Spoken Pivot Script |
| :--- | :--- | :--- |
| **Tier 1 Glitch:** Primary service stalls or network drops. | Run `python test_mock_replay.py`. | *"As you can see, the live network has encountered latency; let me switch to our offline telemetry replay to demonstrate the consensus logic."* |
| **Tier 2 Glitch:** Application crashes or container port collides. | Open `demo_assets/demo_recording.mp4` fullscreen. | *"Our staging instance encountered a port conflict; here is our pre-recorded end-to-end trace showing the exact telemetry verified during peer audit."* |
| **Tier 3 Glitch:** Complete workstation hardware or power crash. | Hand physical printout of Executive Scorecard to panel evaluators and proceed verbally. | *"Hardware glitches happen in enterprise IT. Let us focus on the architectural engineering and empirical stress test results in your dossier."* |
