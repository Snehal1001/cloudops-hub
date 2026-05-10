from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.project_routes import router as project_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(project_router)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(project_router)

@app.get("/")
async def root():
    return {"message": "CloudOps Hub API Running"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }