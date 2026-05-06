const pptxgen = require("pptxgenjs");

let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.author = 'AI Assistant';
pres.title = 'Matriz de Riesgos - Appointa';

// Slide 1: Title Slide
let slide1 = pres.addSlide();
slide1.background = { color: "1E293B" }; // slate-800

slide1.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0.5, w: 10, h: 2,
  fill: { color: "0F172A" } // slate-900
});

slide1.addText("Matriz de Riesgos", {
  x: 0.5, y: 0.8, w: 9, h: 1, 
  fontSize: 44, color: "FFFFFF", bold: true, fontFace: "Helvetica"
});

slide1.addText("Proyecto Appointa", {
  x: 0.5, y: 1.7, w: 9, h: 0.5,
  fontSize: 24, color: "94A3B8", fontFace: "Helvetica" // slate-400
});

slide1.addText("Análisis de Riesgos y Puntos Críticos", {
  x: 0.5, y: 3.5, w: 9, h: 0.5,
  fontSize: 18, color: "CBD5E1", fontFace: "Helvetica", italic: true
});

// Slide 2: Riesgos Críticos
let slide2 = pres.addSlide();
slide2.background = { color: "F8FAFC" }; // slate-50

slide2.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 0.5, w: 0.1, h: 0.6,
  fill: { color: "DC2626" } // red-600
});

slide2.addText("Riesgos Críticos (Exposición Alta)", {
  x: 0.7, y: 0.5, w: 8.5, h: 0.6,
  fontSize: 32, color: "0F172A", bold: true, fontFace: "Helvetica", margin: 0
});

// Card 1
slide2.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.5, w: 4.25, h: 3,
  fill: { color: "FFFFFF" },
  shadow: { type: "outer", color: "000000", blur: 6, offset: 3, angle: 45, opacity: 0.08 }
});

slide2.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.5, w: 4.25, h: 0.1,
  fill: { color: "DC2626" } // red-600 top border
});

slide2.addText("Coordinación del Equipo", {
  x: 0.7, y: 1.8, w: 3.8, h: 0.4,
  fontSize: 20, color: "1E293B", bold: true, fontFace: "Helvetica", margin: 0
});

slide2.addText([
  { text: "Problema:", options: { bold: true, color: "475569" } },
  { text: " Dificultad para coordinar reuniones con los 6 integrantes debido a horarios por trabajos de medio tiempo.\n\n", options: { color: "334155" } },
  { text: "Área:", options: { bold: true, color: "475569" } },
  { text: " Gestión del Proyecto\n", options: { color: "334155" } },
  { text: "Impacto:", options: { bold: true, color: "475569" } },
  { text: " Alto", options: { color: "DC2626", bold: true } }
], {
  x: 0.7, y: 2.3, w: 3.85, h: 2,
  fontSize: 14, fontFace: "Helvetica", margin: 0, valign: "top", breakLine: true
});

// Card 2
slide2.addShape(pres.shapes.RECTANGLE, {
  x: 5.25, y: 1.5, w: 4.25, h: 3,
  fill: { color: "FFFFFF" },
  shadow: { type: "outer", color: "000000", blur: 6, offset: 3, angle: 45, opacity: 0.08 }
});

slide2.addShape(pres.shapes.RECTANGLE, {
  x: 5.25, y: 1.5, w: 4.25, h: 0.1,
  fill: { color: "DC2626" }
});

slide2.addText("Complejidad de la Plataforma", {
  x: 5.45, y: 1.8, w: 3.8, h: 0.4,
  fontSize: 20, color: "1E293B", bold: true, fontFace: "Helvetica", margin: 0
});

slide2.addText([
  { text: "Problema:", options: { bold: true, color: "475569" } },
  { text: " Complejidad subestimada en el desarrollo de la plataforma de gestión de turnos con modelo de membresías.\n\n", options: { color: "334155" } },
  { text: "Área:", options: { bold: true, color: "475569" } },
  { text: " Gestión del Proyecto\n", options: { color: "334155" } },
  { text: "Impacto:", options: { bold: true, color: "475569" } },
  { text: " Alto", options: { color: "DC2626", bold: true } }
], {
  x: 5.45, y: 2.3, w: 3.85, h: 2,
  fontSize: 14, fontFace: "Helvetica", margin: 0, valign: "top", breakLine: true
});


