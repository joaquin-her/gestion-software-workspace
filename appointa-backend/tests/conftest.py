import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

# Importar todos los modelos para asegurar que estén registrados con Base
from app.models.user import User
from app.models.cliente import Cliente
from app.models.profesional import Profesional

# Base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """Fixture que crea tablas, proporciona sesión de base de datos y limpia después de cada test"""
    # Crear tablas antes del test
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()
        # Eliminar tablas después del test
        Base.metadata.drop_all(bind=engine)
