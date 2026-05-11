from fastapi import APIRouter
from app.api.v1 import clientes, profesionales

api_router = APIRouter()

api_router.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
api_router.include_router(profesionales.router, prefix="/profesionales", tags=["profesionales"])
