# Unit 04: Open-Source Guide — Self-Hosting n8n Workflow Automation via Docker & Desktop

> **Course**: AIML 2050 — AI in the Workforce  
> **Toolchain**: n8n, Docker / Node.js, Webhooks  
> **Cost**: $0.00 (Zero-cost open-source deployment)

---

## 1. Overview
**n8n** is a leading fair-code workflow automation platform. Unlike proprietary cloud services that charge per task execution, n8n can be self-hosted locally for free with zero task execution limits.

---

## 2. Option A: Quickstart via NPX (Zero Setup Required)
If you have Node.js installed:
```powershell
# Run n8n locally without installation
npx n8n
```
Open your browser to `http://localhost:5678`.

---

## 3. Option B: Self-Hosting via Docker
For persistent, production-like local hosting:
```powershell
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

---

## 4. Building a Resilient Webhook Test
To test webhooks locally:
```powershell
# Send a test POST request to your n8n test webhook
Invoke-RestMethod -Uri "http://localhost:5678/webhook-test/my-agent" -Method POST -Body (@{
    customer_id = "CUST-9921"
    request_text = "I need to update my shipping address immediately"
} | ConvertTo-Json) -ContentType "application/json"
```
Verify that the inbound trigger node in n8n lights up green and extracts the JSON fields correctly.
