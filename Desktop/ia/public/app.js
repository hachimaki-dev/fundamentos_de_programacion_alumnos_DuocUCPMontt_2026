/* ── JARVIS Client Application ── */
'use strict';

const API_BASE = window.location.origin;
let sessionId = 'session_' + Date.now();
let msgCount = 0;
let sessionStart = Date.now();
let isListening = false;
let isSpeaking = false;
let recognition = null;
let audioCtx = null;
let waveAnimFrame = null;

// ─── DOM refs ─────────────────────────────────────────────────────────────────
const coreOrb    = document.getElementById('coreOrb');
const coreStatus = document.getElementById('coreStatus');
const orbIcon    = document.getElementById('orbIcon');
const chatLog    = document.getElementById('chatLog');
const textInput  = document.getElementById('textInput');
const sendBtn    = document.getElementById('sendBtn');
const micBtn     = document.getElementById('micBtn');
const clearBtn   = document.getElementById('clearBtn');
const msgCounter = document.getElementById('msgCounter');
const sessionTimer = document.getElementById('sessionTimer');
const voiceToggle = document.getElementById('voiceToggle');
const waveformWrap = document.getElementById('waveformWrap');
const waveCanvas   = document.getElementById('waveCanvas');
const procFill     = document.getElementById('procFill');
const apiModal     = document.getElementById('apiModal');
const apiKeyInput  = document.getElementById('apiKeyInput');
const saveApiKeyBtn = document.getElementById('saveApiKey');
const apiStatus    = document.getElementById('apiStatus');

