# AI Log Analyzer

A Python Flask application that reads Linux system logs and uses Groq AI (Llama 3.3-70b) to detect anomalies and security threats in plain English. Deployed to Azure App Service via a fully automated CI/CD pipeline.

**Live:** `https://heath-monitor-app-byddaufqefdnhjgk.westeurope-01.azurewebsites.net`

---

## How It Works

```
Linux Logs → Flask App → Groq AI Analysis → Human-Readable Report
```
```
Push code to GitHub → GitHub Actions builds Docker image → Pushes to ACR → App Service updates automatically.
```
---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI Engine | Groq API (Llama 3.3-70b) |
| Containerization | Docker |
| Registry | Azure Container Registry (ACR) |
| Hosting | Azure App Service |
| CI/CD | GitHub Actions |
| Auth | Azure Service Principal |

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/ridhaaa/ai-log-analyser

# Install dependencies
pip install -r requirements.txt

# Set your Groq API key
export GROQ_API_KEY="your-key-here"

# Run the app
python app.py

# Access at
http://127.0.0.1:5000
```

---

## Obstacles & Solutions

### 1. Azure Parallelism Restriction
**Error:** `No hosted parallelism has been purchased or granted`  
**Fix:** Configured the MacBook Air as a Self-Hosted Azure DevOps Agent to build locally, then migrated the pipeline to GitHub Actions.

### 2. ARM64 vs AMD64 Architecture Mismatch
**Error:** `exec /usr/local/bin/python3: exec format error`  
**Reason:** Mac M1 builds ARM64 images but Azure App Service runs AMD64.  
**Fix:**
```bash
docker build --platform linux/amd64 -t <registry>/<image>:<tag> .
```

### 3. Azure Authentication
**Error:** Basic Authentication (passwords) disabled in Azure.  
**Fix:** Created an Azure Service Principal and stored credentials as a GitHub Secret (`AZURE_CREDENTIALS`) for secure passwordless deployment.

### 4. Resource Not Found
**Error:** Pipeline couldn't find the App Service resource.  
**Fix:** Typo in the resource name — once the YAML matched the exact Azure name, deployment succeeded.

---

## RESULTS
![Log Stream](screenshots/log-stream.png)
![Output](screenshots/output.png)
Tried the logs from log stream.
![Output](screenshots/output1.png)
![Deployment Center](screenshots/deployment-center.png)
