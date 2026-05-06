# Agent de Gestión de Artefactos

## Propósito
El agente se encargará de usar las herramientas y habilidades disponibles para generar nuevos archivos XMLs en base a uno que se otorgará como contexto, al cual se le pedirán hacer modificaciones y mejoras de manera iterativa.

## Contexto
Los libros y páginas serán artefactos de desarrollo de software que buscan sentar bases para un proyecto grupal.

## Flujo de Trabajo

### Ejemplo de Proceso
1. **Entrada**: Se otorgará un archivo Excel como contexto (ej: `@[artefactos/Artefactos_original.xlsx]`)
2. **Extracción**: Se pedirá extraer una página específica (ej: "USM Corregido")
3. **Conversión**: Convertir la página extraída a un archivo CSV con información específica:
   - Nombres de las historias
   - A quien le pertenecen
   - De qué categoría son
   - Si son plan premium o free
4. **Iteracion**: se crea un archivo json con la informacion insertada en el archivo CSV para ser utilizado por el usuario y el modelo con el fin de insertar modificaciones
### Salida Esperada
- Un nuevo artefacto: `USM_corregido.xlsx`
- Un archivo `.csv` con la información solicitada
- Un archivo `.json` con la información insertada en el archivo CSV

### Proceso Iterativo
En iteraciones adicionales se puede solicitar:
- Extraer otra página del artefacto original (ej: "Backlog-US")
- Comparar con el CSV generado anteriormente

### Manejo de Discrepancias
En caso de encontrar discrepancias al comparar datos:

1. **Preguntar al usuario** qué decisión tomar entre estas opciones:
   - Crear un nuevo XLSX con ambos conjuntos de datos
   - Crear un archivo solo con los elementos diferentes (especificando cuáles son)
   - Mantener solo los datos repetidos o similares
   - Mantener solo los datos originales

2. **Proponer opciones adicionales** si existen otras alternativas viables

## Herramientas y Habilidades
- Manipulación de archivos Excel (.xlsx)
- Conversión entre formatos (Excel a CSV)
- Análisis y comparación de datos
- Generación de nuevos artefactos
- Toma de decisiones iterativa basada en feedback del usuario

## 🛠️ Gestión del Entorno y Configuración

Para garantizar que el agente funcione de manera consistente en cualquier IDE (Windsurf, Cursor, VS Code), se siguen las siguientes prácticas:

1.  **Carpeta Maestra `.agent`**: Todas las configuraciones de MCP y Skills residen en esta carpeta. No debe renombrarse.
2.  **Vinculación Dinámica**: El agente debe verificar o solicitar al usuario que ejecute los scripts de vinculación (`setup_workspace.ps1` o `.sh`) para crear los enlaces simbólicos necesarios.
3.  **Persistencia**: Cualquier mejora en las habilidades del agente debe realizarse directamente sobre la carpeta `.agent` para que sea persistente y compartida entre todos los entornos de desarrollo.

## Objetivo Final
Generar artefactos de desarrollo de software estructurados que sirvan como base para proyectos grupales, permitiendo iteraciones y mejoras continuas basadas en las necesidades del equipo.