// ─── PARTICLE BACKGROUND ──────────────────────────────────────────────────────
(function initParticles() {
  const canvas = document.getElementById('particleCanvas');
  const ctx = canvas.getContext('2d');
  const particles = [];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  for (let i = 0; i < 60; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      size: Math.random() * 1.5 + 0.3,
      alpha: Math.random() * 0.4 + 0.1,
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = canvas.width;
      if (p.x > canvas.width) p.x = 0;
      if (p.y < 0) p.y = canvas.height;
      if (p.y > canvas.height) p.y = 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(0,212,255,${p.alpha})`;
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  draw();
})();

// ─── SESSION TIMER ────────────────────────────────────────────────────────────
setInterval(() => {
  const elapsed = Math.floor((Date.now() - sessionStart) / 1000);
  const m = String(Math.floor(elapsed / 60)).padStart(2, '0');
  const s = String(elapsed % 60).padStart(2, '0');
  sessionTimer.textContent = `${m}:${s}`;

  // Update footer clock
  const footerTime = document.getElementById('footerTime');
  if (footerTime) footerTime.textContent = new Date().toLocaleTimeString('es-MX');

  // Update HUD clock
  const clockVal = document.getElementById('clockVal');
  if (clockVal) clockVal.textContent = new Date().toLocaleTimeString('es-MX');
}, 1000);

// Set boot time
document.getElementById('bootTime').textContent = new Date().toLocaleTimeString('es-MX');

// ─── SYSTEM INFO ──────────────────────────────────────────────────────────────
async function fetchSystemInfo() {
  try {
    const res = await fetch(`${API_BASE}/api/system`);
    const data = await res.json();
    const cpu  = document.getElementById('cpuVal');
    const disk = document.getElementById('diskVal');
    const node = document.getElementById('nodeVal');
    if (cpu) cpu.textContent = data.cpu?.split(' ')[0] || '—';
    if (disk) disk.textContent = data.disk || '—';
    if (node) node.textContent = data.node || '—';
  } catch {}
}
fetchSystemInfo();

// ─── ORB STATE MACHINE ────────────────────────────────────────────────────────
function setOrbState(state) {
  coreOrb.className = 'core-orb';
  const states = {
    idle:      { cls: '',         icon: '⬡', label: 'AWAITING COMMAND',  bar: 0   },
    listening: { cls: 'listening', icon: '◉', label: 'LISTENING...',      bar: 85  },
    thinking:  { cls: 'thinking',  icon: '◌', label: 'PROCESSING...',     bar: 100 },
    speaking:  { cls: 'speaking',  icon: '◈', label: 'SPEAKING...',       bar: 65  },
    error:     { cls: '',          icon: '✕', label: 'SYSTEM ERROR',      bar: 0   },
  };
  const s = states[state] || states.idle;
  if (s.cls) coreOrb.classList.add(s.cls);
  orbIcon.textContent = s.icon;
  coreStatus.textContent = s.label;
  animateBar(procFill, s.bar);

  if (state === 'listening') {
    waveformWrap.classList.add('active');
    startWaveform();
  } else {
    waveformWrap.classList.remove('active');
    stopWaveform();
  }
}

function animateBar(el, target) {
  let curr = 0;
  const step = () => {
    curr = Math.min(curr + 4, target);
    el.style.width = curr + '%';
    if (curr < target) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

// ─── WAVEFORM ─────────────────────────────────────────────────────────────────
function startWaveform() {
  const ctx = waveCanvas.getContext('2d');
  let t = 0;
  function draw() {
    ctx.clearRect(0, 0, waveCanvas.width, waveCanvas.height);
    ctx.beginPath();
    const bars = 40;
    const bw = waveCanvas.width / bars;
    for (let i = 0; i < bars; i++) {
      const h = Math.abs(Math.sin(i * 0.5 + t) * Math.sin(i * 0.2 - t * 0.7)) * 35 + 4;
      const x = i * bw + bw / 2;
      const y = waveCanvas.height / 2;
      ctx.fillStyle = `rgba(0,212,255,${0.3 + h / 50})`;
      ctx.fillRect(x - 1.5, y - h / 2, 3, h);
    }
    t += 0.12;
    waveAnimFrame = requestAnimationFrame(draw);
  }
  draw();
}

function stopWaveform() {
  if (waveAnimFrame) { cancelAnimationFrame(waveAnimFrame); waveAnimFrame = null; }
  const ctx = waveCanvas.getContext('2d');
  ctx.clearRect(0, 0, waveCanvas.width, waveCanvas.height);
}

// ─── CHAT ─────────────────────────────────────────────────────────────────────
function addMessage(role, text, animate = true) {
  const wrap = document.createElement('div');
  wrap.className = `msg-wrap ${role === 'user' ? 'user-wrap' : 'jarvis-wrap'}`;
  if (!animate) wrap.style.animation = 'none';

  const sender = document.createElement('span');
  sender.className = 'msg-sender';
  sender.textContent = role === 'user' ? 'YOU' : 'JARVIS';

  const bubble = document.createElement('div');
  bubble.className = `msg-bubble ${role === 'user' ? 'user-bubble' : 'jarvis-bubble'}`;
  bubble.textContent = text;

  const time = document.createElement('span');
  time.className = 'msg-time';
  time.textContent = new Date().toLocaleTimeString('es-MX');

  wrap.appendChild(sender);
  wrap.appendChild(bubble);
  wrap.appendChild(time);
  chatLog.appendChild(wrap);
  chatLog.scrollTop = chatLog.scrollHeight;

  if (role === 'user') {
    msgCount++;
    msgCounter.textContent = msgCount;
  }
  return bubble;
}

function showTyping() {
  const wrap = document.createElement('div');
  wrap.className = 'msg-wrap jarvis-wrap';
  wrap.id = 'typingIndicator';

  const sender = document.createElement('span');
  sender.className = 'msg-sender';
  sender.textContent = 'JARVIS';

  const dots = document.createElement('div');
  dots.className = 'typing-dots';
  dots.innerHTML = '<span></span><span></span><span></span>';

  wrap.appendChild(sender);
  wrap.appendChild(dots);
  chatLog.appendChild(wrap);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function hideTyping() {
  const el = document.getElementById('typingIndicator');
  if (el) el.remove();
}

// ─── VOICE SYNTHESIS ──────────────────────────────────────────────────────────
function speakText(text) {
  if (!voiceToggle.checked) return;

  // Use Web Speech API (uses macOS voices in Safari/Chrome)
  const synth = window.speechSynthesis;
  if (!synth) return;

  synth.cancel();
  const utt = new SpeechSynthesisUtterance(text);
  utt.lang = 'en-US';
  utt.rate = 1.0;
  utt.pitch = 0.85;
  utt.volume = 1;

  // Try to pick a nice English voice
  const voices = synth.getVoices();
  const preferred = ['Daniel', 'Oliver', 'Samantha', 'Alex', 'Tom'];
  for (const name of preferred) {
    const v = voices.find(v => v.name.includes(name));
    if (v) { utt.voice = v; break; }
  }

  setOrbState('speaking');
  isSpeaking = true;

  utt.onend = () => { isSpeaking = false; setOrbState('idle'); };
  utt.onerror = () => { isSpeaking = false; setOrbState('idle'); };

  synth.speak(utt);
}

// ─── SEND MESSAGE ─────────────────────────────────────────────────────────────
async function sendMessage(text) {
  if (!text.trim() || isSpeaking) return;

  addMessage('user', text);
  textInput.value = '';
  setOrbState('thinking');
  showTyping();

  try {
    const res = await fetch(`${API_BASE}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text, sessionId }),
    });

    const data = await res.json();
    hideTyping();

    if (data.error === 'API_KEY_MISSING') {
      addMessage('jarvis', '⚠ API key not configured. Please add your Gemini key to the .env file and restart the server.');
      setOrbState('error');
      apiModal.style.display = 'flex';
      return;
    }

    const reply = data.response || 'I apologize, Sir. No response received.';
    addMessage('jarvis', reply);
    setOrbState('idle');
    speakText(reply);
    apiStatus.textContent = 'GEMINI: CONNECTED';
    apiStatus.style.color = 'var(--green)';

  } catch (err) {
    hideTyping();
    addMessage('jarvis', `Network error: ${err.message}. Please ensure the server is running on port 3000, Sir.`);
    setOrbState('error');
    apiStatus.textContent = 'SERVER: OFFLINE';
    apiStatus.style.color = 'var(--red)';
    setTimeout(() => setOrbState('idle'), 2000);
  }
}