// Slide 3: Riesgos Moderados
let slide3 = pres.addSlide();
slide3.background = { color: "F8FAFC" }; // slate-50

slide3.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 0.5, w: 0.1, h: 0.6,
  fill: { color: "EAB308" } // yellow-500
});

slide3.addText("Riesgos Moderados (Exposición Media)", {
  x: 0.7, y: 0.5, w: 8.5, h: 0.6,
  fontSize: 32, color: "0F172A", bold: true, fontFace: "Helvetica", margin: 0
});

// Create 3 columns for the categories
let colWidth = 2.8;

// Column 1: Técnico
slide3.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.5, w: colWidth, h: 3.5, fill: { color: "FFFFFF" },
  shadow: { type: "outer", color: "000000", blur: 6, offset: 2, angle: 45, opacity: 0.08 }
});
slide3.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.5, w: colWidth, h: 0.1, fill: { color: "3B82F6" } }); // blue

slide3.addText("Técnico", { x: 0.6, y: 1.7, w: 2.6, h: 0.4, fontSize: 18, color: "1E293B", bold: true, fontFace: "Helvetica", margin: 0 });
slide3.addText([
  { text: "Inconsistencia de código", options: { bullet: true, breakLine: true, bold: true, color: "334155" } },
  { text: "Por falta de estandarización entre 6 devs.\n", options: { color: "64748B", fontSize: 11, breakLine: true } },
  { text: "Excesiva dependencia de IA", options: { bullet: true, breakLine: true, bold: true, color: "334155" } },
  { text: "Sin comprensión profunda del código.\n", options: { color: "64748B", fontSize: 11, breakLine: true } },
  { text: "Problemas en demos vivas", options: { bullet: true, breakLine: true, bold: true, color: "334155" } },
  { text: "Fallos durante las defensas semanales.", options: { color: "64748B", fontSize: 11 } }
], {
  x: 0.6, y: 2.2, w: 2.6, h: 2.7, fontSize: 13, fontFace: "Helvetica", margin: 0, valign: "top"
});


// Column 2: Recursos Humanos
slide3.addShape(pres.shapes.RECTANGLE, {
  x: 3.6, y: 1.5, w: colWidth, h: 3.5, fill: { color: "FFFFFF" },
  shadow: { type: "outer", color: "000000", blur: 6, offset: 2, angle: 45, opacity: 0.08 }
});
slide3.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 1.5, w: colWidth, h: 0.1, fill: { color: "F59E0B" } }); // amber

slide3.addText("Recursos Humanos", { x: 3.7, y: 1.7, w: 2.6, h: 0.4, fontSize: 18, color: "1E293B", bold: true, fontFace: "Helvetica", margin: 0 });
slide3.addText([
  { text: "Falta de experiencia ágil", options: { bullet: true, breakLine: true, bold: true, color: "334155" } },
  { text: "El equipo no ha trabajado junto bajo este marco.\n", options: { color: "64748B", fontSize: 11, breakLine: true } },
  { text: "Agotamiento del equipo", options: { bullet: true, breakLine: true, bold: true, color: "334155" } },
  { text: "Por carga académica combinada con part-time.", options: { color: "64748B", fontSize: 11 } }
], {
  x: 3.7, y: 2.2, w: 2.6, h: 2.7, fontSize: 13, fontFace: "Helvetica", margin: 0, valign: "top"
});


// Column 3: Académico
slide3.addShape(pres.shapes.RECTANGLE, {
  x: 6.7, y: 1.5, w: colWidth, h: 3.5, fill: { color: "FFFFFF" },
  shadow: { type: "outer", color: "000000", blur: 6, offset: 2, angle: 45, opacity: 0.08 }
});
slide3.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 1.5, w: colWidth, h: 0.1, fill: { color: "8B5CF6" } }); // purple

