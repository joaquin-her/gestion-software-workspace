# Cronograma de Sprints (Fases + Paralelización Interna)

> **Velocidad Objetivo:** ~41 SP por Sprint
> **Estrategia:** Agrupación rígida por 5 Fases de Dependencia (para que nada se construya sin sus cimientos). Dentro de cada Fase, distribución Round-Robin para permitir trabajo en paralelo.

## Sprint 1
- **Cantidad de Tickets:** 13
- **Total Story Points:** 41

| ID | Clave | Fase | Módulo | Resumen | SP |
|---|---|---|---|---|---|
| 10000 | SCRUM-1 | Fase 1 | AUTH | [AUTH] [BASE] Registrarse con Email y contraseña | 2 |
| 10056 | SCRUM-57 | Fase 1 | USER | [USER] [BASE] Gestionar perfil personal: Editar datos (Nombre, Celular) | 3 |
| 10001 | SCRUM-2 | Fase 1 | PERFIL | [PERFIL] [BASE] Configurar perfil basico: Cargar nombre, especialidad, foto | 3 |
| 10020 | SCRUM-21 | Fase 1 | AGENDA | [AGENDA] [BASE] Definir estructura base: Establecer días laborables y franjas horarias | 3 |
| 10024 | SCRUM-25 | Fase 1 | SERVICIOS | [SERVICIOS] [BASE] Configurar servicios: Crear un servicio | 5 |
| 10003 | SCRUM-4 | Fase 1 | AUTH | [AUTH] [BASE] Validar Email | 3 |
| 10057 | SCRUM-58 | Fase 1 | USER | [USER] [BASE] Cambiar contraseña | 2 |
| 10010 | SCRUM-11 | Fase 1 | PERFIL | [PERFIL] [BASE] Configurar Perfil Básico: Cargar nombre, especialidad y foto | 3 |
| 10021 | SCRUM-22 | Fase 1 | AGENDA | [AGENDA] [BASE] Definir duración estándar del turno | 5 |
| 10025 | SCRUM-26 | Fase 1 | SERVICIOS | [SERVICIOS] [BASE] Configurar capacidad por turno | 5 |
| 10004 | SCRUM-5 | Fase 1 | AUTH | [AUTH] [BASE] Iniciar sesión / Recuperar contraseña | 2 |
| 10058 | SCRUM-59 | Fase 1 | USER | [USER] [BASE] Eliminar mi cuenta | 3 |
| 10011 | SCRUM-12 | Fase 1 | PERFIL | [PERFIL] [BASE] Definir modalidad (Presencial/Virtual) | 2 |

## Sprint 2
- **Cantidad de Tickets:** 11
- **Total Story Points:** 44

| ID | Clave | Fase | Módulo | Resumen | SP |
|---|---|---|---|---|---|
| 10022 | SCRUM-23 | Fase 1 | AGENDA | [AGENDA] [BASE] Configurar descansos entre turnos | 5 |
| 10026 | SCRUM-27 | Fase 1 | SERVICIOS | [SERVICIOS] [BASE] Editar o eliminar servicios | 5 |
| 10005 | SCRUM-6 | Fase 1 | AUTH | [AUTH] [BASE] Cambiar contraseña / Eliminar | 5 |
| 10012 | SCRUM-13 | Fase 1 | PERFIL | [PERFIL] [BASE] Generar link público de reservas | 3 |
| 10023 | SCRUM-24 | Fase 1 | AGENDA | [AGENDA] [PREM] Sincronización con Google Calendar | 5 |
| 10027 | SCRUM-28 | Fase 1 | SERVICIOS | [SERVICIOS] [PREM] Habilitar cobro de seña por servicio | 3 |
| 10009 | SCRUM-10 | Fase 1 | AUTH | [AUTH] [BASE] Cambiar contraseña / Eliminar | 5 |
| 10013 | SCRUM-14 | Fase 1 | PERFIL | [PERFIL] [BASE] Agregar links a Redes Sociales | 2 |
| 10051 | SCRUM-52 | Fase 1 | AUTH | [AUTH] [BASE] Crear cuenta: Registrarse con Email y WhatsApp | 5 |
| 10014 | SCRUM-15 | Fase 1 | PERFIL | [PERFIL] [BASE] Previsualizar perfil público | 3 |
| 10052 | SCRUM-53 | Fase 1 | AUTH | [AUTH] [BASE] Validar cuenta (Email) | 3 |

