---
name: jira-backlog-importer
description: Automatiza el proceso de extracción de historias de usuario desde un archivo Excel (Backlog-US.xlsx), su desglose asistido por IA en tareas técnicas, el empaquetado en un formato JSON compatible con Jira y finalmente la importación a Jira mediante el MCP Atlassian-Rovo.
---

# Jira Backlog Importer

Esta skill define el pipeline completo para llevar un Backlog en formato Excel a tickets estructurados (Story + Sub-tasks) directamente en Jira. 

Aprovecha scripts programáticos para la extracción y formateo de datos, y delega en el Agente (tú) la capacidad de razonar y desglosar historias en tareas.

## Flujo de Trabajo (Pipeline)

El proceso consta de 4 pasos principales. Como Agente, debes guiar al usuario o ejecutar estos pasos secuencialmente:

### Paso 1: Extracción del Backlog (Automatizado)
Primero, debemos sacar las Historias de Usuario del archivo Excel `.xlsx` y transformarlas en un archivo `.json` manejable.
- **Entrada:** `artefactos/backlog/Backlog-US.xlsx` (Hoja "Backlog-us" o similar).
- **Acción:** Ejecuta el paso 1 del pipeline (`--pre-ai`) usando `run_command`:
  ```bash
  python .agent/skills/jira-backlog-importer/scripts/pipeline.py --pre-ai
  ```
- **Salida esperada:** Este script leerá el Excel original, lo reformateará y generará directamente el archivo `data/backlog.json` listo para que lo leas.

### Paso 2: Desglose de Tareas Asistido por IA (Interacción y Pensamiento)
Aquí es donde entra tu inteligencia. Los tickets de Jira necesitan desglosarse en subtareas técnicas.
- **Entrada:** Lee el archivo `data/backlog.json` generado en el paso anterior.
- **Acción:** Analiza cada historia de usuario (su título, descripción y criterios de aceptación). Para cada una, debes generar mentalmente 2 a 3 tareas técnicas (por ejemplo: "Frontend: Crear UI", "Backend: Crear endpoint", "Base de Datos: Modelo y migraciones").
- **Salida esperada:** Crea y escribe el archivo `data/tareas.json` (usando la herramienta `write_to_file`) con la siguiente estructura:
  ```json
  [
    {
      "Historia": "Nombre de la historia",
      "Tareas": [
        { "Titulo": "Crear UI de login", "Tipo": "Frontend" },
        { "Titulo": "Endpoint POST /login", "Tipo": "Backend" }
      ]
    }
  ]
  ```
*Nota: Si son muchas historias, puedes dividir el trabajo o avisarle al usuario que lo estás generando.*

### Paso 3: Empaquetado a Formato Jira (Automatizado)
Para poder subir esto a Jira (o generar un CSV compatible), necesitamos una estructura plana que siga los requerimientos de Jira (IssueType, Summary, Description, ParentId, etc.).
- **Entrada:** `data/backlog.json` y `data/tareas.json`.
- **Acción:** Ejecuta el paso 3 del pipeline (`--post-ai`) usando `run_command`:
  ```bash
  python .agent/skills/jira-backlog-importer/scripts/pipeline.py --post-ai
  ```
- **Salida esperada:** Se generará el archivo `data/jira_tickets.json` con todos los tickets y subtareas vinculadas.

### Paso 4: Subida a Jira mediante MCP (Interacción de IA)
Finalmente, los tickets estructurados deben subirse al proyecto de Jira correspondiente.
- **Entrada:** Lee el archivo `data/jira_tickets.json`.
- **Acción:** Solicita al usuario confirmación para empezar a subir los tickets.
- **Uso de herramientas:** Utiliza las herramientas de `Atlassian-Rovo-MCP` (como `mcp_Atlassian-Rovo-MCP_getVisibleJiraProjects` para identificar el proyecto y `mcp_Atlassian-Rovo-MCP_createJiraIssue` para crear los tickets).
- **Proceso iterativo:** 
  1. Crea un ticket tipo `Story` (Historia).
  2. Obtén el ID devuelto por Jira (ej. `SCRUM-123`).
  3. Crea sus respectivos `Subtask` utilizando el ID devuelto como `parent`.
  *(Ten cuidado con los campos, como las etiquetas que no pueden tener espacios, ej: "BaseDeDatos" en vez de "Base de Datos").*

## Buenas Prácticas
- Asegúrate de informar al usuario en qué parte del proceso te encuentras.
- Si un script falla (por ejemplo, si cambia la estructura del Excel), usa tus herramientas para arreglar el script temporalmente o pide ayuda al usuario.
- En el Paso 4, pregunta siempre antes de ejecutar subidas masivas a Jira, ofreciendo la opción de importar una historia de prueba primero para validar que los campos mapeen correctamente.
