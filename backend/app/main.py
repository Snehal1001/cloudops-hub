from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.api.project_routes import router as project_router

Base.metadata.create_all(bind = engine)

app = FastAPI(
    title="CloudOps Hub API",
    version="1.0.0"
)

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