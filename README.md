# Package Kubernetes Applications using Helm | MLOps Series - Episode 6

Welcome to **Episode 6** of the MLOps Series.

In the previous episode, we automated the deployment of our Student Score Prediction API using **Jenkins CI/CD**.

As our application grows, managing multiple Kubernetes YAML files becomes difficult. In this episode, we'll solve that problem using **Helm**, the package manager for Kubernetes.

By the end of this video, you'll know how to package, configure, install, upgrade, and rollback Kubernetes applications using Helm.

---

# 🎯 What You'll Learn

- What is Helm?
- Why Helm is needed
- Problems with plain Kubernetes YAML files
- Helm Architecture
- Helm Charts
- Installing Helm
- Creating a Helm Chart
- Understanding Chart.yaml
- Understanding values.yaml
- Helm Templates
- Deploying our Student ML API using Helm
- Upgrading Helm Releases
- Rollback a Release
- Helm Best Practices

---

# Why Helm?

Imagine your application contains:

- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- Horizontal Pod Autoscaler
- Persistent Volume
- Persistent Volume Claim

Managing all these YAML files manually becomes difficult.

For every environment (Dev, QA, Production), you'll need separate YAML files.

Helm solves this problem.

---

# Without Helm

```
deployment-dev.yaml
deployment-qa.yaml
deployment-prod.yaml

service-dev.yaml
service-qa.yaml
service-prod.yaml

configmap-dev.yaml
configmap-qa.yaml
configmap-prod.yaml
```

Lots of duplication.

---

# With Helm

```
One Helm Chart

↓

values-dev.yaml

values-qa.yaml

values-prod.yaml
```

One template

Multiple environments

---

# What is Helm?

Helm is the package manager for Kubernetes.

Just like

- apt → Ubuntu
- yum → RHEL
- npm → NodeJS
- pip → Python

Helm manages Kubernetes applications.

Instead of writing dozens of YAML files, we create reusable templates.

---

# Helm Architecture

```
Developer

     │

     ▼

Helm Chart

     │

     ▼

Values.yaml

     │

     ▼

Templates

     │

     ▼

Kubernetes Cluster
```

---

# Our Existing Project

```
student-ml-project

api/

src/

Dockerfile

Jenkinsfile

kubernetes/
    deployment.yaml
    service.yaml
```

We'll convert the Kubernetes folder into a Helm Chart.

---

# Installing Helm

Ubuntu

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

Verify

```bash
helm version
```

---

# Create Helm Chart

```bash
helm create student-ml-chart
```

Project

```
student-ml-chart

Chart.yaml

values.yaml

templates/

charts/

README.md
```

---

# Chart.yaml

Contains metadata

- Chart Name
- Version
- Description
- Application Version

---

# values.yaml

Stores configurable values

Example

```yaml
replicaCount: 2

image:
  repository: student-m1-api
  tag: "17"

service:
  type: NodePort
  port: 8000

namespace: mlops-dev
```

---

# Templates

Instead of hardcoding values

Deployment

```
replicas: 2
```

We'll write

```
replicas: {{ .Values.replicaCount }}
```

Now changing values.yaml automatically updates the deployment.

---

# Deploy using Helm

Install

```bash
helm install student-ml student-ml-chart \
-n mlops-dev
```

Check

```bash
helm list -n mlops-dev
```

Pods

```bash
kubectl get pods -n mlops-dev
```

---

# Upgrade Application

```bash
helm upgrade student-ml student-ml-chart \
-n mlops-dev
```

---

# Rollback

Show history

```bash
helm history student-ml \
-n mlops-dev
```

Rollback

```bash
helm rollback student-ml 1 \
-n mlops-dev
```

---

# Uninstall

```bash
helm uninstall student-ml \
-n mlops-dev
```

---

# Benefits of Helm

✔ Reusable Templates

✔ Version Control

✔ Easy Upgrades

✔ Easy Rollbacks

✔ Environment Specific Configuration

✔ Less YAML

✔ Production Ready

---

# Project Structure After Helm

```
student-ml-project/

api/

src/

Dockerfile

Jenkinsfile

helm/

└── student-ml-chart/
    ├── Chart.yaml
    ├── values.yaml
    ├── charts/
    └── templates/
        ├── deployment.yaml
        ├── service.yaml
        ├── _helpers.tpl
        └── NOTES.txt
```

---

# Source Code

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

Episode 5
CI/CD for Machine Learning API using Jenkins

---

# Next Episode

GitOps using Argo CD

Automatically Deploy Applications from GitHub to Kubernetes

---

⭐ If you enjoyed this video, don't forget to Star the repository and Subscribe to the channel.

Happy Learning 🚀
