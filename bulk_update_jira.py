#!/usr/bin/env python3
"""
Bulk update script for all remaining Jira stories with proper story point estimations
"""

import json
import pandas as pd
import time

def read_backlog_data():
    """Read backlog data from Excel file"""
    backlog_file = '/home/joaquin-her/repos/gestion/Backlog.xlsx'
    return pd.read_excel(backlog_file, sheet_name='Backlog')

def get_all_jira_stories():
    """Get all Jira stories that need updating"""
    # All Jira stories from previous search
    jira_stories = [
        ('SCRUM-112', '[DATA] [PREM] Exportar liquidación mensual a Excel/CSV'),
        ('SCRUM-111', '[DATA] [PREM] Exportación: Exportar base de datos de clientes'),
        ('SCRUM-110', '[METRICAS] [PREM] Ver ingresos generados por cada empleado'),
        ('SCRUM-109', '[METRICAS] [PREM] Rendimiento: Ver cantidad de turnos por profesional'),
        ('SCRUM-108', '[METRICAS] [PREM] Ver servicios más populares'),
        ('SCRUM-107', '[METRICAS] [PREM] Analítica: Ver total de turnos (Atendidos vs Cancelados)'),
        ('SCRUM-106', '[METRICAS] [PREM] Analítica: Ver tasa de ocupación de turnos'),
        ('SCRUM-105', '[CRM] [PREM] Añadir notas internas al perfil del cliente'),
        ('SCRUM-104', '[CRM] [PREM] Ver historial global del cliente en el local'),
        ('SCRUM-103', '[CRM] [PREM] Base de clientes compartida: Ver base de datos del local'),
        ('SCRUM-102', '[CRM] [PREM] Base de clientes compartida: Editar datos del cliente'),
        ('SCRUM-101', '[CRM] [PREM] Base de clientes compartida: Eliminar cliente'),
        ('SCRUM-100', '[CRM] [PREM] Base de clientes compartida: Crear nuevo cliente'),
        ('SCRUM-99', '[CRM] [PREM] Base de clientes compartida: Ver perfil del cliente'),
        ('SCRUM-98', '[CRM] [PREM] Base de clientes compartida: Buscar cliente'),
        ('SCRUM-97', '[BOOKING] [BASE] Explorar perfil: Aterrizar en URL pública del profesional'),
        ('SCRUM-96', '[BOOKING] [BASE] Explorar perfil: Ver servicios del profesional'),
        ('SCRUM-95', '[BOOKING] [BASE] Explorar perfil: Ver disponibilidad horaria'),
        ('SCRUM-94', '[BOOKING] [BASE] Explorar perfil: Ver reseñas del profesional'),
        ('SCRUM-93', '[BOOKING] [BASE] Explorar perfil: Ver galería de fotos'),
        ('SCRUM-92', '[BOOKING] [BASE] Explorar perfil: Ver ubicación del profesional'),
        ('SCRUM-91', '[BOOKING] [BASE] Explorar perfil: Ver información de contacto'),
        ('SCRUM-90', '[BOOKING] [BASE] Explorar perfil: Ver biografía del profesional'),
        ('SCRUM-89', '[BOOKING] [BASE] Explorar perfil: Ver especialidades del profesional'),
        ('SCRUM-88', '[BOOKING] [BASE] Explorar perfil: Ver experiencia del profesional'),
        ('SCRUM-87', '[BOOKING] [BASE] Explorar perfil: Ver formación del profesional'),
        ('SCRUM-86', '[BOOKING] [BASE] Explorar perfil: Ver idiomas del profesional'),
        ('SCRUM-85', '[BOOKING] [BASE] Explorar perfil: Ver disponibilidad del profesional'),
        ('SCRUM-84', '[BOOKING] [BASE] Explorar perfil: Ver tarifas del profesional'),
        ('SCRUM-83', '[BOOKING] [BASE] Explorar perfil: Ver política de cancelación'),
        ('SCRUM-82', '[BOOKING] [BASE] Explorar perfil: Ver métodos de pago'),
        ('SCRUM-81', '[BOOKING] [BASE] Explorar perfil: Ver horarios de atención'),
        ('SCRUM-80', '[BOOKING] [BASE] Explorar perfil: Ver redes sociales'),
        ('SCRUM-79', '[BOOKING] [BASE] Explorar perfil: Ver certificaciones'),
        ('SCRUM-78', '[BOOKING] [BASE] Explorar perfil: Ver premios y reconocimientos'),
        ('SCRUM-77', '[BOOKING] [BASE] Explorar perfil: Ver publicaciones'),
        ('SCRUM-76', '[BOOKING] [BASE] Explorar perfil: Ver videos'),
        ('SCRUM-75', '[BOOKING] [BASE] Explorar perfil: Ver testimonios'),
        ('SCRUM-74', '[BOOKING] [BASE] Explorar perfil: Ver FAQs'),
        ('SCRUM-73', '[BOOKING] [BASE] Explorar perfil: Ver términos y condiciones'),
        ('SCRUM-72', '[BOOKING] [BASE] Explorar perfil: Ver política de privacidad'),
        ('SCRUM-71', '[BOOKING] [BASE] Explorar perfil: Ver sobre nosotros'),
        ('SCRUM-70', '[BOOKING] [BASE] Explorar perfil: Ver contacto de emergencia'),
        ('SCRUM-69', '[BOOKING] [BASE] Explorar perfil: Ver disponibilidad inmediata'),
        ('SCRUM-68', '[BOOKING] [BASE] Explorar perfil: Ver estado actual'),
        ('SCRUM-67', '[BOOKING] [BASE] Explorar perfil: Aterrizar en URL pública del profesional'),
        ('SCRUM-66', '[PAGOS] [BASE] Descargar comprobante de turno/seña'),
        ('SCRUM-65', '[PAGOS] [BASE] Historial de Pagos: Ver historial de señas pagadas'),
        ('SCRUM-64', '[DASH] [BASE] Guardar un profesional en "Favoritos"'),
        ('SCRUM-63', '[DASH] [BASE] Botón de "Volver a reservar"'),
        ('SCRUM-62', '[DASH] [BASE] Ver calendario con todos los turnos de todos los empleados'),
        ('SCRUM-61', '[DASH] [BASE] Reasignar turno de un empleado a otro'),
        ('SCRUM-60', '[DASH] [BASE] Ver base de datos de clientes del local'),
        ('SCRUM-59', '[DASH] [BASE] Añadir notas internas al perfil del cliente'),
        ('SCRUM-58', '[DASH] [BASE] Ver historial global del cliente en el local'),
        ('SCRUM-57', '[DASH] [BASE] Editar o eliminar servicios'),
        ('SCRUM-56', '[DASH] [BASE] Generar link público general del negocio'),
        ('SCRUM-55', '[DASH] [BASE] Crear/Editar perfil del empleado (Foto, rol)'),
        ('SCRUM-54', '[DASH] [BASE] Configurar días/horarios de cada empleado'),
        ('SCRUM-53', '[DASH] [BASE] Filtrar vista por empleado específico'),
        ('SCRUM-52', '[DASH] [BASE] Bloquear agenda de empleado'),
        ('SCRUM-51', '[DASH] [BASE] Dar de baja/Suspender a un empleado'),
        ('SCRUM-50', '[DASH] [BASE] Asignar roles (Admin general vs. Empleado)'),
        ('SCRUM-49', '[DASH] [BASE] Filtrar vista por servicio'),
        ('SCRUM-48', '[DASH] [BASE] Crear turno manual'),
        ('SCRUM-47', '[DASH] [BASE] Añadir notas internas al perfil del cliente'),
        ('SCRUM-46', '[DASH] [BASE] Ver historial del cliente'),
        ('SCRUM-45', '[DASH] [BASE] Ver servicios más populares'),
        ('SCRUM-44', '[DASH] [BASE] Ver ingresos estimados del mes'),
        ('SCRUM-43', '[DASH] [BASE] Ver ingresos generados por cada empleado'),
        ('SCRUM-42', '[DASH] [BASE] Ver cantidad de turnos por profesional'),
        ('SCRUM-41', '[DASH] [BASE] Ver total de turnos (Atendidos vs Cancelados)'),
        ('SCRUM-40', '[DASH] [BASE] Exportar turnos del mes a Excel/CSV'),
        ('SCRUM-39', '[DASH] [BASE] Exportar base de datos de clientes'),
        ('SCRUM-38', '[DASH] [BASE] Editar datos personales'),
        ('SCRUM-37', '[DASH] [BASE] Seleccionar servicio al reservar'),
        ('SCRUM-36', '[DASH] [BASE] Configurar perfil del local'),
        ('SCRUM-35', '[DASH] [BASE] Crear y editar perfil de empleado'),
        ('SCRUM-34', '[DASH] [BASE] Dar de baja/Suspender a un empleado'),
        ('SCRUM-33', '[DASH] [BASE] Asignar roles (Admin general vs. Empleado)'),
        ('SCRUM-32', '[DASH] [BASE] Filtrar vista por servicio'),
        ('SCRUM-31', '[DASH] [BASE] Crear turno manual'),
        ('SCRUM-30', '[DASH] [BASE] Añadir notas internas al perfil del cliente'),
        ('SCRUM-29', '[DASH] [BASE] Ver historial del cliente'),
        ('SCRUM-28', '[DASH] [BASE] Ver servicios más populares'),
        ('SCRUM-27', '[DASH] [BASE] Ver ingresos estimados del mes'),
        ('SCRUM-26', '[DASH] [BASE] Ver ingresos generados por cada empleado'),
        ('SCRUM-25', '[DASH] [BASE] Ver cantidad de turnos por profesional'),
        ('SCRUM-24', '[DASH] [BASE] Ver total de turnos (Atendidos vs Cancelados)'),
        ('SCRUM-23', '[DASH] [BASE] Exportar turnos del mes a Excel/CSV'),
        ('SCRUM-22', '[DASH] [BASE] Exportar base de datos de clientes'),
        ('SCRUM-21', '[DASH] [BASE] Editar datos personales'),
        ('SCRUM-20', '[DASH] [BASE] Seleccionar servicio al reservar'),
        ('SCRUM-19', '[DASH] [BASE] Configurar perfil del local'),
        ('SCRUM-18', '[DASH] [BASE] Crear y editar perfil de empleado'),
        ('SCRUM-17', '[DASH] [BASE] Dar de baja/Suspender a un empleado'),
        ('SCRUM-16', '[DASH] [BASE] Asignar roles (Admin general vs. Empleado)'),
        ('SCRUM-15', '[DASH] [BASE] Filtrar vista por servicio'),
        ('SCRUM-14', '[DASH] [BASE] Crear turno manual'),
        ('SCRUM-13', '[DASH] [BASE] Añadir notas internas al perfil del cliente'),
        ('SCRUM-12', '[DASH] [BASE] Ver historial del cliente'),
        ('SCRUM-11', '[DASH] [BASE] Ver servicios más populares'),
        ('SCRUM-10', '[DASH] [BASE] Ver ingresos estimados del mes'),
        ('SCRUM-9', '[DASH] [BASE] Ver ingresos generados por cada empleado'),
        ('SCRUM-8', '[DASH] [BASE] Ver cantidad de turnos por profesional'),
        ('SCRUM-7', '[DASH] [BASE] Ver total de turnos (Atendidos vs Cancelados)'),
        ('SCRUM-6', '[DASH] [BASE] Exportar turnos del mes a Excel/CSV'),
        ('SCRUM-5', '[AUTH] [BASE] Iniciar sesión / Recuperar contraseña'),
        ('SCRUM-4', '[AUTH] [BASE] Validar Email'),
        ('SCRUM-3', '[SUBS] [BASE] Administrar suscripcion: Ver estado del plan actual'),
        ('SCRUM-2', '[PERFIL] [BASE] Configurar perfil basico: Cargar nombre, especialidad, foto'),
        ('SCRUM-1', '[AUTH] [BASE] Registrarse con Email y contraseña')
    ]
    
    # Stories already updated (from previous sessions)
    already_updated = ['SCRUM-112', 'SCRUM-111', 'SCRUM-110', 'SCRUM-109', 'SCRUM-108', 
                      'SCRUM-105', 'SCRUM-104', 'SCRUM-103', 'SCRUM-102', 'SCRUM-101', 
                      'SCRUM-100', 'SCRUM-107', 'SCRUM-106', 'SCRUM-99', 'SCRUM-98', 
                      'SCRUM-97', 'SCRUM-96', 'SCRUM-95', 'SCRUM-94', 'SCRUM-93', 
                      'SCRUM-92', 'SCRUM-91', 'SCRUM-90', 'SCRUM-89']
    
    # Filter stories that need updating
    stories_to_update = []
    for key, summary in jira_stories:
        if key not in already_updated:
            stories_to_update.append((key, summary))
    
    return stories_to_update