## Sprint 3
- **Cantidad de Tickets:** 16
- **Total Story Points:** 44

| ID | Clave | Fase | Módulo | Resumen | SP |
|---|---|---|---|---|---|
| 10015 | SCRUM-16 | Fase 1 | PERFIL | [PERFIL] [BASE] Editar perfil | 3 |
| 10053 | SCRUM-54 | Fase 1 | AUTH | [AUTH] [BASE] Acceder a la cuenta: Iniciar sesión con Email y Pass | 3 |
| 10016 | SCRUM-17 | Fase 1 | PERFIL | [PERFIL] [PREM] Personalizar preguntas del formulario al cliente | 3 |
| 10054 | SCRUM-55 | Fase 1 | AUTH | [AUTH] [BASE] Recuperar contraseña | 3 |
| 10055 | SCRUM-56 | Fase 1 | AUTH | [AUTH] [BASE] Login rápido con Google (OAuth) | 3 |
| 10066 | SCRUM-67 | Fase 2 | BOOKING | [BOOKING] [BASE] Explorar perfil: Aterrizar en URL pública del profesional | 2 |
| 10059 | SCRUM-60 | Fase 2 | DASH | [DASH] [BASE] Dashboard de Inicio: Ver resumen de próximos turnos agendados | 3 |
| 10067 | SCRUM-68 | Fase 2 | BOOKING | [BOOKING] [BASE] Ver descripción y modalidad | 2 |
| 10060 | SCRUM-61 | Fase 2 | DASH | [DASH] [BASE] Ver notificaciones/alertas importantes | 3 |
| 10068 | SCRUM-69 | Fase 2 | BOOKING | [BOOKING] [BASE] Ver lista de servicios y duraciones | 2 |
| 10061 | SCRUM-62 | Fase 2 | DASH | [DASH] [BASE] Mis Profesionales: Ver lista de profesionales previos | 5 |
| 10069 | SCRUM-70 | Fase 2 | BOOKING | [BOOKING] [BASE] Filtrar servicios por categoría | 2 |
| 10062 | SCRUM-63 | Fase 2 | DASH | [DASH] [BASE] Botón de "Volver a reservar" | 3 |
| 10070 | SCRUM-71 | Fase 2 | BOOKING | [BOOKING] [BASE] Elegir disponibilidad: Navegar por el calendario | 2 |
| 10063 | SCRUM-64 | Fase 2 | DASH | [DASH] [BASE] Guardar un profesional en "Favoritos" | 3 |
| 10071 | SCRUM-72 | Fase 2 | BOOKING | [BOOKING] [BASE] Ver horarios disponibles en real-time | 2 |

## Sprint 4
- **Cantidad de Tickets:** 19
- **Total Story Points:** 44

