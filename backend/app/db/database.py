from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./cloudops.db"

# engine Handles DB connections.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Creates DB sessions per req
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()