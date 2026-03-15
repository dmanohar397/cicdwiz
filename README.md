# CICDWiz

CICDWiz is a DevOps automation tool that generates CI/CD pipelines automatically based on project configuration.

## Features

- Generate CI pipelines automatically
- Supports Python and Node.js
- Dockerfile generation
- FastAPI backend
- Hosted on Azure App Service

## API Endpoints

GET /health

POST /generate

Example request:

```json
{
 "repo": "https://github.com/user/project",
 "language": "python",
 "framework": "fastapi",
 "docker": true,
 "cloud": "azure"
}
```

## Tech Stack

- FastAPI
- Python
- Docker
- Azure App Service

## Project Goal

Automate CI/CD pipeline setup for developers by generating ready-to-use configuration files.