# Gemal World Infrastructure

> Infrastructure and deployment configuration for my personal AWS environment, supporting multiple containerized applications using Kubernetes, Docker, and Infrastructure as Code.

## Overview

This repository contains the infrastructure and deployment configuration for two applications:

| Application | Description | Repository |
|---|---|---|
| **Gemal World** | Java / Spring Boot web application | `ghornemo/gemal-world` |
| **Personal Website** | Standalone personal website | `ghornemo/website` |

Application source code is maintained independently. This repository is responsible for **deploying, configuring, and operating those applications in AWS**.

---

## Architecture

```text
┌─────────────────────────────┐
│          GitHub             │
├─────────────────────────────┤
│  Gemal World     Website    │
└──────┬──────────────┬───────┘
       │              │
       ▼              ▼
┌─────────────┐ ┌─────────────┐
│ Docker Image│ │ Docker Image│
└──────┬──────┘ └──────┬──────┘
       │                │
       └───────┬────────┘
               ▼
       ┌───────────────┐
       │ Container     │
       │ Registry      │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │  Kubernetes   │
       │    Cluster    │
       ├───────────────┤
       │ Gemal World   │
       │ Website       │
       └───────┬───────┘
               │
               ▼
              AWS
```

---

## Repository Structure

```text
gemal-world-infrastructure/
│
├── kubernetes/
│   ├── gemal-world/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ...
│   │
│   └── website/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── ...
│
├── terraform/
│   └── ...
│
├── .gitignore
└── README.md
```

---

## Kubernetes

The `kubernetes/` directory contains the manifests required to deploy each application.

Each application is managed independently and can include:

- Deployments
- Services
- Ingress
- ConfigMaps
- Secrets
- Health checks
- Resource requests and limits

This allows each workload to be deployed, updated, scaled, and operated independently.

---

## Infrastructure as Code

The `terraform/` directory will contain the Terraform configuration used to provision the underlying AWS environment.

The goal is to make the infrastructure **reproducible and version controlled**, rather than relying on resources configured manually through the AWS Console.

Planned infrastructure includes:

- VPC and networking
- Kubernetes compute resources
- IAM roles and policies
- Security groups
- Container registry
- Load balancing
- DNS
- Supporting AWS services

---

## Deployment Flow

```text
Code Change
    │
    ▼
  GitHub
    │
    ▼
Build & Test
    │
    ▼
Docker Image
    │
    ▼
Container Registry
    │
    ▼
Kubernetes Deployment
    │
    ▼
    AWS
```

The long-term goal is for this process to be automated through CI/CD pipelines.

---

## Technology Stack

| Area | Technology |
|---|---|
| **Cloud** | AWS |
| **Containers** | Docker |
| **Orchestration** | Kubernetes |
| **Infrastructure as Code** | Terraform |
| **CI/CD** | GitHub Actions |
| **Backend** | Java / Spring Boot |
| **Operating System** | Linux |

---

## Project Goals

This environment is being built as a practical implementation of modern cloud and DevOps practices.

Key areas include:

- Containerized application deployment
- Kubernetes workload management
- AWS infrastructure design
- Infrastructure as Code
- CI/CD automation
- Networking and load balancing
- Health checks and application resiliency
- Monitoring and observability
- Secure configuration and secrets management
- Production-style deployment practices

---

## Related Repositories

### Gemal World

Java / Spring Boot application deployed through this infrastructure.

**Repository:** `ghornemo/gemal-world`

### Personal Website

Standalone web application deployed alongside Gemal World.

**Repository:** `ghornemo/website`

---

## Roadmap

- [ ] Containerize both applications
- [ ] Create Kubernetes deployments and services
- [ ] Deploy applications to Kubernetes
- [ ] Configure ingress and external access
- [ ] Add health checks and resource limits
- [ ] Add CI/CD with GitHub Actions
- [ ] Define AWS infrastructure with Terraform
- [ ] Add monitoring and observability
- [ ] Document the final architecture

---

## Status

🚧 **Active Development**

This repository is being built incrementally as the environment evolves from manually deployed applications into a reproducible, automated cloud infrastructure.
