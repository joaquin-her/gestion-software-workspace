# Gestión Repository

Este repositorio contiene herramientas y artefactos para la gestión de proyectos, integración con Jira y análisis de riesgos.

## 🚀 Instalación y Configuración

### Clonado del Repositorio

```bash
git clone <repository-url>
cd gestion
```

### ⚠️ **Paso Crítico - Renombrar Carpeta de Configuración**

**IMPORTANTE**: Después de clonar el repositorio, debe renombrar la carpeta `.windsurf` según el IDE/agent workspace que esté utilizando:

```bash
# Para VS Code con Windsurf
mv .windsurf .vscode

# Para Cursor IDE
mv .windsurf .cursor

# Para otros IDEs/workspaces, renombrar según corresponda
mv .windsurf .<nombre-del-ide>
```

Esta carpeta contiene configuraciones específicas del workspace y **debe ser renombrada** para que las herramientas funcionen correctamente en tu entorno.

### Configuración del Entorno

1. **Para integración con Jira**:
   ```bash
   chmod +x setup_jira_env.sh
   ./setup_jira_env.sh
   ```

2. **Instalar dependencias de Python**:
   ```bash
   pip install -r requirements.txt  # si existe
   # o instalar paquetes necesarios manualmente
   pip install pandas openpyxl requests atlassian-python-api
   ```

## 📁 Estructura del Repositorio

```
gestion/
├── artefactos/                    # Documentos y plantillas de Excel
│   ├── Template Costos.xlsx        # Plantilla de costos (Fixed Price)
│   ├── Artefactos_original.xlsx    # Datos originales del proyecto
│   └── Costos_Corregidos.xlsx    # Costos corregidos (generado)
├── scripts/                      # Scripts de automatización
│   ├── bulk_update_jira.py       # Actualización masiva de issues Jira
│   ├── update_jira_stories.py     # Actualización individual de stories
│   └── test_single_update.py    # Pruebas de actualización
├── data/                        # Datos y configuraciones
│   ├── prepared_update.json       # Datos preparados para actualización
│   └── all_jira_updates.json     # Historial de actualizaciones
├── docs/                        # Documentación
│   └── Instrucciones_Analisis_de_Riesgos.md
├── .windsurf/                   # Configuración del workspace (RENOMBRAR)
└── README.md                     # Este archivo
```

## 🛠️ Herramientas Disponibles

### 1. Gestión de Costos
- **Template Costos.xlsx**: Plantilla para cálculo de costos con fórmulas predefinidas
- **Artefactos_original.xlsx**: Datos originales del proyecto
- **Costos_Corregidos.xlsx**: Versión corregida combinando datos originales con fórmulas de la plantilla

### 2. Integración con Jira
- **bulk_update_jira.py**: Actualización masiva de issues en Jira
- **update_jira_stories.py**: Actualización individual de stories
- **setup_jira_env.sh**: Configuración del entorno Jira

### 3. Análisis de Riesgos
- **Matriz_de_Riesgos_Appointa.xlsx**: Matriz de riesgos del proyecto
- **Instrucciones_Analisis_de_Riesgos.md**: Guía para análisis de riesgos

## 📋 Uso

### Actualización de Issues en Jira

1. **Preparar datos**:
   ```bash
   python update_jira_stories.py
   ```

2. **Actualización masiva**:
   ```bash
   python bulk_update_jira.py
   ```

3. **Probar actualización**:
   ```bash
   python test_single_update.py
   ```

### Análisis de Costos

1. Abrir `artefactos/Template Costos.xlsx` para ver la estructura de fórmulas
2. Comparar con `artefactos/Artefactos_original.xlsx` 
3. Utilizar `artefactos/Costos_Corregidos.xlsx` como versión final

### Matriz de Riesgos

1. Revisar `Matriz_de_Riesgos_Appointa.xlsx`
2. Seguir instrucciones en `Instrucciones_Analisis_de_Riesgos.md`
3. Actualizar según evolución del proyecto

## 🔧 Fórmulas Útiles de Plantilla de Costos

La plantilla incluye las siguientes fórmulas clave:

### Cálculo de Costos por Período
```excel
=HorasColumna * RateColumna
=Ejemplo: =C3*$B3
```

### Totales Individuales
```excel
=SUM(C3:E3:G3:I3:K3:M3)  # Total horas
=SUM(D3:F3:H3:J3:L3:N3)  # Total costos
```

### Subtotales por Período
```excel
=SUM(C3:C8)  # Total horas período 1
=SUM(D3:D8)  # Total costos período 1
```

## 📝 Notas Importantes

- El repositorio está configurado para trabajar con múltiples IDEs mediante el renombramiento de la carpeta `.windsurf`
- Los scripts de Python requieren configuración previa de credenciales de Jira
- Los archivos de Excel contienen fórmulas dinámicas que se recalculan automáticamente
- Mantener actualizada la matriz de riesgos durante todo el ciclo del proyecto

## 🤝 Contribución

1. Fork del repositorio
2. Crear rama de feature: `git checkout -b nueva-funcionalidad`
3. Commit de cambios: `git commit -am 'Agregar nueva funcionalidad'`
4. Push a la rama: `git push origin nueva-funcionalidad`
5. Crear Pull Request

## 📄 Licencia

Este proyecto es para uso interno del equipo de gestión.

---

**⚠️ Recordatorio**: No olvide renombrar la carpeta `.windsurf` según su IDE antes de comenzar a trabajar.