slide3.addText("Académico", { x: 6.8, y: 1.7, w: 2.6, h: 0.4, fontSize: 18, color: "1E293B", bold: true, fontFace: "Helvetica", margin: 0 });
slide3.addText([
  { text: "Falta de preparación", options: { bullet: true, breakLine: true, bold: true, color: "334155" } },
  { text: "Para defensas semanales debido a la presión y poco tiempo.", options: { color: "64748B", fontSize: 11 } }
], {
  x: 6.8, y: 2.2, w: 2.6, h: 2.7, fontSize: 13, fontFace: "Helvetica", margin: 0, valign: "top"
});

// Slide 4: Planes de Respuesta y Contingencia
let slide4 = pres.addSlide();
slide4.background = { color: 'F8FAFC' };

slide4.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 0.5, w: 0.1, h: 0.6,
  fill: { color: '10B981' } // emerald-500
});

slide4.addText('Planes de Respuesta y Contingencia', {
  x: 0.7, y: 0.5, w: 8.5, h: 0.6,
  fontSize: 32, color: '0F172A', bold: true, fontFace: 'Helvetica', margin: 0
});

// Riesgo 1: Coordinación
slide4.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.5, w: 9, h: 1.6, fill: { color: 'FFFFFF' },
  shadow: { type: 'outer', color: '000000', blur: 6, offset: 2, angle: 45, opacity: 0.08 }
});
slide4.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.5, w: 0.05, h: 1.6, fill: { color: '3B82F6' } });

slide4.addText('Riesgo Crítico: Coordinación del Equipo', { x: 0.7, y: 1.6, w: 8.5, h: 0.4, fontSize: 18, color: '1E293B', bold: true, fontFace: 'Helvetica', margin: 0 });
slide4.addText([
  { text: 'Plan de Respuesta: ', options: { bold: true, color: '10B981' } },
  { text: 'Establecer comunicación asíncrona robusta, minutas obligatorias en Daily y seguimiento riguroso de tareas.\n', options: { color: '334155' } },
  { text: 'Plan de Contingencia: ', options: { bold: true, color: 'F59E0B' } },
  { text: 'Grabar reuniones clave; sistema de votación asíncrona para decisiones críticas si no hay quorum.', options: { color: '334155' } }
], { x: 0.7, y: 2.1, w: 8.5, h: 0.9, fontSize: 14, fontFace: 'Helvetica', margin: 0, valign: 'top', breakLine: true });

// Riesgo 2: Complejidad
slide4.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 3.4, w: 9, h: 1.6, fill: { color: 'FFFFFF' },
  shadow: { type: 'outer', color: '000000', blur: 6, offset: 2, angle: 45, opacity: 0.08 }
});
slide4.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.4, w: 0.05, h: 1.6, fill: { color: '8B5CF6' } });

slide4.addText('Riesgo Crítico: Complejidad de la Plataforma', { x: 0.7, y: 3.5, w: 8.5, h: 0.4, fontSize: 18, color: '1E293B', bold: true, fontFace: 'Helvetica', margin: 0 });
slide4.addText([
  { text: 'Plan de Respuesta: ', options: { bold: true, color: '10B981' } },
  { text: 'Desarrollo iterativo priorizando el MVP; estandarización de arquitectura y buenas prácticas desde el Día 1.\n', options: { color: '334155' } },
  { text: 'Plan de Contingencia: ', options: { bold: true, color: 'F59E0B' } },
  { text: 'Reducción del alcance del MVP (ej. posponer sistema de membresías complejas) y usar tecnologías de confort.', options: { color: '334155' } }
], { x: 0.7, y: 4.0, w: 8.5, h: 0.9, fontSize: 14, fontFace: 'Helvetica', margin: 0, valign: 'top', breakLine: true });

pres.writeFile({ fileName: "Resumen_Riesgos_Appointa.pptx" }).then(() => {
  console.log("created Resumen_Riesgos_Appointa.pptx");
});
