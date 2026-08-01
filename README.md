# CI/CD for Machine Learning API using Jenkins | MLOps Series - Episode 5

Welcome to **Episode 5** of the MLOps Series.

In this episode, we'll automate the deployment of our **Student Score Prediction API** using **Jenkins CI/CD**. Every code change pushed to GitHub will automatically trigger a Jenkins pipeline that builds, trains, packages, and deploys the application to our Kubernetes (Kind) cluster.

---

## 🎯 What You'll Learn

- Introduction to Continuous Integration (CI)
- Introduction to Continuous Delivery (CD)
- Why CI/CD is important in MLOps
- Jenkins Architecture
- Installing Jenkins on Ubuntu
- Creating a Jenkins Pipeline
- Connecting Jenkins with GitHub
- Creating a Jenkinsfile
- Building Docker Images automatically
- Training the ML Model inside the Pipeline
- Loading Docker Images into Kind Cluster
- Updating Kubernetes Deployment
- Verifying Rollout Status
- Smoke Testing the Application

---

# CI/CD Workflow

```
Developer
      │
      ▼
Push Code to GitHub
      │
      ▼
Jenkins Pipeline
      │
      ├── Checkout Code
      ├── Install Python Dependencies
      ├── Train ML Model
      ├── Build Docker Image
      ├── Load Image into Kind
      ├── Deploy to Kubernetes
      ├── Verify Rollout
      └── Smoke Test
      │
      ▼
Student ML API Running
```

---

# Project Architecture

```
                GitHub
                   │
                   ▼
              Jenkins Pipeline
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
 Train ML Model        Build Docker Image
        │                     │
        └──────────┬──────────┘
                   ▼
          Load Image into Kind
                   │
                   ▼
        Kubernetes Deployment
                   │
                   ▼
        Student ML REST API
```

---

# Project Structure

```
student-ml-project/

├── api/
├── config/
├── data/
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── namespace.yaml
├── models/
├── src/
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
```

---

# Jenkins Pipeline Stages

✔ Checkout Source Code

✔ Install Dependencies

✔ Train Machine Learning Model

✔ Build Docker Image

✔ Verify Kind Cluster

✔ Load Image into Kind

✔ Create Namespace

✔ Deploy Kubernetes Resources

✔ Update Deployment

✔ Verify Rollout

✔ Smoke Test

---

# Technologies Used

- Python
- FastAPI
- Scikit-Learn
- Pandas
- Docker
- Kubernetes
- Kind Cluster
- Jenkins
- GitHub
- YAML
- Linux (Ubuntu)

---

# Prerequisites

- Ubuntu Linux
- Docker Installed
- Kind Cluster
- kubectl
- Jenkins
- Python 3
- Git

---

# Clone Repository

```bash
git clone https://github.com/harpal1990/student-ml-project.git

cd student-ml-project
```

---

# Jenkins Pipeline

The pipeline automatically performs the following tasks:

- Clone Repository
- Install Dependencies
- Train Model
- Build Docker Image
- Load Image into Kind Cluster
- Deploy Application
- Verify Deployment
- Display Kubernetes Resources

No manual deployment is required.

---

# Verify Deployment

```bash
kubectl get pods -n mlops-dev

kubectl get deployment -n mlops-dev

kubectl get svc -n mlops-dev
```

---

# Access Application

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

Health Check

```
http://localhost:8000/health
```

---

# Jenkins Dashboard

You can monitor:

- Build History
- Console Output
- Pipeline Stages
- Deployment Status
- Failed Builds
- Successful Deployments

---

# Source Code

GitHub Repository

https://github.com/harpal1990/student-ml-project

---

# Previous Episodes

Episode 1
Introduction to AI, Machine Learning & MLOps

Episode 2
Build Machine Learning REST API using FastAPI

Episode 3
Dockerize Machine Learning API

Episode 4
Deploy Machine Learning API on Kubernetes using Kind

---

# Next Episode

Package Kubernetes Applications using Helm

---

⭐ If you enjoyed this video, don't forget to Star the repository and Subscribe to the channel.

Happy Learning 🚀