def match_jira_to_backlog(jira_summary, df_backlog):
    """Match JIRA story to backlog entry"""
    jira_lower = jira_summary.lower()
    
    best_match = None
    best_score = 0
    
    for idx, row in df_backlog.iterrows():
        backlog_title = str(row['Historia de Usuario']).lower()
        score = 0
        
        # Enhanced keyword matching
        if 'exportar' in jira_lower and 'exportar' in backlog_title:
            score += 10
        if 'ingresos' in jira_lower and 'ingresos' in backlog_title:
            score += 10
        if 'turnos' in jira_lower and 'turnos' in backlog_title:
            score += 10
        if 'servicios' in jira_lower and 'servicios' in backlog_title:
            score += 10
        if 'notas' in jira_lower and 'notas' in backlog_title:
            score += 10
        if 'historial' in jira_lower and 'historial' in backlog_title:
            score += 10
        if 'perfil' in jira_lower and 'perfil' in backlog_title:
            score += 10
        if 'buscar' in jira_lower and ('buscar' in backlog_title or 'búsqueda' in backlog_title):
            score += 10
        if 'editar' in jira_lower and 'editar' in backlog_title:
            score += 10
        if 'eliminar' in jira_lower and ('eliminar' in backlog_title or 'borrar' in backlog_title):
            score += 10
        if 'crear' in jira_lower and 'crear' in backlog_title:
            score += 10
        if 'login' in jira_lower and ('autenticación' in backlog_title or 'sesión' in backlog_title):
            score += 10
        if 'validar' in jira_lower and 'validar' in backlog_title:
            score += 10
        if 'suscripción' in jira_lower and 'suscripción' in backlog_title:
            score += 10
        if 'configurar' in jira_lower and 'configurar' in backlog_title:
            score += 10
        if 'disponibilidad' in jira_lower and 'disponibilidad' in backlog_title:
            score += 10
        if 'reseñas' in jira_lower and ('reseña' in backlog_title or 'review' in backlog_title):
            score += 10
        if 'galería' in jira_lower and ('foto' in backlog_title or 'galería' in backlog_title):
            score += 10
        if 'ubicación' in jira_lower and ('ubicación' in backlog_title or 'dirección' in backlog_title):
            score += 10
        if 'contacto' in jira_lower and ('contacto' in backlog_title or 'email' in backlog_title):
            score += 10
        if 'biografía' in jira_lower and ('biografía' in backlog_title or 'acerca de' in backlog_title):
            score += 10
        if 'especialidades' in jira_lower and ('especialidad' in backlog_title or 'servicio' in backlog_title):
            score += 10
        if 'experiencia' in jira_lower and 'experiencia' in backlog_title:
            score += 10
        if 'formación' in jira_lower and ('formación' in backlog_title or 'educación' in backlog_title):
            score += 10
        if 'idiomas' in jira_lower and 'idioma' in backlog_title:
            score += 10
        if 'tarifas' in jira_lower and ('tarifa' in backlog_title or 'precio' in backlog_title):
            score += 10
        if 'cancelación' in jira_lower and 'cancelación' in backlog_title:
            score += 10
        if 'pago' in jira_lower and ('pago' in backlog_title or 'método' in backlog_title):
            score += 10
        if 'horarios' in jira_lower and 'horario' in backlog_title:
            score += 10
        if 'redes' in jira_lower and ('red' in backlog_title or 'social' in backlog_title):
            score += 10
        if 'certificaciones' in jira_lower and 'certificación' in backlog_title:
            score += 10
        if 'premios' in jira_lower and 'premio' in backlog_title:
            score += 10
        if 'publicaciones' in jira_lower and 'publicación' in backlog_title:
            score += 10
        if 'videos' in jira_lower and 'video' in backlog_title:
            score += 10
        if 'testimonios' in jira_lower and 'testimonio' in backlog_title:
            score += 10
        if 'faqs' in jira_lower and ('faq' in backlog_title or 'pregunta' in backlog_title):
            score += 10
        if 'términos' in jira_lower and 'término' in backlog_title:
            score += 10
        if 'privacidad' in jira_lower and 'privacidad' in backlog_title:
            score += 10
        if 'nosotros' in jira_lower and 'nosotros' in backlog_title:
            score += 10
        if 'emergencia' in jira_lower and 'emergencia' in backlog_title:
            score += 10
        if 'inmediata' in jira_lower and 'inmediata' in backlog_title:
            score += 10
        if 'estado' in jira_lower and 'estado' in backlog_title:
            score += 10
        if 'comprobante' in jira_lower and 'comprobante' in backlog_title:
            score += 10
        if 'seña' in jira_lower and 'seña' in backlog_title:
            score += 10
        if 'favoritos' in jira_lower and 'favorito' in backlog_title:
            score += 10
        if 'reservar' in jira_lower and 'reserva' in backlog_title:
            score += 10
        if 'calendario' in jira_lower and 'calendario' in backlog_title:
            score += 10
        if 'reasignar' in jira_lower and 'reasignar' in backlog_title:
            score += 10
        if 'bloquear' in jira_lower and 'bloquear' in backlog_title:
            score += 10
        if 'baja' in jira_lower and ('baja' in backlog_title or 'suspender' in backlog_title):
            score += 10
        if 'roles' in jira_lower and 'rol' in backlog_title:
            score += 10
        
        # Partial matching for lower scores
        if score == 0:
            for word in jira_lower.split():
                if len(word) > 4 and word in backlog_title:
                    score += 2
        
        if score > best_score:
            best_score = score
            best_match = row
    
    return best_match if best_score >= 5 else None

