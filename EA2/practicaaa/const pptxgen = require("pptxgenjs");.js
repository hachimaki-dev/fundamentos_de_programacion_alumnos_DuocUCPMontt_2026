const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
 
// Icon imports
const { FaShieldAlt, FaMapMarkerAlt, FaBell, FaUsers, FaLock, FaMobileAlt,
        FaExclamationTriangle, FaCheckCircle, FaComments, FaEye, FaRocket,
        FaChartLine, FaHandsHelping, FaUserShield, FaSatellite, FaCog,
        FaLightbulb, FaGraduationCap, FaCity, FaBus, FaUserSecret,
        FaHeartbeat, FaStar, FaArrowRight, FaTimes, FaQuoteLeft } = require("react-icons/fa");
const { MdSecurity, MdLocationOn, MdNotifications, MdGroupWork, MdPhone,
        MdWarning, MdVerifiedUser, MdSmartphone } = require("react-icons/md");
const { BiTargetLock } = require("react-icons/bi");
 
// Colors
const C = {
  BLACK: "050A14",
  NAVY: "0A1628",
  DARK_NAVY: "0D1F3C",
  MID_NAVY: "112244",
  BLUE: "1A3A6B",
  ACCENT: "1E90FF",
  BRIGHT: "00B4FF",
  CYAN: "00D4FF",
  WHITE: "FFFFFF",
  GRAY: "8FA3BF",
  LIGHT_GRAY: "B0C4D8",
  CARD: "0E1E38",
  CARD2: "111D35",
  GLOW: "1565C0",
};
 
async function iconToPng(IconComponent, color = "#FFFFFF", size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
  const pngBuffer = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + pngBuffer.toString("base64");
}
 
// Helper: dark card shape
function addCard(slide, x, y, w, h, color = C.CARD) {
  slide.addShape("rect", {
    x, y, w, h,
    fill: { color },
    line: { color: C.ACCENT, width: 1 },
    shadow: { type: "outer", color: "000000", blur: 10, offset: 3, angle: 135, opacity: 0.4 }
  });
}
 
// Helper: section title
function addSlideTitle(slide, text, y = 0.35) {
  slide.addText(text, {
    x: 0.5, y, w: 9, h: 0.55,
    fontSize: 26, bold: true, color: C.WHITE,
    fontFace: "Calibri",
    align: "left", valign: "middle",
    margin: 0
  });
  // Accent line under title
  slide.addShape("rect", {
    x: 0.5, y: y + 0.58, w: 1.2, h: 0.05,
    fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 }
  });
}
 
