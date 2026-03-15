from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CICDWiz API",
    description="Generate CI/CD pipelines automatically",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PipelineRequest(BaseModel):
    repo: str
    language: str
    framework: str
    docker: bool
    cloud: str


@app.get("/health")
def health():
    return {"status": "CICDWiz running"}


@app.post("/generate")
def generate(req: PipelineRequest):

    workflow, dockerfile = generate_pipeline(req)

    return {
        "workflow": workflow,
        "dockerfile": dockerfile
    }