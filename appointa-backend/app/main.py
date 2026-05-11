from fastapi import FastAPI
from app.database import engine, Base
from app.api.v1.router import api_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Appointa API",
    description="Backend para Appointa - Sistema de gestión de turnos",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Appointa API is running", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