async function buildPresentation() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625
 
  // Pre-render icons
  const icons = {
    shield: await iconToPng(FaShieldAlt, "#00B4FF"),
    map: await iconToPng(FaMapMarkerAlt, "#00B4FF"),
    bell: await iconToPng(FaBell, "#00B4FF"),
    users: await iconToPng(FaUsers, "#00B4FF"),
    lock: await iconToPng(FaLock, "#00B4FF"),
    mobile: await iconToPng(FaMobileAlt, "#00B4FF"),
    warning: await iconToPng(FaExclamationTriangle, "#FF6B35"),
    check: await iconToPng(FaCheckCircle, "#00D4FF"),
    chat: await iconToPng(FaComments, "#00B4FF"),
    eye: await iconToPng(FaEye, "#00B4FF"),
    rocket: await iconToPng(FaRocket, "#00B4FF"),
    chart: await iconToPng(FaChartLine, "#00B4FF"),
    hands: await iconToPng(FaHandsHelping, "#00B4FF"),
    userShield: await iconToPng(FaUserShield, "#00B4FF"),
    satellite: await iconToPng(FaSatellite, "#00B4FF"),
    lightbulb: await iconToPng(FaLightbulb, "#FFD700"),
    bus: await iconToPng(FaBus, "#FF6B35"),
    city: await iconToPng(FaCity, "#00B4FF"),
    heart: await iconToPng(FaHeartbeat, "#FF6B35"),
    star: await iconToPng(FaStar, "#FFD700"),
    quote: await iconToPng(FaQuoteLeft, "#1E90FF"),
    shieldWhite: await iconToPng(FaShieldAlt, "#FFFFFF"),
    warningYellow: await iconToPng(FaExclamationTriangle, "#FFD700"),
    userSecret: await iconToPng(FaUserSecret, "#00B4FF"),
    phone: await iconToPng(MdPhone, "#00B4FF"),
  };
 
  // ─────────────────────────────────────────────
  // SLIDE 1 – Portada
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.BLACK };
 
    // Geometric decorative shapes
    s.addShape("rect", { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.NAVY }, line: { color: C.NAVY, width: 0 } });
    // Left accent bar
    s.addShape("rect", { x: 0, y: 0, w: 0.12, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
    // Top-right diagonal accent
    s.addShape("rect", { x: 7.5, y: 0, w: 2.5, h: 0.08, fill: { color: C.BRIGHT }, line: { color: C.BRIGHT, width: 0 } });
    // Bottom accent
    s.addShape("rect", { x: 0, y: 5.52, w: 10, h: 0.1, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
    // Large shield icon background (faint)
    s.addImage({ data: icons.shieldWhite, x: 6.2, y: 0.3, w: 3.2, h: 3.2, transparency: 80 });
 
    // Tag / badge
    addCard(s, 0.55, 0.3, 3.2, 0.45, C.CARD2);
    s.addText("DUOC UC — BASES DE INNOVACIÓN", {
      x: 0.55, y: 0.3, w: 3.2, h: 0.45,
      fontSize: 8, bold: true, color: C.BRIGHT, fontFace: "Calibri",
      align: "center", valign: "middle", charSpacing: 2, margin: 0
    });
 
    // Main title
    s.addImage({ data: icons.shield, x: 0.5, y: 1.0, w: 0.75, h: 0.75 });
    s.addText("SECURITY MONTT", {
      x: 0.4, y: 1.05, w: 9, h: 1.1,
      fontSize: 56, bold: true, color: C.WHITE, fontFace: "Calibri",
      align: "left", valign: "middle", charSpacing: 4, margin: 0
    });
    // Accent under title
    s.addShape("rect", { x: 0.4, y: 2.1, w: 5.5, h: 0.05, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    s.addText("Aplicación de seguridad ciudadana para Puerto Montt", {
      x: 0.4, y: 2.25, w: 7.5, h: 0.65,
      fontSize: 18, bold: false, color: C.LIGHT_GRAY, fontFace: "Calibri",
      align: "left", valign: "top", margin: 0
    });
 
    // Team section
    s.addText("EQUIPO", {
      x: 0.4, y: 3.1, w: 2, h: 0.35,
      fontSize: 9, bold: true, color: C.ACCENT, fontFace: "Calibri",
      align: "left", charSpacing: 3, margin: 0
    });
 
    const names = ["Amaro González", "Alex Osorio", "Benjamín Sánchez", "Marcos Aguilar", "Rodrigo Valdivia"];
    names.forEach((name, i) => {
      const col = i < 3 ? 0 : 1;
      const row = i < 3 ? i : i - 3;
      s.addText("▸  " + name, {
        x: 0.4 + col * 3.2, y: 3.5 + row * 0.32, w: 3.0, h: 0.3,
        fontSize: 12, color: C.LIGHT_GRAY, fontFace: "Calibri",
        align: "left", valign: "middle", margin: 0
      });
    });
 
    // Year badge
    addCard(s, 7.9, 4.9, 1.7, 0.55, C.CARD2);
    s.addText("2024 — 2025", {
      x: 7.9, y: 4.9, w: 1.7, h: 0.55,
      fontSize: 10, bold: true, color: C.GRAY, fontFace: "Calibri",
      align: "center", valign: "middle", margin: 0
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 2 – Introducción
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Introducción");
 
    // Large city/bus icon
    s.addImage({ data: icons.bus, x: 7.0, y: 1.2, w: 2.5, h: 2.5, transparency: 20 });
 
    addCard(s, 0.5, 1.15, 6.2, 3.8, C.CARD);
    s.addImage({ data: icons.warning, x: 0.75, y: 1.4, w: 0.55, h: 0.55 });
    s.addText("El Problema", {
      x: 1.4, y: 1.38, w: 4.5, h: 0.6,
      fontSize: 18, bold: true, color: C.ACCENT, fontFace: "Calibri", margin: 0
    });
 
    s.addText([
      { text: "Muchas personas sienten inseguridad al utilizar locomoción pública o al caminar solas de noche, especialmente en los alrededores del ", options: { breakLine: false } },
      { text: "terminal de buses de Puerto Montt.", options: { bold: true, color: C.BRIGHT } }
    ], {
      x: 0.75, y: 2.1, w: 5.8, h: 1.4,
      fontSize: 14, color: C.LIGHT_GRAY, fontFace: "Calibri",
      align: "left", valign: "top", margin: 0
    });
 
    s.addText("Esta problemática afecta principalmente a quienes dependen del transporte público nocturno, exponiéndose a situaciones de riesgo sin contar con herramientas de apoyo inmediato.", {
      x: 0.75, y: 3.6, w: 5.8, h: 1.1,
      fontSize: 13, color: C.GRAY, fontFace: "Calibri",
      align: "left", valign: "top", margin: 0, italic: true
    });
 
    s.addImage({ data: icons.city, x: 0.75, y: 4.8, w: 0.35, h: 0.35 });
    s.addText("Puerto Montt, Región de Los Lagos", {
      x: 1.2, y: 4.83, w: 4, h: 0.3,
      fontSize: 11, color: C.GRAY, fontFace: "Calibri", margin: 0
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 3 – Contextualización del Problema
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: "FF4444" }, line: { color: "FF4444", width: 0 } });
 
    addSlideTitle(s, "Contextualización del Problema");
 
    const problems = [
      { icon: icons.warning, label: "Robos", desc: "Asaltos frecuentes en horario nocturno cerca del terminal" },
      { icon: icons.warning, label: "Violencia", desc: "Agresiones físicas y verbales en sectores poco vigilados" },
      { icon: icons.userSecret, label: "Drogas", desc: "Presencia de consumo y tráfico en las inmediaciones" },
      { icon: icons.eye, label: "Poca Vigilancia", desc: "Escasa presencia policial y cámaras de seguridad" },
      { icon: icons.heart, label: "Miedo e Inseguridad", desc: "Sensación generalizada de vulnerabilidad ciudadana" },
    ];
 
    problems.forEach((p, i) => {
      const col = i < 3 ? 0 : 1;
      const row = i < 3 ? i : i - 3;
      const x = col === 0 ? 0.4 : 5.2;
      const y = 1.1 + row * 1.35;
      const w = col === 0 ? 4.5 : 4.5;
 
      addCard(s, x, y, w, 1.1, C.CARD);
      s.addShape("rect", { x, y, w: 0.06, h: 1.1, fill: { color: "FF4444" }, line: { color: "FF4444", width: 0 } });
      s.addImage({ data: p.icon, x: x + 0.18, y: y + 0.28, w: 0.5, h: 0.5 });
      s.addText(p.label, { x: x + 0.82, y: y + 0.1, w: w - 0.95, h: 0.38, fontSize: 14, bold: true, color: C.WHITE, fontFace: "Calibri", margin: 0 });
      s.addText(p.desc, { x: x + 0.82, y: y + 0.48, w: w - 0.95, h: 0.55, fontSize: 11, color: C.GRAY, fontFace: "Calibri", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 4 – Evidencias y Fuentes
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Evidencias y Fuentes");
 
    s.addImage({ data: icons.chart, x: 7.5, y: 1.1, w: 2.1, h: 2.1, transparency: 30 });
 
    const sources = [
      {
        org: "Club de Emergencia Décima Región",
        text: "Registros y reportes de incidentes en las inmediaciones del terminal de Puerto Montt, documentando la alta frecuencia de situaciones de riesgo en horarios nocturnos.",
        color: C.ACCENT
      },
      {
        org: "BioBioChile",
        text: "Cobertura periodística sobre inseguridad y robos en el terminal de Puerto Montt, evidenciando una problemática que afecta a miles de ciudadanos que utilizan el transporte público.",
        color: C.BRIGHT
      }
    ];
 
    sources.forEach((src, i) => {
      const y = 1.2 + i * 2.0;
      addCard(s, 0.4, y, 6.8, 1.7, C.CARD);
      s.addShape("rect", { x: 0.4, y, w: 0.07, h: 1.7, fill: { color: src.color }, line: { color: src.color, width: 0 } });
      s.addImage({ data: icons.quote, x: 0.6, y: y + 0.12, w: 0.45, h: 0.45 });
      s.addText(src.org, { x: 1.15, y: y + 0.1, w: 5.8, h: 0.4, fontSize: 15, bold: true, color: src.color, fontFace: "Calibri", margin: 0 });
      s.addText(src.text, { x: 0.6, y: y + 0.58, w: 6.4, h: 1.0, fontSize: 12, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0 });
    });
 
    s.addText("Fuentes de investigación primaria utilizadas en el análisis del problema.", {
      x: 0.4, y: 5.15, w: 9, h: 0.3,
      fontSize: 10, color: C.GRAY, fontFace: "Calibri", italic: true, margin: 0
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 5 – Objetivo del Proyecto
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.BRIGHT }, line: { color: C.BRIGHT, width: 0 } });
 
    addSlideTitle(s, "Objetivo del Proyecto");
 
    s.addImage({ data: icons.rocket, x: 7.2, y: 0.9, w: 2.5, h: 2.5, transparency: 20 });
 
    addCard(s, 0.4, 1.1, 6.5, 1.6, C.CARD);
    s.addImage({ data: icons.mobile, x: 0.65, y: 1.3, w: 0.65, h: 0.65 });
    s.addText("Objetivo Principal", { x: 1.45, y: 1.15, w: 5.2, h: 0.4, fontSize: 17, bold: true, color: C.BRIGHT, fontFace: "Calibri", margin: 0 });
    s.addText("Desarrollar una aplicación móvil conectada al municipio de Puerto Montt que permita mejorar la seguridad ciudadana y agilizar la respuesta ante emergencias en tiempo real.", {
      x: 1.45, y: 1.6, w: 5.2, h: 1.0,
      fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0
    });
 
    const goals = [
      { icon: icons.bell, text: "Respuesta rápida ante emergencias" },
      { icon: icons.map, text: "Monitoreo en tiempo real con GPS" },
      { icon: icons.users, text: "Conexión directa con el municipio" },
      { icon: icons.shield, text: "Prevención y vigilancia ciudadana" },
    ];
 
    goals.forEach((g, i) => {
      const col = i % 2;
      const row = Math.floor(i / 2);
      const x = 0.4 + col * 4.85;
      const y = 2.95 + row * 1.15;
      addCard(s, x, y, 4.5, 0.9, C.CARD2);
      s.addImage({ data: g.icon, x: x + 0.18, y: y + 0.2, w: 0.5, h: 0.5 });
      s.addText(g.text, { x: x + 0.82, y: y + 0.18, w: 3.5, h: 0.5, fontSize: 13, color: C.WHITE, fontFace: "Calibri", valign: "middle", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 6 – Metodologías
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Metodologías Utilizadas");
 
    // DT card
    addCard(s, 0.4, 1.1, 4.3, 3.9, C.CARD);
    s.addShape("rect", { x: 0.4, y: 1.1, w: 4.3, h: 0.06, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
    s.addImage({ data: icons.lightbulb, x: 0.7, y: 1.25, w: 0.6, h: 0.6 });
    s.addText("Design Thinking", { x: 1.45, y: 1.25, w: 3.0, h: 0.55, fontSize: 18, bold: true, color: C.ACCENT, fontFace: "Calibri", margin: 0 });
    s.addText("Metodología centrada en el ser humano que permite comprender profundamente las necesidades del usuario para idear soluciones innovadoras.", {
      x: 0.65, y: 1.95, w: 3.8, h: 1.2,
      fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0
    });
    const dtSteps = ["Empatizar", "Definir", "Idear", "Prototipar", "Testear"];
    dtSteps.forEach((step, i) => {
      s.addShape("rect", { x: 0.65, y: 3.3 + i * 0.33, w: 0.28, h: 0.28, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
      s.addText(step, { x: 1.05, y: 3.3 + i * 0.33, w: 2.8, h: 0.28, fontSize: 13, color: C.WHITE, fontFace: "Calibri", valign: "middle", margin: 0 });
    });
 
    // Scrum card
    addCard(s, 5.1, 1.1, 4.5, 3.9, C.CARD);
    s.addShape("rect", { x: 5.1, y: 1.1, w: 4.5, h: 0.06, fill: { color: C.CYAN }, line: { color: C.CYAN, width: 0 } });
    s.addImage({ data: icons.users, x: 5.4, y: 1.25, w: 0.6, h: 0.6 });
    s.addText("Scrum", { x: 6.15, y: 1.25, w: 3.0, h: 0.55, fontSize: 18, bold: true, color: C.CYAN, fontFace: "Calibri", margin: 0 });
    s.addText("Framework ágil de gestión de proyectos que organiza el trabajo en sprints cortos para entregar valor de forma iterativa e incremental.", {
      x: 5.35, y: 1.95, w: 4.0, h: 1.2,
      fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0
    });
    const scrumItems = ["Product Owner", "Scrum Master", "Equipo de Desarrollo", "Sprint Planning", "Daily Standup"];
    scrumItems.forEach((item, i) => {
      s.addShape("rect", { x: 5.35, y: 3.3 + i * 0.33, w: 0.28, h: 0.28, fill: { color: C.CYAN }, line: { color: C.CYAN, width: 0 } });
      s.addText(item, { x: 5.75, y: 3.3 + i * 0.33, w: 3.5, h: 0.28, fontSize: 13, color: C.WHITE, fontFace: "Calibri", valign: "middle", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 7 – Design Thinking (detalle)
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Design Thinking — Etapas Aplicadas");
 
    const stages = [
      { name: "EMPATIZAR", color: "1E90FF", desc: "Entrevistas a usuarios que utilizan locomoción nocturna en Puerto Montt. Observación directa en el terminal de buses.", num: "01" },
      { name: "DEFINIR", color: "00B4FF", desc: "Identificación del POV: personas expuestas a inseguridad en el terminal sin herramientas de ayuda inmediata.", num: "02" },
      { name: "IDEAR", color: "00D4FF", desc: "Lluvia de ideas: botón SOS, GPS en tiempo real, alertas comunitarias, denuncias anónimas e inteligencia artificial.", num: "03" },
    ];
 
    stages.forEach((st, i) => {
      const x = 0.3 + i * 3.2;
      addCard(s, x, 1.1, 3.0, 3.9, C.CARD);
      s.addShape("rect", { x, y: 1.1, w: 3.0, h: 0.08, fill: { color: st.color }, line: { color: st.color, width: 0 } });
      // Big number
      s.addText(st.num, { x, y: 1.22, w: 3.0, h: 0.9, fontSize: 52, bold: true, color: st.color, fontFace: "Calibri", align: "center", margin: 0 });
      s.addText(st.name, { x, y: 2.18, w: 3.0, h: 0.45, fontSize: 14, bold: true, color: C.WHITE, fontFace: "Calibri", align: "center", charSpacing: 2, margin: 0 });
      s.addShape("rect", { x: x + 0.8, y: 2.65, w: 1.4, h: 0.04, fill: { color: st.color }, line: { color: st.color, width: 0 } });
      s.addText(st.desc, { x: x + 0.15, y: 2.8, w: 2.7, h: 2.0, fontSize: 12, color: C.LIGHT_GRAY, fontFace: "Calibri", align: "center", margin: 0 });
    });
 
    s.addImage({ data: icons.lightbulb, x: 4.5, y: 5.0, w: 0.4, h: 0.4 });
    s.addText("Solo las primeras 3 etapas fueron aplicadas en esta fase del proyecto.", {
      x: 5.0, y: 5.05, w: 4.6, h: 0.35,
      fontSize: 10, color: C.GRAY, fontFace: "Calibri", italic: true, margin: 0
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 8 – Scrum
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.CYAN }, line: { color: C.CYAN, width: 0 } });
 
    addSlideTitle(s, "Marco de Trabajo — Scrum");
 
    const roles = [
      { role: "Product Owner", name: "Amaro González", icon: icons.userShield, color: C.ACCENT, desc: "Define y prioriza el backlog. Representa los intereses del cliente." },
      { role: "Scrum Master", name: "Alex Osorio", icon: icons.shield, color: C.BRIGHT, desc: "Facilita el proceso Scrum y elimina impedimentos del equipo." },
      { role: "Dev Team", name: "Benjamín • Marcos • Rodrigo", icon: icons.users, color: C.CYAN, desc: "Desarrollan y entregan funcionalidades en cada sprint." },
    ];
 
    roles.forEach((r, i) => {
      const y = 1.15 + i * 1.42;
      addCard(s, 0.4, y, 5.0, 1.22, C.CARD);
      s.addShape("rect", { x: 0.4, y, w: 0.07, h: 1.22, fill: { color: r.color }, line: { color: r.color, width: 0 } });
      s.addImage({ data: r.icon, x: 0.6, y: y + 0.33, w: 0.55, h: 0.55 });
      s.addText(r.role, { x: 1.3, y: y + 0.1, w: 3.8, h: 0.4, fontSize: 14, bold: true, color: r.color, fontFace: "Calibri", margin: 0 });
      s.addText(r.name, { x: 1.3, y: y + 0.5, w: 3.8, h: 0.35, fontSize: 13, color: C.WHITE, fontFace: "Calibri", margin: 0 });
      s.addText(r.desc, { x: 1.3, y: y + 0.84, w: 3.8, h: 0.35, fontSize: 11, color: C.GRAY, fontFace: "Calibri", italic: true, margin: 0 });
    });
 
    // Sprint info
    addCard(s, 5.8, 1.15, 3.8, 3.65, C.CARD);
    s.addShape("rect", { x: 5.8, y: 1.15, w: 3.8, h: 0.07, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
    s.addText("SPRINT", { x: 5.8, y: 1.3, w: 3.8, h: 0.45, fontSize: 16, bold: true, color: C.ACCENT, fontFace: "Calibri", align: "center", charSpacing: 4, margin: 0 });
 
    const sprintItems = [
      "Planificación del Sprint",
      "Daily Standup diario",
      "Revisión de Sprint",
      "Retrospectiva",
      "Entrega de incremento",
    ];
    sprintItems.forEach((item, i) => {
      addCard(s, 6.0, 1.9 + i * 0.52, 3.4, 0.42, "112244");
      s.addShape("oval", { x: 6.1, y: 2.0 + i * 0.52, w: 0.22, h: 0.22, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
      s.addText(item, { x: 6.42, y: 1.93 + i * 0.52, w: 2.9, h: 0.4, fontSize: 12, color: C.WHITE, fontFace: "Calibri", valign: "middle", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 9 – Equipo Scrum
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Equipo Scrum");
 
    const members = [
      { name: "Amaro González", role: "Product Owner", color: C.ACCENT, icon: icons.userShield },
      { name: "Alex Osorio", role: "Scrum Master", color: C.BRIGHT, icon: icons.shield },
      { name: "Benjamín Sánchez", role: "Equipo Desarrollo", color: C.CYAN, icon: icons.users },
      { name: "Marcos Aguilar", role: "Equipo Desarrollo", color: C.CYAN, icon: icons.users },
      { name: "Rodrigo Valdivia", role: "Equipo Desarrollo", color: C.CYAN, icon: icons.users },
    ];
 
    members.forEach((m, i) => {
      const col = i < 2 ? i : i - 2;
      const row = i < 2 ? 0 : 1;
      let x, y, w;
      if (row === 0) {
        x = 0.4 + col * 4.85;
        y = 1.15;
        w = 4.4;
      } else {
        x = 0.4 + col * 3.2;
        y = 3.1;
        w = 2.95;
      }
      if (i === 4) x = 6.65;
 
      addCard(s, x, y, w, 1.65, C.CARD);
      s.addShape("rect", { x, y, w, h: 0.07, fill: { color: m.color }, line: { color: m.color, width: 0 } });
      s.addImage({ data: m.icon, x: x + 0.2, y: y + 0.45, w: 0.65, h: 0.65 });
      s.addText(m.name, { x: x + 1.0, y: y + 0.2, w: w - 1.1, h: 0.45, fontSize: 14, bold: true, color: C.WHITE, fontFace: "Calibri", margin: 0 });
      s.addText(m.role, { x: x + 1.0, y: y + 0.68, w: w - 1.1, h: 0.35, fontSize: 12, color: m.color, fontFace: "Calibri", margin: 0 });
      s.addText("Security Montt Team", { x: x + 1.0, y: y + 1.05, w: w - 1.1, h: 0.35, fontSize: 10, color: C.GRAY, fontFace: "Calibri", italic: true, margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 10 – Perfil del Usuario
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Perfil del Usuario");
 
    s.addImage({ data: icons.users, x: 7.8, y: 0.9, w: 2.0, h: 2.0, transparency: 25 });
 
    addCard(s, 0.4, 1.1, 7.0, 1.5, C.CARD);
    s.addImage({ data: icons.userShield, x: 0.65, y: 1.3, w: 0.75, h: 0.75 });
    s.addText("Usuario Principal", { x: 1.55, y: 1.15, w: 5.5, h: 0.45, fontSize: 17, bold: true, color: C.ACCENT, fontFace: "Calibri", margin: 0 });
    s.addText("Trabajador que utiliza locomoción pública nocturna en Puerto Montt", { x: 1.55, y: 1.62, w: 5.5, h: 0.75, fontSize: 14, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0 });
 
    const traits = [
      { label: "Perfil", val: "Adulto/joven trabajador, 18-50 años" },
      { label: "Contexto", val: "Usa buses nocturnos o camina en zonas de riesgo" },
      { label: "Situación", val: "Se ha enfrentado o teme enfrentar situaciones de riesgo" },
      { label: "Necesidad", val: "Herramienta de ayuda rápida conectada con autoridades" },
    ];
 
    traits.forEach((t, i) => {
      addCard(s, 0.4, 2.8 + i * 0.65, 9.2, 0.55, C.CARD2);
      s.addText(t.label + ":", { x: 0.6, y: 2.82 + i * 0.65, w: 1.6, h: 0.4, fontSize: 12, bold: true, color: C.BRIGHT, fontFace: "Calibri", margin: 0 });
      s.addText(t.val, { x: 2.3, y: 2.82 + i * 0.65, w: 7.0, h: 0.4, fontSize: 12, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 11 – Frustraciones del Usuario
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: "FF4444" }, line: { color: "FF4444", width: 0 } });
 
    addSlideTitle(s, "Frustraciones del Usuario");
 
    const frustrations = [
      { text: "Miedo a robos y asaltos nocturnos", icon: icons.warning },
      { text: "Exposición a violencia en la calle", icon: icons.warning },
      { text: "Falta de seguridad y protección", icon: icons.lock },
      { text: "Poca iluminación en sectores clave", icon: icons.eye },
      { text: "Desconfianza en el entorno urbano", icon: icons.heart },
    ];
 
    frustrations.forEach((f, i) => {
      const col = i % 2;
      const row = Math.floor(i / 2);
      if (i === 4) {
        addCard(s, 2.55, 4.1, 4.9, 1.05, C.CARD);
        s.addShape("rect", { x: 2.55, y: 4.1, w: 0.07, h: 1.05, fill: { color: "FF4444" }, line: { color: "FF4444", width: 0 } });
        s.addImage({ data: f.icon, x: 2.75, y: 4.28, w: 0.5, h: 0.5 });
        s.addText(f.text, { x: 3.4, y: 4.25, w: 3.7, h: 0.6, fontSize: 13, color: C.WHITE, fontFace: "Calibri", valign: "middle", margin: 0 });
      } else {
        const x = 0.4 + col * 5.0;
        const y = 1.15 + row * 1.45;
        addCard(s, x, y, 4.6, 1.25, C.CARD);
        s.addShape("rect", { x, y, w: 0.07, h: 1.25, fill: { color: "FF4444" }, line: { color: "FF4444", width: 0 } });
        s.addImage({ data: f.icon, x: x + 0.2, y: y + 0.35, w: 0.5, h: 0.5 });
        s.addText(f.text, { x: x + 0.85, y: y + 0.2, w: 3.5, h: 0.85, fontSize: 13, color: C.WHITE, fontFace: "Calibri", valign: "middle", margin: 0 });
      }
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 12 – Necesidades del Usuario
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.BRIGHT }, line: { color: C.BRIGHT, width: 0 } });
 
    addSlideTitle(s, "Necesidades del Usuario");
 
    const needs = [
      { text: "Protección inmediata ante situaciones de riesgo", icon: icons.shield, color: C.ACCENT },
      { text: "Comunicación rápida con autoridades y municipio", icon: icons.phone, color: C.BRIGHT },
      { text: "Monitoreo GPS en tiempo real de rutas seguras", icon: icons.map, color: C.CYAN },
      { text: "Vigilancia comunitaria colaborativa", icon: icons.eye, color: C.ACCENT },
      { text: "Respuesta rápida ante emergencias", icon: icons.bell, color: C.BRIGHT },
    ];
 
    needs.forEach((n, i) => {
      const y = 1.1 + i * 0.88;
      addCard(s, 0.4, y, 9.2, 0.75, C.CARD);
      s.addShape("rect", { x: 0.4, y, w: 0.07, h: 0.75, fill: { color: n.color }, line: { color: n.color, width: 0 } });
      s.addImage({ data: n.icon, x: 0.6, y: y + 0.12, w: 0.5, h: 0.5 });
      s.addText((i + 1).toString().padStart(2, "0"), { x: 1.25, y: y + 0.08, w: 0.5, h: 0.6, fontSize: 20, bold: true, color: n.color, fontFace: "Calibri", valign: "middle", margin: 0 });
      s.addText(n.text, { x: 1.85, y: y + 0.1, w: 7.4, h: 0.55, fontSize: 14, color: C.WHITE, fontFace: "Calibri", valign: "middle", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 13 – Entrevistas
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Entrevistas a Usuarios");
 
    const quotes = [
      { text: "\"Falta más seguridad en el sector del terminal.\"", profile: "Trabajadora, 34 años" },
      { text: "\"Da miedo esperar la locomoción de noche, hay gente sospechosa.\"", profile: "Estudiante, 22 años" },
      { text: "\"Sería muy útil tener alguna forma de pedir ayuda inmediata.\"", profile: "Usuario frecuente, 45 años" },
    ];
 
    quotes.forEach((q, i) => {
      const y = 1.15 + i * 1.48;
      addCard(s, 0.4, y, 9.2, 1.28, C.CARD);
      s.addShape("rect", { x: 0.4, y, w: 0.07, h: 1.28, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
      s.addImage({ data: icons.quote, x: 0.65, y: y + 0.12, w: 0.55, h: 0.55 });
      s.addText(q.text, { x: 1.35, y: y + 0.1, w: 7.9, h: 0.72, fontSize: 15, bold: true, color: C.WHITE, fontFace: "Calibri", margin: 0, italic: true });
      s.addText("— " + q.profile, { x: 1.35, y: y + 0.88, w: 7.9, h: 0.32, fontSize: 12, color: C.GRAY, fontFace: "Calibri", margin: 0 });
    });
 
    s.addText("Testimonios recopilados durante la fase de Empatía (Design Thinking).", {
      x: 0.4, y: 5.15, w: 9, h: 0.3,
      fontSize: 10, color: C.GRAY, fontFace: "Calibri", italic: true, margin: 0
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 14 – POV
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "POV — Punto de Vista");
 
    addCard(s, 0.4, 1.1, 9.2, 0.55, C.CARD2);
    s.addText("Point of View (POV)", { x: 0.55, y: 1.12, w: 9, h: 0.5, fontSize: 14, bold: true, color: C.BRIGHT, fontFace: "Calibri", charSpacing: 2, margin: 0 });
 
    addCard(s, 0.4, 1.85, 9.2, 2.2, C.CARD);
    s.addShape("rect", { x: 0.4, y: 1.85, w: 9.2, h: 0.07, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
    s.addImage({ data: icons.users, x: 0.65, y: 2.05, w: 0.8, h: 0.8 });
    s.addText("[Usuario]", { x: 1.6, y: 2.0, w: 3.0, h: 0.4, fontSize: 13, bold: true, color: C.ACCENT, fontFace: "Calibri", margin: 0 });
    s.addText("Las personas que se trasladan en el área del terminal de Puerto Montt durante horarios nocturnos", { x: 1.6, y: 2.42, w: 7.6, h: 0.6, fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0 });
    s.addText("[Necesitan]", { x: 1.6, y: 3.05, w: 3.0, h: 0.38, fontSize: 13, bold: true, color: C.BRIGHT, fontFace: "Calibri", margin: 0 });
    s.addText("una forma rápida y segura de pedir ayuda ante situaciones de peligro, porque", { x: 1.6, y: 3.45, w: 7.6, h: 0.45, fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0 });
 
    addCard(s, 0.4, 4.2, 9.2, 1.1, C.CARD2);
    s.addShape("rect", { x: 0.4, y: 4.2, w: 0.07, h: 1.1, fill: { color: C.CYAN }, line: { color: C.CYAN, width: 0 } });
    s.addText("[Insight]", { x: 0.6, y: 4.22, w: 2.0, h: 0.38, fontSize: 13, bold: true, color: C.CYAN, fontFace: "Calibri", margin: 0 });
    s.addText("se exponen diariamente a la delincuencia y violencia sin contar con ninguna herramienta digital de protección o alerta conectada al municipio.", { x: 0.6, y: 4.62, w: 8.8, h: 0.6, fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0 });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 15 – Lluvia de Ideas
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: "FFD700" }, line: { color: "FFD700", width: 0 } });
 
    addSlideTitle(s, "Lluvia de Ideas — Ideación");
 
    const ideas = [
      { idea: "Botón SOS", desc: "Alerta de emergencia inmediata", icon: icons.bell, color: "FF4444" },
      { idea: "GPS en Tiempo Real", desc: "Ubicación y rutas seguras", icon: icons.map, color: C.ACCENT },
      { idea: "Alertas Comunitarias", desc: "Notificaciones entre vecinos", icon: icons.bell, color: C.BRIGHT },
      { idea: "Reportes Ciudadanos", desc: "Denuncia incidentes con foto", icon: icons.eye, color: C.CYAN },
      { idea: "Chat Comunitario", desc: "Comunicación entre usuarios", icon: icons.chat, color: "FFD700" },
      { idea: "Denuncias Anónimas", desc: "Privacidad garantizada", icon: icons.userSecret, color: C.ACCENT },
      { idea: "IA y Reconocimiento", desc: "Detección automática de riesgos", icon: icons.satellite, color: C.BRIGHT },
    ];
 
    ideas.forEach((id, i) => {
      const col = i % 4;
      const row = Math.floor(i / 4);
      let x, y;
      if (row === 0) {
        x = 0.3 + col * 2.42;
        y = 1.05;
      } else {
        x = 0.95 + (col % 3) * 2.72;
        y = 3.1;
      }
      addCard(s, x, y, 2.2, 1.8, C.CARD);
      s.addShape("rect", { x, y, w: 2.2, h: 0.07, fill: { color: id.color }, line: { color: id.color, width: 0 } });
      s.addImage({ data: id.icon, x: x + 0.75, y: y + 0.2, w: 0.7, h: 0.7 });
      s.addText(id.idea, { x, y: y + 1.0, w: 2.2, h: 0.42, fontSize: 12, bold: true, color: C.WHITE, fontFace: "Calibri", align: "center", margin: 0 });
      s.addText(id.desc, { x, y: y + 1.4, w: 2.2, h: 0.38, fontSize: 10, color: C.GRAY, fontFace: "Calibri", align: "center", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 16 – Idea Final
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.BLACK };
    s.addShape("rect", { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.NAVY }, line: { color: C.NAVY, width: 0 } });
 
    // Big shield bg
    s.addImage({ data: icons.shieldWhite, x: 5.5, y: 0.2, w: 4.8, h: 4.8, transparency: 85 });
 
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    s.addText("IDEA FINAL", { x: 0.4, y: 0.5, w: 5.5, h: 0.45, fontSize: 11, bold: true, color: C.ACCENT, fontFace: "Calibri", charSpacing: 4, margin: 0 });
 
    s.addText("Security Montt", { x: 0.4, y: 0.95, w: 6.5, h: 1.0, fontSize: 44, bold: true, color: C.WHITE, fontFace: "Calibri", margin: 0 });
 
    s.addShape("rect", { x: 0.4, y: 1.97, w: 2.5, h: 0.05, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    s.addText("Una aplicación móvil enfocada en tres pilares:", {
      x: 0.4, y: 2.1, w: 5.5, h: 0.5,
      fontSize: 15, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0
    });
 
    const pillars = [
      { label: "PREVENCIÓN", desc: "Alertas y zonas de riesgo en tiempo real", icon: icons.shield, color: C.ACCENT },
      { label: "MONITOREO", desc: "GPS y vigilancia ciudadana colaborativa", icon: icons.map, color: C.BRIGHT },
      { label: "SEGURIDAD", desc: "Botón SOS y conexión con autoridades", icon: icons.bell, color: C.CYAN },
    ];
 
    pillars.forEach((p, i) => {
      const y = 2.75 + i * 0.88;
      addCard(s, 0.4, y, 5.6, 0.75, C.CARD);
      s.addShape("rect", { x: 0.4, y, w: 0.07, h: 0.75, fill: { color: p.color }, line: { color: p.color, width: 0 } });
      s.addImage({ data: p.icon, x: 0.6, y: y + 0.12, w: 0.5, h: 0.5 });
      s.addText(p.label, { x: 1.25, y: y + 0.05, w: 2.0, h: 0.38, fontSize: 14, bold: true, color: p.color, fontFace: "Calibri", charSpacing: 2, margin: 0 });
      s.addText(p.desc, { x: 1.25, y: y + 0.42, w: 4.5, h: 0.3, fontSize: 12, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 17 – Beneficios
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.DARK_NAVY };
    s.addShape("rect", { x: 0, y: 0, w: 0.08, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addSlideTitle(s, "Beneficios de Security Montt");
 
    const benefits = [
      { label: "Mayor Tranquilidad", desc: "Los ciudadanos se sienten acompañados y protegidos al usar el transporte nocturno.", icon: icons.check, color: C.ACCENT },
      { label: "Prevención de Delitos", desc: "Las alertas en tiempo real disuaden y previenen actos delictivos en la zona.", icon: icons.shield, color: C.BRIGHT },
      { label: "Respuesta Rápida", desc: "Conexión directa con Carabineros y municipio para atención en minutos.", icon: icons.bell, color: C.CYAN },
      { label: "Seguridad Comunitaria", desc: "Red de vecinos colaborando para mantener sectores seguros.", icon: icons.users, color: "FFD700" },
      { label: "Confianza Ciudadana", desc: "Mayor percepción de seguridad y recuperación del espacio público.", icon: icons.star, color: C.ACCENT },
    ];
 
    benefits.forEach((b, i) => {
      const col = i % 3;
      const row = Math.floor(i / 3);
      let x, y, w, h;
      if (row === 0) {
        x = 0.3 + col * 3.22;
        y = 1.1;
        w = 3.0;
        h = 2.1;
      } else {
        x = 1.4 + (i - 3) * 3.72;
        y = 3.35;
        w = 3.3;
        h = 1.95;
      }
      addCard(s, x, y, w, h, C.CARD);
      s.addShape("rect", { x, y, w, h: 0.07, fill: { color: b.color }, line: { color: b.color, width: 0 } });
      s.addImage({ data: b.icon, x: x + (w / 2) - 0.35, y: y + 0.25, w: 0.7, h: 0.7 });
      s.addText(b.label, { x, y: y + 1.05, w, h: 0.45, fontSize: 13, bold: true, color: b.color, fontFace: "Calibri", align: "center", margin: 0 });
      s.addText(b.desc, { x: x + 0.15, y: y + 1.5, w: w - 0.3, h: h - 1.6, fontSize: 11, color: C.LIGHT_GRAY, fontFace: "Calibri", align: "center", margin: 0 });
    });
  }
 
  // ─────────────────────────────────────────────
  // SLIDE 18 – Conclusión y Cierre
  // ─────────────────────────────────────────────
  {
    const s = pres.addSlide();
    s.background = { color: C.BLACK };
    s.addShape("rect", { x: 0, y: 0, w: 10, h: 5.625, fill: { color: C.NAVY }, line: { color: C.NAVY, width: 0 } });
    s.addShape("rect", { x: 0, y: 0, w: 0.12, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
    s.addShape("rect", { x: 0, y: 5.52, w: 10, h: 0.1, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
    s.addShape("rect", { x: 9.88, y: 0, w: 0.12, h: 5.625, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    // Big faint shield
    s.addImage({ data: icons.shieldWhite, x: 5.8, y: 0.3, w: 4.0, h: 4.0, transparency: 82 });
 
    s.addText("CONCLUSIÓN", { x: 0.55, y: 0.45, w: 4, h: 0.38, fontSize: 11, bold: true, color: C.ACCENT, fontFace: "Calibri", charSpacing: 4, margin: 0 });
    s.addText("Security Montt", { x: 0.55, y: 0.88, w: 7, h: 1.0, fontSize: 42, bold: true, color: C.WHITE, fontFace: "Calibri", margin: 0 });
    s.addShape("rect", { x: 0.55, y: 1.9, w: 3.2, h: 0.05, fill: { color: C.ACCENT }, line: { color: C.ACCENT, width: 0 } });
 
    addCard(s, 0.55, 2.1, 6.5, 2.1, C.CARD);
    s.addText("Este proyecto nace de la necesidad real de miles de ciudadanos que utilizan locomoción nocturna en Puerto Montt y se exponen diariamente a situaciones de inseguridad.", {
      x: 0.8, y: 2.2, w: 6.0, h: 0.95,
      fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0
    });
    s.addText("Security Montt propone una solución tecnológica, accesible y conectada al municipio, que permite a los ciudadanos enfrentar emergencias con herramientas modernas en tiempo real.", {
      x: 0.8, y: 3.2, w: 6.0, h: 0.95,
      fontSize: 13, color: C.LIGHT_GRAY, fontFace: "Calibri", margin: 0
    });
 
    s.addText("DUOC UC  —  Bases de Innovación  —  2024 / 2025", {
      x: 0.55, y: 4.45, w: 8.5, h: 0.35,
      fontSize: 10, bold: true, color: C.GRAY, fontFace: "Calibri", align: "left", charSpacing: 1, margin: 0
    });
 
    s.addImage({ data: icons.shield, x: 0.55, y: 4.85, w: 0.5, h: 0.5 });
    s.addText("Amaro González  •  Alex Osorio  •  Benjamín Sánchez  •  Marcos Aguilar  •  Rodrigo Valdivia", {
      x: 1.15, y: 4.9, w: 8.4, h: 0.35,
      fontSize: 11, color: C.GRAY, fontFace: "Calibri", margin: 0
    });
  }
 
  const outPath = "/mnt/user-data/outputs/SecurityMontt.pptx";
  await pres.writeFile({ fileName: outPath });
  console.log("✅ Saved:", outPath);
}
 
buildPresentation().catch(console.error);