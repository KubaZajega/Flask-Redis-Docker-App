# Flask‑Redis‑Docker‑App

A simple Flask application using Redis, containerized with Docker and now orchestrated with **Kubernetes**.  
This project was created **as part of university DevOps exercises**.

## 🚀 Features

- **Flask Web App**: Simple Python backend running on port 5050.
- **Redis Integration**: Used for counting page visits.
- **Dockerized**: Ready-to-use `Dockerfile`.
- **Orchestration**:
  - **Docker Compose**: For quick local development.
  - **Kubernetes (K8s)**: Scalable deployment with Minikube.

---

## 🛠 Prerequisites

Before running the app, ensure you have the following installed:
* **Docker Desktop**
* **Minikube**
* **kubectl**

---

## 📦 Running with Docker Compose

To start the application using Docker Compose:

```
docker-compose up --build
```

## ☸️ Running on Kubernetes (Minikube)
Follow these steps to deploy the application on a local Kubernetes cluster:

1. Start Minikube

```
minikube start --driver=docker
```
2. Build Image in Minikube Environment
```
eval $(minikube docker-env)
docker build -t flask-redis-app:latest .
```
3. Deploy to Kubernetes
```
kubectl apply -f k8s/redis.yaml
kubectl apply -f k8s/flask-app.yaml
```
4. Scaling the Application
```
kubectl scale deployment flask-app --replicas=2
```
5. Access the Application
```
minikube service flask-service
```
