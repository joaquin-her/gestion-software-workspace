# Guía para el Análisis de Riesgos

## Estructura del Registro de Riesgos

El template de "Análisis de Riesgos" contiene 15 columnas diseñadas para identificar, evaluar y gestionar riesgos de manera sistemática:

### Columnas y su Propósito

1. **#**: Número identificador único del riesgo
2. **Descripción**: Descripción clara y concisa del riesgo
3. **Tipo**: Categoría del riesgo (Ej: Técnico, Financiero, Legal, Operativo, etc.)
4. **Causas**: Factores que podrían provocar que el riesgo se materialice
5. **Consecuencias**: Impacto negativo si el riesgo ocurre
6. **Probabilidad**: Likelihood de ocurrencia (Baja, Media, Alta)
7. **Impacto**: Severidad del impacto (Bajo, Medio, Alto, Crítico)
8. **Exposición**: Nivel de riesgo combinando probabilidad e impacto
9. **Plan de Respuesta**: Acciones preventivas para mitigar el riesgo
10. **Umbral**: Indicadores específicos que activan el plan de contingencia
11. **Plan de Contingencia**: Acciones correctivas si el riesgo se materializa
12. **Estado**: Estado actual del riesgo (Activo, Mitigado, Cerrado, etc.)
13. **Responsable**: Persona o equipo responsable de gestionar el riesgo
14. **Fecha Actualización**: Última fecha de revisión del riesgo
15. **Observaciones**: Notas adicionales o comentarios relevantes

## Cómo Llenar el Template

### Paso 1: Identificación del Riesgo
- **Descripción**: Sea específico y claro. Evite descripciones vagas.
  - ❌ Mal: "Problemas técnicos"
  - ✅ Buen: "Falla del servidor principal durante horas pico de operación"

- **Tipo**: Clasifique el riesgo en categorías estándar:
  - Técnico/Tecnológico
  - Financiero
  - Operativo
  - Legal/Regulatorio
  - Gestión del Proyecto
  - Recursos Humanos
  - Reputacional
  - Estratégico

### Paso 2: Análisis de Causas y Consecuencias
- **Causas**: Identifique las raíces del problema, no solo síntomas
- **Consecuencias**: Sea específico sobre el impacto en tiempo, dinero, calidad, etc.

### Paso 3: Evaluación del Riesgo
Use esta matriz para determinar Probabilidad e Impacto:

| Probabilidad | Criterio | Impacto | Criterio |
|-------------|----------|---------|----------|
| Baja | <10% de ocurrencia | Bajo | <5% afectación al proyecto |
| Media | 10-50% de ocurrencia | Medio | 5-20% afectación al proyecto |
| Alta | >50% de ocurrencia | Alto | 20-50% afectación al proyecto |
| - | - | Crítico | >50% afectación al proyecto |

**Exposición** se calcula combinando ambos factores:
- Baja × Bajo = Muy Baja
- Media × Medio = Media
- Alta × Crítico = Muy Alta

### Paso 4: Planes de Acción

**Plan de Respuesta (Preventivo)**:
- Acciones para reducir la probabilidad o impacto
- Debe ser proactivo y específico
- Incluya responsables y plazos

**Plan de Contingencia (Correctivo)**:
- Qué hacer si el riesgo ocurre
- Debe ser reactivo y de rápida ejecución
- Incluya recursos necesarios

**Umbral**:
- Indicadores específicos y medibles
- Ej: "Atraso mayor a 2 semanas"
- Ej: "Costo excedido en más del 15%"

### Paso 5: Gestión Continua

**Estados comunes**:
- **Activo**: Riesgo identificado y siendo monitoreado
- **Mitigado**: Acciones preventivas implementadas
- **Materializado**: El riesgo ha ocurrido
- **Cerrado**: Riesgo resuelto o ya no aplicable

**Responsable**: Designe una persona específica, no un departamento genérico

**Fecha Actualización**: Revise riesgos regularmente (mensual recomendado)

## Ejemplos Prácticos

El archivo `Ejemplo_Analisis_de_Riesgos.xlsx` contiene 4 ejemplos completos:

1. **Riesgo de Gestión**: Retraso por falta de recursos
2. **Riesgo Financiero**: Incremento de costos
3. **Riesgo Técnico**: Falla de plataforma
4. **Riesgo Legal**: Cambios regulatorios

## Mejores Prácticas

1. **Sea Específico**: Evite generalizaciones
2. **Enfoque en Acciones**: Cada riesgo debe tener planes concretos
3. **Asigne Responsables**: Sin responsable claro, no hay acción
4. **Revise Regularmente**: Los riesgos cambian con el tiempo
5. **Priorice**: No todos los riesgos requieren la misma atención
6. **Documente**: Mantenga registro de decisiones y cambios
7. **Comunique**: Comparta riesgos relevantes con stakeholders

## Proceso de Revisión Mensual

1. Actualizar estados de riesgos existentes
2. Identificar nuevos riesgos
3. Cerrar riesgos resueltos
4. Evaluar efectividad de planes de respuesta
5. Ajustar planes según sea necesario
6. Comunicar cambios al equipo

## Herramientas Adicionales

- **Matriz de Riesgos**: Visualización gráfica de probabilidad vs impacto
- **Dashboard de Seguimiento**: Indicadores clave de riesgos activos
- **Registro Histórico**: Lecciones aprendidas de riesgos materializados

---

**Nota**: Este template es una guía. Adapte las categorías y procesos según las necesidades específicas de su proyecto y organización.