// ─── VOICE RECOGNITION ────────────────────────────────────────────────────────
function initSpeechRecognition() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    micBtn.title = 'Voice not supported in this browser';
    micBtn.style.opacity = '0.4';
    return;
  }

  recognition = new SpeechRecognition();
  recognition.lang = 'es-MX';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onstart = () => {
    isListening = true;
    micBtn.classList.add('listening');
    setOrbState('listening');
  };

  recognition.onresult = (e) => {
    const transcript = e.results[0][0].transcript;
    textInput.value = transcript;
    sendMessage(transcript);
  };

  recognition.onerror = (e) => {
    console.warn('Speech error:', e.error);
    stopListening();
  };

  recognition.onend = () => stopListening();
}

function startListening() {
  if (!recognition) return;
  if (isListening) { recognition.stop(); return; }
  try { recognition.start(); } catch (e) { console.warn(e); }
}

function stopListening() {
  isListening = false;
  micBtn.classList.remove('listening');
  if (!isSpeaking) setOrbState('idle');
}

// ─── EVENT LISTENERS ──────────────────────────────────────────────────────────
sendBtn.addEventListener('click', () => sendMessage(textInput.value));

textInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(textInput.value); }
});

micBtn.addEventListener('click', startListening);

clearBtn.addEventListener('click', () => {
  chatLog.innerHTML = '';
  msgCount = 0;
  msgCounter.textContent = 0;
  sessionId = 'session_' + Date.now();
  addMessage('jarvis', 'Conversation log cleared. Ready for new directives, Sir.', false);
});

// Quick command buttons
document.getElementById('cmdSafari')?.addEventListener('click',   () => sendMessage('open Safari'));
document.getElementById('cmdSpotify')?.addEventListener('click',  () => sendMessage('open Spotify'));
document.getElementById('cmdFinder')?.addEventListener('click',   () => sendMessage('open Finder'));
document.getElementById('cmdTerminal')?.addEventListener('click', () => sendMessage('open Terminal'));
document.getElementById('cmdCalc')?.addEventListener('click',     () => sendMessage('open Calculator'));
document.getElementById('cmdNotes')?.addEventListener('click',    () => sendMessage('open Notes'));

// Clickable command examples in right panel
document.querySelectorAll('.cmd-item').forEach(el => {
  el.addEventListener('click', () => {
    const cmd = el.textContent.replace(/"/g, '').trim();
    textInput.value = cmd;
    textInput.focus();
  });
});

// API key modal save
saveApiKeyBtn?.addEventListener('click', () => {
  const key = apiKeyInput.value.trim();
  if (!key || !key.startsWith('AIza')) {
    apiKeyInput.style.borderColor = 'var(--red)';
    return;
  }
  addMessage('jarvis', 'API key received. However, to apply it you need to add it to your .env file on the server and restart. I\'ll guide you through it, Sir.\n\nIn your terminal:\n1. Open /Desktop/ia/.env\n2. Set GEMINI_API_KEY=YOUR_KEY\n3. Run: npm start');
  apiModal.style.display = 'none';
});

// Auto-listen after JARVIS speaks
document.getElementById('autoListenToggle')?.addEventListener('change', (e) => {
  if (e.target.checked) {
    addMessage('jarvis', 'Auto-listen mode enabled. I will begin listening immediately after each response, Sir.');
  }
});

// Load voices after page load (required by some browsers)
window.speechSynthesis?.addEventListener('voiceschanged', () => {});

// ─── INIT ─────────────────────────────────────────────────────────────────────
initSpeechRecognition();
setOrbState('idle');

// Focus input on load
setTimeout(() => textInput.focus(), 500);

console.log('%c J.A.R.V.I.S. ONLINE ', 'background:#00d4ff;color:#000;font-weight:bold;font-size:16px;padding:4px 12px;border-radius:4px;');
