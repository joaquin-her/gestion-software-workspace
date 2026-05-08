# Procedimiento de Consolidación de Backlog para Jira

Este documento detalla el proceso técnico y lógico seguido para transformar los artefactos de diseño (User Story Map) en un backlog de implementación de alta calidad listo para Jira.

## 1. Fuentes de Datos Originales
Se analizaron tres fuentes principales:
*   **`usm_backlog.json`**: Contenía la estructura completa de 116 historias (Título, Rol, Categoría) pero carecía de detalle técnico.
*   **`tareas_usm.json`**: Proporcionaba el desglose de tareas técnicas (Backend/Frontend) para las 116 historias, pero sin descripciones funcionales.
*   **`jira_tickets.json`**: Servía como estándar de calidad (incluyendo Criterios de Aceptación y descripciones detalladas), pero solo cubría un subconjunto de 21 historias.

## 2. Metodología de Consolidación
El objetivo fue aplicar la "Calidad Jira" al "Alcance Total" del USM.

### Paso 1: Enriquecimiento de Historias (AI-Hydration)
Para cada una de las 116 historias en `usm_backlog.json`:
1.  Se mapeó el **Rol** y la **Categoría** para definir el contexto de la historia.
2.  Se generó una **Descripción Funcional** siguiendo el formato estándar: *"Como [rol], quiero [acción], para [beneficio]"*.
3.  Se redactaron **Criterios de Aceptación (AC)** específicos y verificables, basándose en la complejidad de la historia y las mejores prácticas observadas en los ejemplos de referencia.

### Paso 2: Sincronización de Tareas Técnicas
Se vincularon las tareas definidas en `tareas_usm.json` con las historias enriquecidas utilizando el `Titulo` como llave de unión. Esto aseguró que cada ticket de Jira no solo fuera una descripción funcional, sino que tuviera sus correspondientes sub-tareas técnicas listas para ser asignadas.

### Paso 3: Formateo Óptimo para Jira
Se estructuró el archivo final siguiendo el esquema esperado por la API de Jira y el skill `jira-backlog-importer`:
*   **Historias (Parent):** Incluyen resumen, descripción extendida con AC, Story Points y etiquetas.
*   **Sub-tareas (Child):** Vinculadas vía `parentId`, con etiquetas heredadas y tipo de tarea (Frontend/Backend).

## 3. Resultados Obtenidos
*   **Archivo Final:** `data/jira_import_final.json`
*   **Total Historias:** 116
*   **Total Sub-tareas:** ~300
*   **Estado:** Listo para importación masiva.

## 4. Próximos Pasos
Para subir estos tickets a Jira, se debe ejecutar el pipeline de importación:
```powershell
python .agent/skills/jira-backlog-importer/scripts/pipeline.py --post-ai --usm
```

---
*Documento generado automáticamente por Antigravity - 2026-05-08*
