# Setup Workspace Script
# Este script crea enlaces (Junctions) desde .agent a las carpetas que los IDEs reconocen.

$sourceDir = ".agent"
$targets = @(".vscode", ".cursor", ".windsurf")

if (-not (Test-Path $sourceDir)) {
    Write-Host "Error: La carpeta fuente '$sourceDir' no existe." -ForegroundColor Red
    exit 1
}

foreach ($target in $targets) {
    if (Test-Path $target) {
        Write-Host "La carpeta '$target' ya existe. Omitiendo..." -ForegroundColor Yellow
    } else {
        Write-Host "Creando enlace para $target..." -ForegroundColor Cyan
        try {
            # Usamos Junction para máxima compatibilidad en Windows
            New-Item -ItemType Junction -Path $target -Target $sourceDir | Out-Null
            Write-Host "Exito: $target vinculado a $sourceDir" -ForegroundColor Green
        } catch {
            Write-Host "Error al crear el enlace para ${target}: $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}

Write-Host "`nConfiguracion completada. Ahora puedes usar el IDE de tu preferencia." -ForegroundColor White