def create_description(backlog_match, jira_summary, estimation):
    """Create description for JIRA story"""
    if backlog_match is not None:
        backlog_title = str(backlog_match['Historia de Usuario'])
        criteria = str(backlog_match['Criterios de Aceptación'])
        est = estimation if pd.notna(backlog_match['Estimación']) else 3
    else:
        backlog_title = jira_summary
        criteria = '* La funcionalidad está disponible y operativa\\n* El sistema responde correctamente a las interacciones\\n* La interfaz es intuitiva y fácil de usar\\n* Se cumplen los requisitos del negocio'
        est = 3
    
    description = f"""h2. Descripción

{backlog_title}

h2. Criterios de Aceptación

{criteria}

h2. Estimación

{est} story points"""
    
    return description

def main():
    """Main function to bulk update JIRA stories"""
    print("=== JIRA BULK UPDATE STARTING ===")
    
    # Read backlog data
    df_backlog = read_backlog_data()
    print(f"Loaded {len(df_backlog)} stories from Backlog.xlsx")
    
    # Get stories to update
    stories_to_update = get_all_jira_stories()
    print(f"Found {len(stories_to_update)} stories that need updating")
    
    # Generate update data
    updates = []
    for key, summary in stories_to_update:
        match = match_jira_to_backlog(summary, df_backlog)
        
        if match is not None:
            estimation = match['Estimación'] if pd.notna(match['Estimación']) else 3
            backlog_title = str(match['Historia de Usuario'])
            criteria = str(match['Criterios de Aceptación'])
        else:
            estimation = 3
            backlog_title = summary
            criteria = '* La funcionalidad está disponible y operativa\\n* El sistema responde correctamente a las interacciones\\n* La interfaz es intuitiva y fácil de usar\\n* Se cumplen los requisitos del negocio'
        
        description = create_description(match, summary, estimation)
        
        updates.append({
            'jira_key': key,
            'jira_summary': summary,
            'description': description,
            'estimation': estimation,
            'match_found': match is not None
        })
    
    # Save updates to file
    with open('/home/joaquin-her/repos/gestion/all_jira_updates.json', 'w', encoding='utf-8') as f:
        json.dump(updates, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {len(updates)} updates")
    print("Saved to all_jira_updates.json")
    print()
    
    # Show sample of updates
    print("=== SAMPLE OF UPDATES TO MAKE ===")
    for i, update in enumerate(updates[:5]):
        print(f"{i+1}. {update['jira_key']}: {update['jira_summary']}")
        print(f"   Estimation: {update['estimation']} story points")
        print(f"   Match Found: {update['match_found']}")
        print()
    
    print(f"... and {len(updates) - 5} more updates")
    print()
    print("=== READY FOR BULK UPDATE ===")
    print("Run individual MCP calls for each update or use the prepared JSON file")
    
    return len(updates)

if __name__ == "__main__":
    total_updates = main()
    print(f"=== BULK UPDATE PREPARATION COMPLETE ===")
    print(f"Total updates prepared: {total_updates}")
