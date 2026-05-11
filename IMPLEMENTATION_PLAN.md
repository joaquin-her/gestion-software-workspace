# Implementation Plan - Backend Appointa

## Objetivo
Construir el backend desde cero para la aplicación Appointa, comenzando con SCRUM-121: Edición de Perfil Del Cliente y Profesional [BACK].

## Stack Tecnológico

### Backend
- **Framework**: FastAPI (Python 3.11+)
  - Rápido, moderno, con documentación automática (Swagger/OpenAPI)
  - Soporte nativo para async/await
  - Validación automática con Pydantic
  
### Base de Datos
- **ORM**: SQLAlchemy 2.0
- **Database**: PostgreSQL 15
- **Migrations**: Alembic

### Autenticación
- **JWT**: python-jose
- **Password Hashing**: passlib (bcrypt)

### Validación
- **Pydantic v2**: Validación de datos y schemas

### Docker
- **Docker**: Contenedorización
- **docker-compose**: Orquestación de servicios

## Estructura del Proyecto

```
appointa-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point de FastAPI
│   ├── config.py               # Configuración (env vars)
│   ├── database.py             # Conexión a DB
│   ├── models/                 # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── base.py            # Base model
│   │   ├── user.py            # Usuario base
│   │   ├── cliente.py         # Modelo Cliente
│   │   └── profesional.py     # Modelo Profesional
│   ├── schemas/                # Schemas Pydantic (DTOs)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── cliente.py
│   │   └── profesional.py
│   ├── api/                    # Rutas API
│   │   ├── __init__.py
│   │   ├── deps.py            # Dependencias (auth, db)
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── router.py      # Router principal v1
│   │   │   ├── auth.py        # Endpoints de auth
│   │   │   ├── clientes.py    # Endpoints de clientes
│   │   │   └── profesionales.py # Endpoints de profesionales
│   ├── core/                   # Lógica core
│   │   ├── __init__.py
│   │   ├── security.py        # JWT, password hashing
│   │   └── config.py          # Settings
│   └── utils/                  # Utilidades
│       ├── __init__.py
│       └── helpers.py
├── alembic/                    # Migrations
│   ├── versions/
│   └── env.py
├── tests/                      # Tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_clientes.py
│   └── test_profesionales.py
├── .env.example                # Variables de entorno ejemplo
├── .gitignore
├── Dockerfile                  # Docker image
├── docker-compose.yml          # Orquestación
├── requirements.txt            # Dependencias Python
├── alembic.ini                 # Config Alembic
└── start.ps1                   # Script para levantar la app (Windows)
```

## Fase 1: Setup Inicial

### 1.1 Crear estructura base
- Crear directorios del proyecto
- Inicializar git
- Crear archivos de configuración

### 1.2 Configurar dependencias
```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.25
alembic==1.13.1
psycopg2-binary==2.9.9
pydantic==2.5.3
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
email-validator==2.1.0
pytest==7.4.4
pytest-asyncio==0.23.3
httpx==0.26.0
```

### 1.3 Configurar Docker
- Dockerfile para la app FastAPI
- docker-compose.yml con:
  - Servicio API (FastAPI)
  - Servicio PostgreSQL
  - Volúmenes para persistencia
  - Redes internas

### 1.4 Script start.ps1
- Script PowerShell para:
  - Construir imágenes Docker
  - Levantar servicios con docker-compose
  - Ejecutar migrations
  - Mostrar logs
  - Manejo de errores

## Fase 2: Modelos de Datos

### 2.1 Modelo Base
```python
class Base(DeclarativeBase):
    pass

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)
```

### 2.2 Modelo User (Base)
```python
class User(Base, TimestampMixin):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(255))
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[str] = mapped_column(String(50))  # 'cliente', 'profesional', 'admin'
```

### 2.3 Modelo Cliente
```python
class Cliente(Base, TimestampMixin):
    __tablename__ = "clientes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    dni: Mapped[Optional[str]] = mapped_column(String(20))
    date_of_birth: Mapped[Optional[date]] = mapped_column(Date)
    address: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    notes: Mapped[Optional[str]] = mapped_column(Text)  # Notas internas
    
    # Relaciones
    user: Mapped["User"] = relationship(back_populates="cliente")
```

### 2.4 Modelo Profesional
```python
class Profesional(Base, TimestampMixin):
    __tablename__ = "profesionales"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    specialty: Mapped[str] = mapped_column(String(100))  # Especialidad
    license_number: Mapped[Optional[str]] = mapped_column(String(50))  # Matrícula
    experience_years: Mapped[Optional[int]] = mapped_column(Integer)
    bio: Mapped[Optional[str]] = mapped_column(Text)
    consultation_fee: Mapped[Optional[Decimal]] = mapped_column(Decimal(10, 2))
    is_verified: Mapped[bool] = mapped_column(default=False)
    
    # Relaciones
    user: Mapped["User"] = relationship(back_populates="profesional")
```

## Fase 3: Schemas Pydantic

### 3.1 Schemas de Cliente
```python
class ClienteBase(BaseModel):
    dni: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    city: Optional[str] = None
    notes: Optional[str] = None

class ClienteCreate(ClienteBase):
    email: str
    password: str
    full_name: str
    phone: Optional[str] = None

class ClienteUpdate(ClienteBase):
    full_name: Optional[str] = None
    phone: Optional[str] = None

class ClienteResponse(ClienteBase):
    id: int
    email: str
    full_name: str
    phone: Optional[str]
    created_at: datetime
```

