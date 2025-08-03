## 🚀 Sentiment Analysis API (Azure + Docker)

[![Build Status](https://img.shields.io/github/actions/workflow/status/niketbhatt2002/sentiment-api-azure/docker-build.yml?label=Build&logo=github&style=flat-square)](https://github.com/niketbhatt2002/sentiment-api-azure/actions)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker&style=flat-square)](https://hub.docker.com/)
[![Azure](https://img.shields.io/badge/hosted%20on-Azure-blue?logo=microsoft-azure&style=flat-square)](https://portal.azure.com/)
[![License](https://img.shields.io/github/license/niketbhatt2002/sentiment-api-azure?style=flat-square)](LICENSE)

A lightweight and production-ready **sentiment analysis API** built with **Python**, containerized with **Docker**, and deployed to **Azure App Service**. It accepts raw text and returns the sentiment label and confidence scores using modern NLP tools.

---

## ✨ Features

- 🔍 Analyze sentiment (positive / neutral / negative)
- ⚡ Fast and RESTful API (FastAPI-based)
- 🐳 Dockerized for consistency across environments
- ☁️ Azure-ready deployment
- 📊 Returns label + probability scores
- 🧪 Swagger UI for testing

---

## 🔧 Tech Stack

- **Framework**: FastAPI
- **NLP**: TextBlob / HuggingFace / VADER *(update as needed)*
- **Deployment**: Docker + Azure App Service
- **CI/CD**: GitHub Actions
- **Docs**: Auto-generated via Swagger UI

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/niketbhatt2002/sentiment-api-azure.git
cd sentiment-api-azure
2. Run with Docker
bash
Copy
Edit
docker build -t sentiment-api .
docker run -d -p 8000:8000 sentiment-api
Then go to: http://localhost:8000/docs for Swagger UI.

3. Without Docker (local)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
🧪 Example Usage
Request
bash
Copy
Edit
POST /predict
Content-Type: application/json

{
  "text": "I absolutely love this!"
}
Response
json
Copy
Edit
{
  "sentiment": "positive",
  "confidence": {
    "positive": 0.91,
    "neutral": 0.07,
    "negative": 0.02
  }
}
🐙 CI/CD with GitHub Actions
The repo includes a GitHub Actions workflow (.github/workflows/docker-build.yml) that:

Builds the Docker image

Optionally pushes it to Docker Hub or Azure Container Registry

Can auto-deploy to Azure App Service

☁️ Azure Deployment Steps
Create an Azure App Service & Resource Group.

Connect to GitHub repo via Deployment Center.

Set up environment variables (if needed).

Optionally push Docker image to Azure Container Registry (ACR).

🧾 API Documentation
Once running, you can access:

Swagger UI → /docs

ReDoc → /redoc

📄 License
This project is licensed under the MIT License.

👤 Author
Niket Bhatt
GitHub: @niketbhatt2002