| ID | Clave | Fase | Módulo | Resumen | SP |
|---|---|---|---|---|---|
| 10072 | SCRUM-73 | Fase 2 | BOOKING | [BOOKING] [BASE] Seleccionar franja horaria | 2 |
| 10073 | SCRUM-74 | Fase 2 | BOOKING | [BOOKING] [BASE] Seleccionar el servicio deseado | 2 |
| 10074 | SCRUM-75 | Fase 2 | BOOKING | [BOOKING] [BASE] Confirmar y abonar: Completar datos básicos / Comentarios | 2 |
| 10075 | SCRUM-76 | Fase 2 | BOOKING | [BOOKING] [BASE] Confirmar reserva (Pantalla de éxito) | 2 |
| 10076 | SCRUM-77 | Fase 2 | BOOKING | [BOOKING] [BASE] Completar formulario personalizado | 2 |
| 10028 | SCRUM-29 | Fase 3 | TURNOS | [TURNOS] [BASE] Manejar excepciones: Pausar agenda temporalmente | 2 |
| 10081 | SCRUM-82 | Fase 3 | GESTION | [GESTION] [BASE] Modificar reserva: Cancelar turno reservado | 2 |
| 10077 | SCRUM-78 | Fase 3 | MIS-TURNOS | [MIS-TURNOS] [BASE] Revisar mis turnos: Ver panel de "Mis Turnos" | 2 |
| 10064 | SCRUM-65 | Fase 3 | PAGOS | [PAGOS] [BASE] Historial de Pagos: Ver historial de señas pagadas | 2 |
| 10037 | SCRUM-38 | Fase 3 | CLIENTE | [CLIENTE] [BASE] Seguimiento: Recibir notificaciones sobre cierto cliente | 3 |
| 10084 | SCRUM-85 | Fase 3 | NOTIF | [NOTIF] [BASE] Recibir confirmación de reserva por Email | 2 |
| 10029 | SCRUM-30 | Fase 3 | TURNOS | [TURNOS] [BASE] Bloquear fechas (Vacaciones/Feriados) | 3 |
| 10082 | SCRUM-83 | Fase 3 | GESTION | [GESTION] [BASE] Indicar motivo de cancelación | 2 |
| 10078 | SCRUM-79 | Fase 3 | MIS-TURNOS | [MIS-TURNOS] [BASE] Ver historial de turnos pasados | 2 |
| 10065 | SCRUM-66 | Fase 3 | PAGOS | [PAGOS] [BASE] Descargar comprobante de turno/seña | 3 |
| 10038 | SCRUM-39 | Fase 3 | CLIENTE | [CLIENTE] [BASE] Botón de contacto rápido por WhatsApp | 5 |
| 10085 | SCRUM-86 | Fase 3 | NOTIF | [NOTIF] [BASE] Recibir aviso si el profesional cancela | 2 |
| 10030 | SCRUM-31 | Fase 3 | TURNOS | [TURNOS] [BASE] Revisar agenda: Ver panel de turnos (Dashboard) | 2 |
| 10083 | SCRUM-84 | Fase 3 | GESTION | [GESTION] [BASE] Reprogramar turno (Mover fecha) | 2 |

## Sprint 5
- **Cantidad de Tickets:** 15
- **Total Story Points:** 44

| ID | Clave | Fase | Módulo | Resumen | SP |
|---|---|---|---|---|---|
| 10079 | SCRUM-80 | Fase 3 | MIS-TURNOS | [MIS-TURNOS] [BASE] Ver detalle (Dirección, link de Zoom, etc.) | 2 |
| 10039 | SCRUM-40 | Fase 3 | CLIENTE | [CLIENTE] [BASE] Ver historial del cliente | 5 |
| 10086 | SCRUM-87 | Fase 3 | NOTIF | [NOTIF] [PREM] Recibir recordatorio por WhatsApp (24hs) | 2 |
| 10031 | SCRUM-32 | Fase 3 | TURNOS | [TURNOS] [BASE] Ver detalle del turno | 3 |
| 10080 | SCRUM-81 | Fase 3 | MIS-TURNOS | [MIS-TURNOS] [BASE] Ver estado de pagos / señas | 2 |
| 10040 | SCRUM-41 | Fase 3 | CLIENTE | [CLIENTE] [PREM] Añadir notas internas privadas | 5 |
| 10032 | SCRUM-33 | Fase 3 | TURNOS | [TURNOS] [PREM] Exportar turnos del mes a Excel/CSV | 3 |
| 10033 | SCRUM-34 | Fase 3 | TURNOS | [TURNOS] [BASE] Administrar reservas: Cancelar el turno de un cliente | 3 |
| 10034 | SCRUM-35 | Fase 3 | TURNOS | [TURNOS] [BASE] Marcar asistencia (Asistió / No asistió) | 3 |
| 10035 | SCRUM-36 | Fase 3 | TURNOS | [TURNOS] [BASE] Reprogramar turno desde el panel | 3 |
| 10036 | SCRUM-37 | Fase 3 | TURNOS | [TURNOS] [PREM] Gestionar reembolsos de seña | 3 |
| 10002 | SCRUM-3 | Fase 4 | SUBS | [SUBS] [BASE] Administrar suscripcion: Ver estado del plan actual | 3 |
| 10087 | SCRUM-88 | Fase 4 | ADMIN | [ADMIN] [PREM] Configurar perfil del local: Cargar nombre, logo y dirección | 2 |
| 10090 | SCRUM-91 | Fase 4 | STAFF | [STAFF] [PREM] Administrar Staff: Invitar profesionales por email | 2 |
| 10102 | SCRUM-103 | Fase 4 | CRM | [CRM] [PREM] Base de clientes compartida: Ver base de datos del local | 3 |