### 3.2 Schemas de Profesional
```python
class ProfesionalBase(BaseModel):
    specialty: str
    license_number: Optional[str] = None
    experience_years: Optional[int] = None
    bio: Optional[str] = None
    consultation_fee: Optional[Decimal] = None

class ProfesionalCreate(ProfesionalBase):
    email: str
    password: str
    full_name: str
    phone: Optional[str] = None

class ProfesionalUpdate(ProfesionalBase):
    full_name: Optional[str] = None
    phone: Optional[str] = None

class ProfesionalResponse(ProfesionalBase):
    id: int
    email: str
    full_name: str
    phone: Optional[str]
    is_verified: bool
    created_at: datetime
```

## Fase 4: Endpoints API (SCRUM-121)

### 4.1 Endpoints de Cliente
```
GET    /api/v1/clientes/me           # Obtener mi perfil
PUT    /api/v1/clientes/me           # Editar mi perfil
PATCH  /api/v1/clientes/me           # Actualización parcial
GET    /api/v1/clientes/{id}         # Obtener cliente (admin)
```

### 4.2 Endpoints de Profesional
```
GET    /api/v1/profesionales/me      # Obtener mi perfil
PUT    /api/v1/profesionales/me      # Editar mi perfil
PATCH  /api/v1/profesionales/me      # Actualización parcial
GET    /api/v1/profesionales/{id}    # Obtener profesional (admin)
```

### 4.3 Validaciones
- Email válido
- Contraseña mínima 8 caracteres
- Campos obligatorios según schema
- Validación de formatos (DNI, teléfono, fecha)

## Fase 5: Autenticación

### 5.1 JWT Token
- Generación de token al login
- Validación de token en endpoints protegidos
- Refresh token opcional

### 5.2 Dependencias
```python
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # Validar token y retornar usuario
    pass

async def get_current_cliente(current_user: User = Depends(get_current_user)) -> Cliente:
    # Validar que sea cliente
    pass

async def get_current_profesional(current_user: User = Depends(get_current_user)) -> Profesional:
    # Validar que sea profesional
    pass
```

## Fase 6: Docker Configuración

### 6.1 Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 6.2 docker-compose.yml
```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: appointa
      POSTGRES_PASSWORD: appointa123
      POSTGRES_DB: appointa
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://appointa:appointa123@db:5432/appointa
      SECRET_KEY: your-secret-key-here
    depends_on:
      - db
    volumes:
      - .:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

volumes:
  postgres_data:
```

## Fase 7: Script start.ps1

```powershell
# Script para levantar Appointa Backend

Write-Host "🚀 Levantando Appointa Backend..." -ForegroundColor Green

# Verificar Docker
Write-Host "📦 Verificando Docker..." -ForegroundColor Yellow
docker --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker no está instalado" -ForegroundColor Red
    exit 1
}

# Construir imágenes
Write-Host "🔨 Construyendo imágenes Docker..." -ForegroundColor Yellow
docker-compose build

# Levantar servicios
Write-Host "🌟 Levantando servicios..." -ForegroundColor Yellow
docker-compose up -d

# Esperar a que la DB esté lista
Write-Host "⏳ Esperando a la base de datos..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

# Ejecutar migrations
Write-Host "🔄 Ejecutando migrations..." -ForegroundColor Yellow
docker-compose exec api alembic upgrade head

# Mostrar logs
Write-Host "📊 Mostrando logs (Ctrl+C para salir)..." -ForegroundColor Green
docker-compose logs -f
```

## Cronograma de Implementación

### Día 1: Setup y Estructura
- [x] Crear estructura de directorios
- [x] Configurar dependencias (requirements.txt)
- [x] Configurar Docker y docker-compose
- [x] Crear script start.ps1
- [x] Configurar conexión a DB

### Día 2: Modelos y Schemas
- [x] Implementar modelos SQLAlchemy
- [x] Implementar schemas Pydantic
- [x] Configurar Alembic migrations
- [x] Crear primera migration

### Día 3: Autenticación
- [x] Implementar JWT
- [x] Implementar password hashing
- [x] Crear endpoints de auth (login, register)
- [x] Implementar dependencias de autenticación

### Día 4: SCRUM-121 - Endpoints
- [x] Implementar endpoints de Cliente (GET/PUT/PATCH /me)
- [x] Implementar endpoints de Profesional (GET/PUT/PATCH /me)
- [x] Implementar validaciones
- [x] Documentación automática (Swagger)

### Día 5: Testing y Deploy
- [x] Escribir tests unitarios
- [x] Probar endpoints con Postman/Swagger
- [x] Validar Docker localmente
- [x] Documentar deployment

## Criterios de Aceptación SCRUM-121

- [ ] El formulario permite editar datos simples del perfil
- [ ] No incluye manejo de imágenes
- [ ] Los datos se validan correctamente
- [ ] La API responde con códigos HTTP apropiados
- [ ] La documentación Swagger está disponible
- [ ] El backend levanta correctamente con start.ps1
- [ ] Los datos persisten en PostgreSQL

## Próximos Pasos

1. Crear estructura del proyecto
2. Implementar modelos y schemas
3. Configurar Docker
4. Implementar endpoints SCRUM-121
5. Testing y validación
