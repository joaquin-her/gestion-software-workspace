# Agent Context: Proyecto Appointa

Este documento define el contexto, la estructura de datos y los protocolos de operación para agentes de IA que interactúen con los artefactos de este repositorio, independientemente de su proveedor o interfaz (Claude, Windsurf, VS Code, etc.).

## 1. Contexto del Proyecto
**Producto:** Appointa
**Descripción:** Plataforma SaaS de gestión de turnos online para profesionales independientes y pequeñas clínicas.
**Modelo:** Freemium (Planes Free y Premium).
**Pila Tecnológica:** Web, integraciones con WhatsApp y Google Calendar.

## 2. Mapa de Artefactos (Knowledge Base)

### Fuentes de Información (Local)
- **Excel Maestro:** `artefactos/Artefactos_original.xlsx` (Contiene los datos técnicos y de cálculo).
- **Consolidado Markdown:** `artefactos/ARTEFACTOS_CONSOLIDADO.md` (Referencia rápida para lectura de contexto/RAG).

### Repositorio Cloud (Confluence)
- **Espacio:** `Appointa (A)`
- **Página Raíz:** `Artefactos del Proyecto (Excel)` (ID: `4128769`)
- **Páginas Hijas:** `Product Vision`, `Personas`, `Features`, `User Story Map (USM)`, `WBS`, `Backlog User Stories`, `Planilla de Costos`.

## 3. Protocolos para el Asistente de IA

### Al recibir un pedido de cambio:
1. **Verificación de Contexto:** Consultar `ARTEFACTOS_CONSOLIDADO.md` antes de proponer ediciones transversales.
2. **Sincronización:** Si se modifica el Excel local, proponer la actualización de la página correspondiente en Confluence.
3. **Mantenimiento de Estándares:**
   - Respetar el formato de tablas Markdown.
   - Preservar nombres de columnas y emojis de prioridad (⭐).

## 4. Estructura de Datos para Procesamiento
Las tablas en los documentos Markdown siguen este esquema de limpieza:
- Saltos de línea en celdas reemplazados por `<br>`.
- Pipes (`|`) escapados con `\|`.
- Valores nulos tratados como strings vacíos.

---
*Este documento es auto-mantenido. Si se agrega un nuevo artefacto, actualice la sección 2.*