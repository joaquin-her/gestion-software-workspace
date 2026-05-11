# Script para levantar Appointa Backend

$BACKEND_DIR = "appointa-backend"

Write-Host "Levantando Appointa Backend..." -ForegroundColor Green

# Verificar Docker
Write-Host "Verificando Docker..." -ForegroundColor Yellow
docker --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker no esta instalado" -ForegroundColor Red
    exit 1
}

# Verificar docker-compose
Write-Host "Verificando docker-compose..." -ForegroundColor Yellow
docker-compose --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "docker-compose no esta instalado" -ForegroundColor Red
    exit 1
}

# Cambiar al directorio del backend
Write-Host "Cambiando al directorio $BACKEND_DIR..." -ForegroundColor Yellow
Set-Location $BACKEND_DIR

# Crear archivo .env si no existe
if (-not (Test-Path ".env")) {
    Write-Host "Creando archivo .env desde .env.example..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
}

# Construir imagenes
Write-Host "Construyendo imagenes Docker..." -ForegroundColor Yellow
docker-compose build

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Docker no esta corriendo actualmente" -ForegroundColor Red
    Write-Host "Por favor inicia Docker Desktop y vuelve a ejecutar este script" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Presiona Enter para cerrar..." -ForegroundColor Cyan
    Read-Host
    exit 1
}

# Levantar servicios
Write-Host "Levantando servicios..." -ForegroundColor Yellow
docker-compose up -d

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error al levantar servicios" -ForegroundColor Red
    exit 1
}

# Esperar a que la DB este lista
Write-Host "Esperando a la base de datos..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Crear tablas
Write-Host "Creando tablas en la base de datos..." -ForegroundColor Yellow
docker-compose exec api python -c "from app.database import engine, Base; Base.metadata.create_all(bind=engine); print('Tablas creadas exitosamente')"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Advertencia: No se pudieron crear las tablas automaticamente" -ForegroundColor Yellow
    Write-Host "Puedes crearlas manualmente ejecutando:" -ForegroundColor Yellow
    Write-Host "docker-compose exec api python -c 'from app.database import engine, Base; Base.metadata.create_all(bind=engine)'" -ForegroundColor Yellow
}

# Mostrar informacion
Write-Host "Appointa Backend esta corriendo!" -ForegroundColor Green
Write-Host "API Documentation: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host "API Documentation (ReDoc): http://localhost:8000/redoc" -ForegroundColor Cyan
Write-Host "Health Check: http://localhost:8000/health" -ForegroundColor Cyan
Write-Host ""
Write-Host "Comandos utiles:" -ForegroundColor Yellow
Write-Host "Ver logs: cd $BACKEND_DIR; docker-compose logs -f" -ForegroundColor White
Write-Host "Detener: cd $BACKEND_DIR; docker-compose down" -ForegroundColor White
Write-Host "Reiniciar: cd $BACKEND_DIR; docker-compose restart" -ForegroundColor White
Write-Host ""
Write-Host "Mostrando logs (Ctrl+C para salir de los logs, los servicios seguiran corriendo)..." -ForegroundColor Green
docker-compose logs -f