## Sprint 6
- **Cantidad de Tickets:** 16
- **Total Story Points:** 42

| ID | Clave | Fase | Módulo | Resumen | SP |
|---|---|---|---|---|---|
| 10017 | SCRUM-18 | Fase 4 | SUBS | [SUBS] [BASE] Administrar Suscripción: Ver estado del plan actual | 3 |
| 10088 | SCRUM-89 | Fase 4 | ADMIN | [ADMIN] [PREM] Generar link público general del negocio | 0 |
| 10091 | SCRUM-92 | Fase 4 | STAFF | [STAFF] [PREM] Crear/Editar perfil del empleado | 2 |
| 10103 | SCRUM-104 | Fase 4 | CRM | [CRM] [PREM] Ver historial global del cliente en el local | 2 |
| 10018 | SCRUM-19 | Fase 4 | SUBS | [SUBS] [PREM] Hacer Upgrade a Premium | 3 |
| 10089 | SCRUM-90 | Fase 4 | ADMIN | [ADMIN] [PREM] Configurar horarios de apertura del local | 2 |
| 10092 | SCRUM-93 | Fase 4 | STAFF | [STAFF] [PREM] Dar de baja/Suspender a un empleado | 2 |
| 10104 | SCRUM-105 | Fase 4 | CRM | [CRM] [PREM] Añadir notas internas al perfil del cliente | 2 |
| 10019 | SCRUM-20 | Fase 4 | SUBS | [SUBS] [BASE] Cancelar Suscripción Premium | 3 |
| 10093 | SCRUM-94 | Fase 4 | STAFF | [STAFF] [PREM] Asignar servicios y horarios: Definir qué servicios da cada empleado | 2 |
| 10094 | SCRUM-95 | Fase 4 | STAFF | [STAFF] [PREM] Configurar días/horarios de cada empleado | 3 |
| 10095 | SCRUM-96 | Fase 4 | STAFF | [STAFF] [PREM] Asignar roles (Admin general vs. Empleado) | 3 |
| 10096 | SCRUM-97 | Fase 5 | GLOBAL | [GLOBAL] [PREM] Monitorear agenda: Ver calendario unificado (Todos los empleados) | 2 |
| 10105 | SCRUM-106 | Fase 5 | METRICAS | [METRICAS] [PREM] Analítica: Ver total de turnos (Atendidos vs Cancelados) | 5 |
| 10110 | SCRUM-111 | Fase 5 | DATA | [DATA] [PREM] Exportación: Exportar base de datos de clientes | 5 |
| 10097 | SCRUM-98 | Fase 5 | GLOBAL | [GLOBAL] [PREM] Filtrar vista por empleado específico | 3 |

## Sprint 7
- **Cantidad de Tickets:** 9
- **Total Story Points:** 32

| ID | Clave | Fase | Módulo | Resumen | SP |
|---|---|---|---|---|---|
| 10106 | SCRUM-107 | Fase 5 | METRICAS | [METRICAS] [PREM] Ver ingresos estimados del mes | 5 |
| 10111 | SCRUM-112 | Fase 5 | DATA | [DATA] [PREM] Exportar liquidación mensual a Excel/CSV | 5 |
| 10098 | SCRUM-99 | Fase 5 | GLOBAL | [GLOBAL] [PREM] Filtrar vista por servicio | 2 |
| 10107 | SCRUM-108 | Fase 5 | METRICAS | [METRICAS] [PREM] Ver servicios más populares | 3 |
| 10099 | SCRUM-100 | Fase 5 | GLOBAL | [GLOBAL] [PREM] Gestión administrativa: Reasignar turno de un empleado a otro | 2 |
| 10108 | SCRUM-109 | Fase 5 | METRICAS | [METRICAS] [PREM] Rendimiento: Ver cantidad de turnos por profesional | 5 |
| 10100 | SCRUM-101 | Fase 5 | GLOBAL | [GLOBAL] [PREM] Bloquear agenda de empleado | 3 |
| 10109 | SCRUM-110 | Fase 5 | METRICAS | [METRICAS] [PREM] Ver ingresos generados por cada empleado | 5 |
| 10101 | SCRUM-102 | Fase 5 | GLOBAL | [GLOBAL] [PREM] Crear turno manual | 2 |

## Resumen Total
- **Total de Tickets:** 99
- **Total de Story Points:** 291
