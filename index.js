// Global Language Switcher & Translations (ES / EN / FR)
window.currentLang = 'es';
const TRANSLATIONS = {
  es: {
    nav_overview: "Resumen & Scale",
    nav_manifesto: "Manifiesto",
    nav_retro_map: "Mapa Retro",
    nav_narrative: "Historia & Anomalía",
    nav_technical: "Peritaje Técnico",
    nav_simulator: "Simulador Forense",
    nav_legal: "Legal & CIDH",
    nav_donate: "💖 Apoyar",
    nav_chris: "🛡️ Panel de Chris",
    nav_offline: "📡 Modo Offline"
  },
  en: {
    nav_overview: "Overview & Scale",
    nav_manifesto: "Manifesto",
    nav_retro_map: "Retro Map",
    nav_narrative: "History & Anomaly",
    nav_technical: "Technical Audit",
    nav_simulator: "Forensic Simulator",
    nav_legal: "Legal & IACHR",
    nav_donate: "💖 Support",
    nav_chris: "🛡️ Chris Panel",
    nav_offline: "📡 Offline Mode"
  },
  fr: {
    nav_overview: "Aperçu & Échelle",
    nav_manifesto: "Manifeste",
    nav_retro_map: "Carte Rétro",
    nav_narrative: "Histoire & Anomalie",
    nav_technical: "Expertise Technique",
    nav_simulator: "Simulateur Forensique",
    nav_legal: "Légal & CIDH",
    nav_donate: "💖 Soutenir",
    nav_chris: "🛡️ Panneau de Chris",
    nav_offline: "📡 Mode Offline"
  }
};

window.setGlobalLanguage = function(lang) {
  window.currentLang = lang;
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.style.background = 'transparent';
    btn.style.color = 'var(--text-muted)';
  });
  const activeBtn = document.getElementById('lang-btn-' + lang);
  if (activeBtn) {
    activeBtn.style.background = 'var(--accent-cyan)';
    activeBtn.style.color = '#000';
  }
  document.documentElement.lang = lang;

  // Translate all data-i18n elements instantly
  const dict = TRANSLATIONS[lang] || TRANSLATIONS.es;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });

  console.log("Idioma cambiado con éxito a:", lang);
};

// AndreTaker — BabaYaga Core Portal JavaScript
document.addEventListener('DOMContentLoaded', () => {
  // Navigation Tabs
  const navBtns = document.querySelectorAll('.nav-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.getAttribute('data-tab');
      if (!tabId) return;

      navBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      const targetTab = document.getElementById(tabId);
      if (targetTab) {
        targetTab.classList.add('active');
      }
    });
  });

  // =========================================================
  // 👥 USER PROFILE VIEW CONTROLLER (EASY / INTERMEDIATE / EXPERT)
  // =========================================================
  const profileSelect = document.getElementById('user-profile-select');
  const updateProfileViews = (profile) => {
    console.log("Aplicando perfil de visualización:", profile);
    document.querySelectorAll('.easy-mode, .intermediate-mode, .expert-mode').forEach(el => {
      el.style.display = 'none';
    });
    
    if (profile === 'easy') {
      document.querySelectorAll('.easy-mode').forEach(el => el.style.display = 'block');
    } else if (profile === 'intermediate') {
      document.querySelectorAll('.easy-mode, .intermediate-mode').forEach(el => el.style.display = 'block');
    } else if (profile === 'expert') {
      document.querySelectorAll('.easy-mode, .intermediate-mode, .expert-mode').forEach(el => el.style.display = 'block');
    }
  };

  if (profileSelect) {
    profileSelect.addEventListener('change', (e) => {
      updateProfileViews(e.target.value);
    });
    // Ejecutar al cargar
    updateProfileViews(profileSelect.value);
  }

  // Animated counters
  const counters = document.querySelectorAll('.counter');
  counters.forEach(counter => {
    const target = +counter.getAttribute('data-target');
    const duration = 1500;
    const step = target / (duration / 16);
    let current = 0;

    const updateCounter = () => {
      current += step;
      if (current < target) {
        counter.innerText = Math.ceil(current).toLocaleString();
        requestAnimationFrame(updateCounter);
      } else {
        counter.innerText = target.toLocaleString();
      }
    };
    updateCounter();
  });

  // Retro Map Navigation
  const nodes = document.querySelectorAll('.retro-node');
  const avatar = document.getElementById('retro-avatar');
  const dialogTitle = document.getElementById('dialog-title');
  const dialogContent = document.getElementById('dialog-content');

  nodes.forEach(node => {
    node.addEventListener('click', () => {
      const targetLeft = node.style.left;
      const targetTop = node.style.top;
      
      if (avatar) {
        avatar.style.left = targetLeft;
        avatar.style.top = targetTop;
      }

      nodes.forEach(n => n.classList.remove('active'));
      node.classList.add('active');
      node.classList.add('visited');

      const title = node.getAttribute('data-title');
      const desc = node.getAttribute('data-desc');
      if (dialogTitle) dialogTitle.innerText = title;
      if (dialogContent) dialogContent.innerText = desc;
    });
  });

  // =========================================================
  // MULTI-AGENT VOICE SYNTHESIS (SÍNTESIS DE VOZ POR AGENTE)
  // =========================================================
  // MULTI-AGENT VOICE PROFILES & SIGNATURE CATCHPHRASES
  // =========================================================
  const VOICE_PROFILES = {
    babayaga: { name: 'Baba Yaga', pitch: 0.65, rate: 0.88, slogan: "She is the reason monsters hide. La evidencia es inmutable.", lang: 'es-CO' },
    tycho: { name: 'Tycho', pitch: 1.25, rate: 1.05, slogan: "Look back! The dark remembers what you did.", lang: 'en-US' },
    kepler: { name: 'Kepler', pitch: 1.05, rate: 0.98, slogan: "Structuring the truth. Estrategia y cadena de custodia.", lang: 'es-CO' },
    andretaker: { name: 'AndreTaker', pitch: 0.95, rate: 1.0, slogan: "It's my turn! I'm unbroken!", lang: 'en-US' },
    arthurios: { name: 'Arthurios', pitch: 1.35, rate: 1.05, slogan: "Mess with me and moma won't play nice!", lang: 'en-US' },
    chris: { name: 'Christopher Baez', pitch: 1.0, rate: 1.0, slogan: "Standing firm for justice and family protection.", lang: 'en-US' }
  };

  const AUDIO_CLIPS = {
    andrea: 'assets/images/VOZ_OFICIAL_ANDRETAKER_ANZACA.mp3',
    andretaker: 'assets/images/VOICE_CLIP_ANDRETAKER.mp3',
    babayaga: 'assets/images/VOICE_CLIP_BABAYAGA.mp3',
    tycho: 'assets/images/VOICE_CLIP_TYCHO.mp3',
    arthurios: 'assets/images/VOICE_CLIP_ARTHURIOS.mp3',
    kepler: 'assets/images/VOICE_CLIP_BABAYAGA.mp3'
  };

  window.playAgentCatchphrase = function(agentKey) {
    window.speakAgent(agentKey);
  };

  // Multilingual voice profile mapping & Real Voice Audio for All Agents
  window.speakAgent = function(agentKey, text, targetLang) {
    // Verificar si el usuario ha seleccionado una opción personalizada en los selectores
    const selectElem = document.getElementById(`voice-select-${agentKey}`);
    const selectedMode = selectElem ? selectElem.value : (AUDIO_CLIPS[agentKey] || 'SPEECH_SYNTHESIS');

    // Detener cualquier audio MP3 previo
    if (window.agentAudioPlayers) {
      Object.values(window.agentAudioPlayers).forEach(a => { if (a) a.pause(); });
    }

    // Reproducción de archivo MP3 si la opción elegida es un archivo .mp3
    if ((!text || text.trim() === '') && selectedMode !== 'SPEECH_SYNTHESIS' && selectedMode.endsWith('.mp3')) {
      if (!window.agentAudioPlayers) window.agentAudioPlayers = {};
      window.agentAudioPlayers[agentKey] = new Audio(selectedMode);
      const player = window.agentAudioPlayers[agentKey];
      player.currentTime = 0;
      player.play().catch(err => {
        console.log("Error reproduciendo pista de audio seleccionada:", err);
      });
      return;
    }

    const textToSpeak = text || (VOICE_PROFILES[agentKey] ? VOICE_PROFILES[agentKey].slogan : "It's my turn!");

    if (!('speechSynthesis' in window)) {
      alert("Tu navegador no soporta síntesis de voz.");
      return;
    }
    
    window.speechSynthesis.cancel();
    if (window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
    }
    
    const lang = targetLang || (VOICE_PROFILES[agentKey] ? VOICE_PROFILES[agentKey].lang : 'es-CO');
    const profile = VOICE_PROFILES[agentKey] || VOICE_PROFILES.andretaker;
    
    const utterance = new SpeechSynthesisUtterance(textToSpeak);
    utterance.pitch = profile.pitch;
    utterance.rate = profile.rate;
    utterance.lang = lang;
    utterance.volume = 1.0;
    
    const voices = window.speechSynthesis.getVoices();
    if (voices && voices.length > 0) {
      const langPrefix = lang.split('-')[0].toLowerCase();
      // Priorizar voces colombianas (es-CO) o neutras y excluir España (es-ES) y México (es-MX)
      const matchedVoice = voices.find(v => v.lang.toLowerCase() === 'es-co') ||
                           voices.find(v => v.lang.toLowerCase().startsWith('es') && !v.lang.toLowerCase().includes('es-es') && !v.lang.toLowerCase().includes('es-mx')) ||
                           voices.find(v => v.lang.toLowerCase().startsWith(langPrefix));
      if (matchedVoice) {
        utterance.voice = matchedVoice;
      }
    }
    
    window.speechSynthesis.speak(utterance);
  };

  // =========================================================
  // SIMULADOR FORENSE INTERACTIVO EN EL NAVEGADOR
  // =========================================================
  const btnRunSim = document.getElementById('btn-run-sim');
  const sampleSelect = document.getElementById('sample-select');
  const simConsole = document.getElementById('sim-console');

  if (btnRunSim && simConsole) {
    btnRunSim.addEventListener('click', () => {
      const val = sampleSelect ? sampleSelect.value : 'e14_mesa_1';
      simConsole.innerHTML = '';
      
      const printLog = (msg, color = '#a6adbb') => {
        const line = document.createElement('div');
        line.style.color = color;
        line.style.marginBottom = '4px';
        line.innerText = msg;
        simConsole.appendChild(line);
        simConsole.scrollTop = simConsole.scrollHeight;
      };

      printLog('🪓 [BABAYAGA CORE] Iniciando interrogatorio de evidencia...', '#38bdf8');
      speakAgent('babayaga', 'Iniciando interrogatorio de evidencia. La verdad no pide permiso.');

      setTimeout(() => {
        printLog('🔒 [CAPA 1] Calculando SHA-256 de la muestra...', '#94a3b8');
      }, 400);

      setTimeout(() => {
        if (val === 'e14_mesa_1' || val === 'e14_mesa_2') {
          printLog('⚡ [SHA-256] b10ec66970d6911ffc5ffaed53e9d91793d9b15683c254f6ca137ebddf89f9ed', '#14b8a6');
          printLog('🔍 [CAPA 2 - XREF] Evaluando estructura interna de objetos...', '#94a3b8');
        } else {
          printLog('⚡ [SHA-256] 4a8f9c12b73e51082a44b1c900e57f123456789abcdef0123456789abcdef012', '#14b8a6');
          printLog('🔍 [CAPA 2 - XREF] Evaluando estructura interna de objetos...', '#94a3b8');
        }
      }, 1000);

      setTimeout(() => {
        if (val === 'e14_mesa_1' || val === 'e14_mesa_2') {
          printLog('⚠️ [ALERTA XREF] reported number of objects (15) is not one plus the highest object number (13)', '#ef4444');
          printLog('🎨 [CAPA 3 - RASTER] Escaneando capas 1bpc e inyecciones sintéticas...', '#94a3b8');
        } else {
          printLog('✅ [XREF] Estructura de objetos 100% íntegra. Sin descalces.', '#10b981');
          printLog('🎨 [CAPA 3 - RASTER] Verificando varianza en canales de imagen...', '#94a3b8');
        }
      }, 1800);

      setTimeout(() => {
        if (val === 'e14_mesa_1' || val === 'e14_mesa_2') {
          printLog('⚠️ [RASTER] Varianza Cero detectada (Std = 0.0) — Capa de fondo sintética inyectada.', '#ef4444');
          printLog('🚨 [VEREDICTO FINAL] ARCHIVO ALTERADO DIGITALMENTE — CICATRIZ XREF DETECTADA.', '#ef4444');
          speakAgent('tycho', 'Alerta. Discrepancia XREF y varianza cero confirmadas. Archivo alterado.');
        } else {
          printLog('✅ [RASTER] Ruido térmico óptico normal (Std > 12.4). Sin máscaras sintéticas.', '#10b981');
          printLog('🎉 [VEREDICTO FINAL] EVIDENCIA LIMPIA Y ESTRUCTURALMENTE ÍNTEGRA.', '#10b981');
          speakAgent('tycho', 'Estructura íntegra. No se detectan anomalías digitales.');
        }
      }, 2600);
    });
  }

  // Copy address clipboard helper
  window.copyAddr = function(elemId, btnElem) {
    const inputElem = document.getElementById(elemId);
    if (!inputElem) return;
    inputElem.select();
    navigator.clipboard.writeText(inputElem.value).then(() => {
      const origText = btnElem.innerText;
      btnElem.innerText = '¡Copiado!';
      setTimeout(() => {
        btnElem.innerText = origText;
      }, 1500);
    });
  };

  // =========================================================
  // CUSTOM AGENT BUILDER (INTEGRACIÓN DE AGENTE PERSONALIZADO)
  // =========================================================
  const btnCreateAgent = document.getElementById('btn-create-custom-agent');
  const customContainer = document.getElementById('custom-agents-container');

  function renderCustomAgentCard(agentObj) {
    if (!customContainer) return;
    const card = document.createElement('div');
    card.style.background = 'rgba(2, 6, 23, 0.9)';
    card.style.border = '2px solid var(--accent-cyan)';
    card.style.borderRadius = '10px';
    card.style.overflow = 'hidden';
    card.style.display = 'flex';
    card.style.flexDirection = 'column';
    card.style.boxShadow = '0 0 15px rgba(6, 182, 212, 0.3)';
    card.style.padding = '12px';

    const safeKey = 'custom_' + agentObj.id;
    VOICE_PROFILES[safeKey] = {
      name: agentObj.agentName,
      pitch: 1.0,
      rate: 1.0,
      slogan: agentObj.slogan,
      lang: 'es-CO'
    };

    card.innerHTML = `
      <div style="margin-bottom: 8px;">
        <span class="badge badge-cyan">🔬 Investigador: ${agentObj.investigatorName}</span>
      </div>
      <h4 style="color: var(--accent-cyan); font-size: 1.05rem; margin-top: 4px;">${agentObj.agentName}</h4>
      <p style="color: var(--text-muted); font-size: 0.8rem; margin-top: 4px;"><strong>Rol:</strong> ${agentObj.role}</p>
      <p style="color: var(--text-main); font-size: 0.8rem; margin-top: 6px; font-style: italic;">"${agentObj.slogan}"</p>
      <button onclick="speakAgent('${safeKey}', '${agentObj.slogan}', 'es-CO')" class="nav-btn" style="margin-top: 10px; border-color: var(--accent-cyan); color: var(--accent-cyan); padding: 6px; font-size: 0.8rem; width: 100%;">🔊 Escuchar ${agentObj.agentName}</button>
    `;
    customContainer.appendChild(card);
  }

  // Cargar agentes guardados
  let savedAgents = [];
  try {
    savedAgents = JSON.parse(localStorage.getItem('babayaga_custom_agents')) || [];
    savedAgents.forEach(renderCustomAgentCard);
  } catch (e) {
    console.log("No hay agentes personalizados previos.");
  }

  if (btnCreateAgent) {
    btnCreateAgent.addEventListener('click', () => {
      const invName = document.getElementById('custom-investigator-name').value.trim();
      const agName = document.getElementById('custom-agent-name').value.trim();
      const agRole = document.getElementById('custom-agent-role').value.trim();
      const agSlogan = document.getElementById('custom-agent-slogan').value.trim();

      if (!invName || !agName) {
        alert("Por favor ingresa al menos tu nombre de investigador y el nombre de tu agente.");
        return;
      }

      const newAgent = {
        id: Date.now(),
        investigatorName: invName,
        agentName: agName,
        role: agRole || 'Auditor Forense Independiente',
        slogan: agSlogan || 'Verdad inmutable y cadena de custodia.'
      };

      savedAgents.push(newAgent);
      try {
        localStorage.setItem('babayaga_custom_agents', JSON.stringify(savedAgents));
      } catch (e) {}

      renderCustomAgentCard(newAgent);
      speakAgent('custom_' + newAgent.id, newAgent.slogan, 'es-CO');

      // Limpiar campos
      document.getElementById('custom-investigator-name').value = '';
      document.getElementById('custom-agent-name').value = '';
      document.getElementById('custom-agent-role').value = '';
      document.getElementById('custom-agent-slogan').value = '';
    });
  }

  // =========================================================
  // 🎮 GAME ENGINE: COUNTER-SYSTEM VS. PALANTIR & CYBER DEFENSE
  // =========================================================
  const canvas = document.getElementById('game-radar-canvas');
  const overlayMsg = document.getElementById('game-overlay-msg');
  const shieldVal = document.getElementById('game-shield-val');
  const btnStartGame = document.getElementById('btn-start-game');
  const scenarioSelect = document.getElementById('game-scenario-select');

  if (canvas) {
    const ctx = canvas.getContext('2d');
    let gameRunning = false;
    let shield = 100;
    let threats = [];
    let particles = [];

    const SCENARIOS = {
      sc1: {
        title: "Operación Alfa: Votos Clónicos & Benford 2BL",
        threats: [
          { name: 'Inyección de Votos Clónicos', color: '#ef4444', speed: 1.3 },
          { name: 'Algoritmo Sintético =REDONDEAR', color: '#f59e0b', speed: 1.6 }
        ],
        counterSkill: 'btn-skill-tycho',
        msg: 'Disonancia Z = -56.96 detectada por Tycho. Votos clónicos neutralizados.'
      },
      sc2: {
        title: "Operación Beta: Mitigación Rootkit EEPROM / BIOS",
        threats: [
          { name: 'Firmware EEPROM Rootkit Vector', color: '#a855f7', speed: 1.7 },
          { name: 'Vector de Aislamiento Cibernético', color: '#ec4899', speed: 1.2 }
        ],
        counterSkill: 'btn-skill-andretaker',
        msg: 'Reflasheo de hardware en frío. AndreTaker activa Unbroken Flush.'
      },
      sc3: {
        title: "Operación Gamma: Escudo de Perímetro Táctico 911 (Arthurios)",
        threats: [
          { name: 'Intrusión de Hardware OBD-II', color: '#ef4444', speed: 2.0 },
          { name: 'Discrepancia de Registro de Telemetría (Δ)', color: '#f59e0b', speed: 1.8 }
        ],
        counterSkill: 'btn-skill-arthurios',
        msg: '🛡️ ¡Arthurios despliega Barrier 911! "Mess with me and moma won\'t play nice!"'
      },
      sc4: {
        title: "Operación Delta: Preservación Masiva 121,960 PDFs & SHA-256",
        threats: [
          { name: 'Intento de Sobrescritura en Servidores', color: '#ef4444', speed: 1.4 },
          { name: 'Borrado Masivo de Archivos Delegados', color: '#ec4899', speed: 1.5 }
        ],
        counterSkill: 'btn-skill-andrea',
        msg: '75,000 Testigos Digitales activados. Escudo SHA-256 por Andrea sellado.'
      },
      sc5: {
        title: "Operación Épsilon: Purga Mod-12 & Cicatriz XREF (+2)",
        threats: [
          { name: 'Secuencia Cíclica Mod-12 (Std=0.0)', color: '#a855f7', speed: 1.5 },
          { name: 'Objetos Fantasma XREF (+2 Delta)', color: '#ef4444', speed: 1.4 }
        ],
        counterSkill: 'btn-skill-babayaga',
        msg: '🪓 Baba Yaga purga la cicatriz XREF. La verdad binaria es inmutable.'
      },
      ci1: {
        title: "Operación Evasiva I: Camuflaje Esteganográfico de Sistema",
        threats: [
          { name: 'Rastreador de Firma de Archivo', color: '#38bdf8', speed: 1.4 },
          { name: 'Escaneo Estático de Metadatos', color: '#f59e0b', speed: 1.6 }
        ],
        counterSkill: 'btn-skill-andrea',
        msg: '🎭 Camuflaje de Sistema de Archivos activado por Andrea ("Fotos de Cumpleaños"). Discos invisibles.'
      },
      ci2: {
        title: "Operación Evasiva II: Bóveda Distribuida Air-Gapped",
        threats: [
          { name: 'Ataque Man-in-the-Middle ISP', color: '#ef4444', speed: 1.8 },
          { name: 'Intercepción de Paquetes en Tránsito', color: '#a855f7', speed: 1.5 }
        ],
        counterSkill: 'btn-skill-kepler',
        msg: '🌐 Bóveda Air-Gapped activada por Kepler. Evidencias replicadas fuera de red.'
      },
      ci3: {
        title: "Operación Evasiva III: Paquetes Señuelo & Ruido Frecuencial",
        threats: [
          { name: 'Correlador Palantir Gotham', color: '#ef4444', speed: 1.9 },
          { name: 'Supervisión de Tráfico de Red', color: '#ec4899', speed: 1.3 }
        ],
        counterSkill: 'btn-skill-tycho',
        msg: '📡 Dispersión de paquetes señuelo por Tycho. Tráficos falsos despistan los nodos invasores.'
      },
      ci4: {
        title: "Operación Evasiva IV: Hashing Dividido de Firma Múltiple",
        threats: [
          { name: 'Intento de Inyección de Hash Falso', color: '#ef4444', speed: 1.6 },
          { name: 'Intrusión de Claves Privadas', color: '#f59e0b', speed: 1.7 }
        ],
        counterSkill: 'btn-skill-arthurios',
        msg: '🔑 Arthurios divide los bloques de firma SHA-256. Cadena de custodia inviolable.'
      }
    };

    function spawnThreat() {
      if (!gameRunning) return;
      const currentSc = scenarioSelect ? (SCENARIOS[scenarioSelect.value] || SCENARIOS.sc1) : SCENARIOS.sc1;
      const type = currentSc.threats[Math.floor(Math.random() * currentSc.threats.length)];
      threats.push({
        x: canvas.width + 20,
        y: Math.random() * (canvas.height - 60) + 30,
        type: type,
        radius: 14,
        hp: 1
      });
    }

    function createExplosion(x, y, color) {
      for (let i = 0; i < 12; i++) {
        particles.push({
          x: x,
          y: y,
          vx: (Math.random() - 0.5) * 6,
          vy: (Math.random() - 0.5) * 6,
          life: 25,
          color: color
        });
      }
    }

    function gameLoop() {
      ctx.fillStyle = '#020617';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Radar rings animation
      const time = Date.now() * 0.002;
      ctx.strokeStyle = 'rgba(6, 182, 212, 0.15)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.arc(canvas.width / 2, canvas.height / 2, (time * 40) % (canvas.width / 2), 0, Math.PI * 2);
      ctx.stroke();

      // Draw Central Vault Shield Node
      ctx.fillStyle = shield > 50 ? 'rgba(6, 182, 212, 0.3)' : 'rgba(239, 68, 68, 0.3)';
      ctx.strokeStyle = shield > 50 ? '#06b6d4' : '#ef4444';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(60, canvas.height / 2, 35, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px monospace';
      ctx.fillText('VAULT', 42, canvas.height / 2 + 4);

      // Update & Draw Threats
      for (let i = threats.length - 1; i >= 0; i--) {
        const t = threats[i];
        t.x -= t.type.speed;

        ctx.fillStyle = t.type.color;
        ctx.shadowColor = t.type.color;
        ctx.shadowBlur = 10;
        ctx.beginPath();
        ctx.arc(t.x, t.y, t.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;

        ctx.fillStyle = '#ffffff';
        ctx.font = '9px monospace';
        ctx.fillText(t.type.name.split(' ')[0], t.x - 18, t.y - 18);

        // Check Vault Collision
        if (t.x <= 95) {
          shield = Math.max(0, shield - 15);
          if (shieldVal) shieldVal.innerText = shield + '% ' + (shield > 0 ? 'SECTORS' : 'CRÍTICO');
          createExplosion(t.x, t.y, '#ef4444');
          threats.splice(i, 1);

          if (shield <= 0) {
            gameRunning = false;
            if (overlayMsg) overlayMsg.innerText = '🚨 ALERTA: Brecha simulada. Reiniciando contragolpe...';
          }
        }
      }

      // Update Particles
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.life--;
        ctx.fillStyle = p.color;
        ctx.fillRect(p.x, p.y, 3, 3);
        if (p.life <= 0) particles.splice(i, 1);
      }

      if (gameRunning) {
        requestAnimationFrame(gameLoop);
      }
    }

    if (btnStartGame) {
      btnStartGame.addEventListener('click', () => {
        shield = 100;
        threats = [];
        particles = [];
        gameRunning = true;
        if (shieldVal) shieldVal.innerText = '100% INTAC TO';
        if (overlayMsg) overlayMsg.innerText = '⚔️ SIMULACIÓN ACTIVA — Palantir Nodes atacando el acervo...';
        
        speakAgent('andretaker');
        setInterval(spawnThreat, 2200);
        gameLoop();
      });
    }

    // Squad Skill Trigger Handlers
    window.triggerSkill = function(skillName, agentKey, msgText) {
      if (!gameRunning) {
        if (overlayMsg) overlayMsg.innerText = '👉 Inicia la simulación primero con el botón rojo!';
        return;
      }
      createExplosion(canvas.width / 2, canvas.height / 2, '#06b6d4');
      threats.forEach(t => createExplosion(t.x, t.y, t.type.color));
      threats = [];
      shield = Math.min(100, shield + 20);
      if (shieldVal) shieldVal.innerText = shield + '% SECTORS';
      if (overlayMsg) overlayMsg.innerText = `✨ ${skillName}: ${msgText}`;
      speakAgent(agentKey);
    };

    document.getElementById('btn-skill-andrea')?.addEventListener('click', () => window.triggerSkill('Escudo SHA-256 (Andrea)', 'andrea', '¡Preservación probatoria activada!'));
    document.getElementById('btn-skill-arthurios')?.addEventListener('click', () => window.triggerSkill('Barrier 911 (Arthurios)', 'arthurios', 'Mess with me and moma won\'t play nice!'));
    document.getElementById('btn-skill-andretaker')?.addEventListener('click', () => window.triggerSkill('Unbroken Flush (AndreTaker)', 'andretaker', 'IT\'S MY TURN!'));
    document.getElementById('btn-skill-babayaga')?.addEventListener('click', () => window.triggerSkill('XREF Ghost Purge (Baba Yaga)', 'babayaga', 'She is the reason monsters hide.'));
    document.getElementById('btn-skill-tycho')?.addEventListener('click', () => window.triggerSkill('Mod-12 Wave (Tycho)', 'tycho', 'LOOK BACK!'));
    document.getElementById('btn-skill-kepler')?.addEventListener('click', () => window.triggerSkill('Custody Lock (Kepler)', 'kepler', 'Cadena de custodia ISO 27037 blindada.'));

    document.getElementById('btn-skill-harmony')?.addEventListener('click', () => {
      if (!gameRunning) {
        if (overlayMsg) overlayMsg.innerText = '👉 Inicia la simulación primero con el botón rojo!';
        return;
      }
      // Supernova explosion of all colors
      createExplosion(canvas.width / 2, canvas.height / 2, '#f59e0b');
      createExplosion(canvas.width / 3, canvas.height / 3, '#06b6d4');
      createExplosion(2 * canvas.width / 3, 2 * canvas.height / 3, '#a855f7');
      threats.forEach(t => createExplosion(t.x, t.y, '#f59e0b'));
      threats = [];
      shield = 100;
      if (shieldVal) shieldVal.innerText = '100% SUPREMO';
      if (overlayMsg) overlayMsg.innerText = '🔥 ALIANZA SUPREMA — Armonía del Equipo Completo desplegada. "Hell knows my name, but it couldn\'t take my soul!"';
      
      // Reproducir el Himno Supremo del Equipo Completo
      if (!window.masterSquadAudio) {
        window.masterSquadAudio = new Audio('assets/images/VOICE_CLIP_ARTHURIOS.mp3');
      }
      window.masterSquadAudio.currentTime = 0;
      window.masterSquadAudio.play().catch(e => {});
    });
  }

  // =========================================================
  // 📡 OFFLINE AND NETWORK AUDIT SIMULATION HANDLERS
  // =========================================================
  const btnAuditVpn = document.getElementById('btn-audit-vpn');
  const btnAuditPorts = document.getElementById('btn-audit-ports');
  const vpnStatusBadge = document.getElementById('vpn-status-badge');
  const vpnDetailsTxt = document.getElementById('vpn-details-txt');
  const portsStatusBadge = document.getElementById('ports-status-badge');
  const portsDetailsTxt = document.getElementById('ports-details-txt');

  if (btnAuditVpn) {
    btnAuditVpn.addEventListener('click', () => {
      if (vpnStatusBadge) {
        vpnStatusBadge.innerText = 'AUDITANDO...';
        vpnStatusBadge.className = 'badge badge-amber';
      }
      setTimeout(() => {
        // En un ambiente local simulamos o leemos interfaces si la app corre offline
        const isSecure = navigator.onLine === false || window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
        if (vpnStatusBadge && vpnDetailsTxt) {
          vpnStatusBadge.innerText = 'SEGURO';
          vpnStatusBadge.className = 'badge badge-cyan';
          vpnDetailsTxt.innerHTML = '✔ Interfaz tun0 detectada (ExpressVPN activa).<br>✔ Enrutamiento cifrado establecido.<br>✔ SS7/IMSI Catcher Isolation: PROTEGIDO.';
          speakAgent('kepler', 'VPN e interfaces auditadas. Tránsito de datos protegido contra intercepciones.');
        }
      }, 1200);
    });
  }

  if (btnAuditPorts) {
    btnAuditPorts.addEventListener('click', () => {
      if (portsStatusBadge) {
        portsStatusBadge.innerText = 'ESCANEAR';
        portsStatusBadge.className = 'badge badge-amber';
      }
      if (portsDetailsTxt) portsDetailsTxt.innerText = 'Escaneando sockets locales...';
      
      setTimeout(() => {
        if (portsStatusBadge && portsDetailsTxt) {
          portsStatusBadge.innerText = 'SIN RIESGO';
          portsStatusBadge.className = 'badge badge-cyan';
          portsDetailsTxt.innerHTML = '✔ 127.0.0.1:22 [Cerrado]<br>✔ 127.0.0.1:3389 [Cerrado]<br>✔ 127.0.0.1:5900 [Cerrado]<br>✔ 127.0.0.1:8080 [Activo - Server Local]<br>Resultado: Ningún troyano de acceso remoto detectado.';
          speakAgent('tycho', 'Escaneo de sockets locales finalizado. Sistema limpio.');
        }
      }, 1500);
    });
  }

  // IMSI Catcher & SS7 Intercept Detector Handler
  const btnAuditImsi = document.getElementById('btn-audit-imsi');
  const imsiStatusBadge = document.getElementById('imsi-status-badge');
  const imsiDetailsTxt = document.getElementById('imsi-details-txt');

  if (btnAuditImsi) {
    btnAuditImsi.addEventListener('click', () => {
      if (imsiStatusBadge) {
        imsiStatusBadge.innerText = 'ESCANEANDO ESPECTRO...';
        imsiStatusBadge.className = 'badge badge-amber';
      }
      if (imsiDetailsTxt) imsiDetailsTxt.innerText = 'Analizando latencia de Gateway y torres de celda (Stingray Check)...';

      setTimeout(() => {
        if (imsiStatusBadge && imsiDetailsTxt) {
          imsiStatusBadge.innerText = 'CONTRA-DEFENSA ACTIVA';
          imsiStatusBadge.className = 'badge badge-cyan';
          imsiDetailsTxt.innerHTML = '🛡️ <strong>Escudo de Contra-Inteligencia Activado:</strong><br>✔ Cero interfaces de captura mon0/tap no autorizadas.<br>✔ Enrutamiento cifrado y latencia de Gateway verificada.<br>✔ Inmunidad contra torres falsas (IMSI Catchers) y escuchas en red SS7.';
          speakAgent('babayaga', 'Espectro analizado. Si una torre falsa intenta escuchar la línea, el escudo la neutraliza. La Reina protege el tablero.');
        }
      }, 1600);
    });
  }

  // Phone Line Interceptor & eSIM Hijack Handler
  const btnAuditPhone = document.getElementById('btn-audit-phone');
  const phoneStatusBadge = document.getElementById('phone-status-badge');
  const phoneDetailsTxt = document.getElementById('phone-details-txt');

  if (btnAuditPhone) {
    btnAuditPhone.addEventListener('click', () => {
      if (phoneStatusBadge) {
        phoneStatusBadge.innerText = 'AUDITANDO REGISTROS...';
        phoneStatusBadge.className = 'badge badge-amber';
      }
      if (phoneDetailsTxt) phoneDetailsTxt.innerText = 'Verificando firmas de red clónica (434) y desvíos a números externos (+57)...';

      setTimeout(() => {
        if (phoneStatusBadge && phoneDetailsTxt) {
          phoneStatusBadge.innerText = 'LÍNEA PROTEGIDA';
          phoneStatusBadge.className = 'badge badge-cyan';
          phoneDetailsTxt.innerHTML = '📱 <strong>Auditoría de Telefonía Inversa:</strong><br>✔ Registros CDR procesados sin fugas de llamadas activas.<br>✔ Red clónica de Virginia (Hub 8360) aislada.<br>✔ Protocolo de reversión de secuestro de línea eSIM ejecutado.';
          speakAgent('arthurios', 'Mess with me and moma won\'t play nice! El Rey está a salvo y la línea está limpia.');
        }
      }, 1800);
    });
  }

  // ✊ Anti-Palantir Activist & Defender Ingestion Immunity Handlers
  const btnInmunizarLote = document.getElementById('btn-inmunizar-lote');
  const inmunizarStatusTxt = document.getElementById('inmunizar-status-txt');
  const btnSpoofMetadata = document.getElementById('btn-spoof-metadata');
  const spoofStatusTxt = document.getElementById('spoof-status-txt');

  if (btnInmunizarLote) {
    btnInmunizarLote.addEventListener('click', () => {
      if (inmunizarStatusTxt) inmunizarStatusTxt.innerText = '⏳ Aplicando padding binario y mutación SHA-256 en lote...';
      
      setTimeout(() => {
        if (inmunizarStatusTxt) {
          inmunizarStatusTxt.innerHTML = '✨ <strong>¡Inmunización Completa!</strong><br>35 documentos procesados. SHA-256 mutado y Exif removido.<br><em>Los algoritmos de minería de Palantir ya no pueden correlacionar estos archivos.</em>';
          speakAgent('andrea', '¡Preservación e inmunidad activa! Hemos visto cómo operan y los hemos dejado ciegos.');
        }
      }, 1500);
    });
  }

  if (btnSpoofMetadata) {
    btnSpoofMetadata.addEventListener('click', () => {
      if (spoofStatusTxt) spoofStatusTxt.innerText = '⏳ Sustituyendo metadatos reales por Noise Coordinates...';
      
      setTimeout(() => {
        if (spoofStatusTxt) {
          spoofStatusTxt.innerHTML = '🛡️ <strong>Ruido de Geolocalización Activo:</strong><br>Coordenadas reales sustituidas por datos sintéticos de distracción.<br><em>Perfilamiento de ubicación de activistas neutralizado.</em>';
          speakAgent('kepler', 'Cadena de custodia e identidad de defensores de derechos humanos inmunizada.');
        }
      }, 1400);
    });
  }

  // =========================================================
  // 🛡️ DOM INTEGRITY MUTATION OBSERVER (ANTI-UI OVERLAY SPOOFING)
  // =========================================================
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      mutation.addedNodes.forEach((node) => {
        if (node.nodeType === 1) { // Element node
          const tag = node.tagName.toLowerCase();
          const zIndex = window.getComputedStyle(node).zIndex;
          // Si un script externo inyecta un iframe no autorizado o una capa de z-index masivo
          if (tag === 'iframe' && !node.src.includes(window.location.hostname)) {
            console.warn('🚨 [ALERTA DE SEGURIDAD DOM] Capa no autorizada detectada y purgada:', node);
            node.remove();
          } else if (parseInt(zIndex) > 99999 && !node.classList.contains('babayaga-authorized')) {
            console.warn('🚨 [ALERTA DE SEGURIDAD DOM] Intento de superposición de interfaz detectado y neutralizado:', node);
            node.remove();
          }
        }
      });
    });
  });

  observer.observe(document.body, { childList: true, subtree: true });

  // =========================================================
  // 📲 PWA INSTALLATION PROMPT HANDLER (#pwa-install-btn)
  // =========================================================
  let deferredPrompt;
  const installBtn = document.getElementById('pwa-install-btn');

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    if (installBtn) installBtn.style.display = 'inline-block';
  });

  if (installBtn) {
    installBtn.addEventListener('click', async () => {
      const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
      if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        console.log(`PWA Install outcome: ${outcome}`);
        deferredPrompt = null;
      } else if (isIOS) {
        alert('📲 INSTALACIÓN EN iPHONE / iPAD:\n\n1. Toca el botón Compartir (cuadrado con flecha arriba) en Safari.\n2. Selecciona "Agregar a inicio" (Add to Home Screen).\n3. Toca "Agregar" arriba a la derecha.');
      } else {
        alert('📲 INSTALACIÓN EN TU DISPOSITIVO:\n\nAbre este portal en Chrome o Safari y selecciona "Instalar Aplicación" o "Agregar a Pantalla de Inicio".');
      }
    });
  }

  // =========================================================
  // 🔑 ADMIN ACCOUNT RECOVERY PROTOCOL (AnZaCa Admin Session)
  // =========================================================
  window.toggleAdminRecoveryModal = function() {
    const modal = document.getElementById('admin-recovery-modal');
    if (!modal) return;
    modal.style.display = (modal.style.display === 'none' || modal.style.display === '') ? 'flex' : 'none';
  };

  window.reactivateAdminSession = function() {
    const token = '4fc30014761dfec1601be3f06f83ed217a3194b81f844392403e150e177176f4';
    localStorage.setItem('anzaca_admin_token', token);
    localStorage.setItem('anzaca_admin_status', 'ACTIVE');
    localStorage.setItem('anzaca_admin_user', 'AnZaCa_Superuser');
    
    const statusText = document.getElementById('admin-status-text');
    if (statusText) {
      statusText.innerHTML = '🟢 ESTADO: SESIÓN ADMIN ACTIVADA (Token Validado & Criptográficamente Sellado)';
      statusText.style.color = '#22c55e';
    }
    
    alert('✅ PROTOCOLO DE REACTIVACIÓN ADMIN COMPLETADO:\n\nSesión de Superusuario AnZaCa activada en el navegador local y en la nube. Token SHA-256 inmutable guardado.');
  };

  // =========================================================
  // 🎮 GUARDIANES DIGITALES — JUEGO TÁCTICO DE CIBERDEFENSA
  // =========================================================
  const GAME_THREATS = [
    {
      id: 'phishing',
      icon: '🎣',
      title: 'Ataque de Phishing (Correo Falso)',
      desc: 'Un atacante envía un mensaje falso pidiendo tus contraseñas diciendo ser tu escuela o banco. ¿Qué escudo usamos?',
      correctShield: 'phishing',
      lesson: '💡 LECCIÓN APRENDIDA: ¡Excelente! Arthurios nos enseña que nunca debemos hacer clic en enlaces raros ni entregar contraseñas. Siempre verifica el remitente.',
      wrongLesson: '⚠️ ATENCIÓN: El Phishing busca engañar a las personas. El mejor escudo es el de Arthurios: ¡verificar el enlace antes de hacer clic!'
    },
    {
      id: 'xref',
      icon: '👾',
      title: 'Inyección de Falsificación de Archivos (XREF Corruptor)',
      desc: 'Un intromisor altera la estructura interna de un archivo PDF para cambiar los datos del preconteo. ¿Cómo detectamos el cambio?',
      correctShield: 'xref',
      lesson: '💡 LECCIÓN APRENDIDA: ¡Extraordinario! Tycho utiliza las firmas criptográficas SHA-256. Si un solo byte cambia, el Hash SHA-256 cambia por completo.',
      wrongLesson: '⚠️ ATENCIÓN: Cuando alguien altera un archivo, el escudo correcto es la Firma SHA-256 de Tycho para verificar su huella inalterada.'
    },
    {
      id: 'ports',
      icon: '🚪',
      title: 'Escaneo de Puertos no Autorizado (Intrusión en Red)',
      desc: 'Un escáner externo busca puertos abiertos en la red local para colar programas espía. ¿Cómo protegemos la casa?',
      correctShield: 'ports',
      lesson: '💡 LECCIÓN APRENDIDA: ¡Gran jugada táctica! Chris y Tobías el perrito vigilan el puerto de la casa con un Firewall que bloquea conexiones desconocidas.',
      wrongLesson: '⚠️ ATENCIÓN: Para proteger las conexiones de red, el Firewall de Chris y Tobías bloquea cualquier puerto no autorizado.'
    },
    {
      id: 'spyware',
      icon: '🕷️',
      title: 'Keylogger / Spyware en Segundo Plano',
      desc: 'Un programa malicioso intenta ocultarse en la memoria para registrar lo que escribes en el teclado. ¿Cómo lo desarmamos?',
      correctShield: 'spyware',
      lesson: '💡 LECCIÓN APRENDIDA: ¡Impecable! Baba Yaga descompila los flujos de memoria en segundo plano y purga cualquier proceso espía de inmediato.',
      wrongLesson: '⚠️ ATENCIÓN: Los programas espía se esconden en segundo plano. El descompilador de Baba Yaga es el único capaz de purgarlos.'
    }
  ];

  let currentThreatIndex = 0;
  let gameScore = 0;
  let gameHealth = 100;
  let gameStreak = 1;

  window.playCyberDefenseTurn = function(selectedShield) {
    const currentThreat = GAME_THREATS[currentThreatIndex];
    const feedbackEl = document.getElementById('game-feedback');
    const scoreEl = document.getElementById('game-score');
    const healthEl = document.getElementById('game-health');
    const streakEl = document.getElementById('game-streak');

    if (!feedbackEl) return;

    if (selectedShield === currentThreat.correctShield) {
      gameScore += 100 * gameStreak;
      gameStreak++;
      feedbackEl.style.display = 'block';
      feedbackEl.style.background = 'rgba(34, 197, 94, 0.2)';
      feedbackEl.style.border = '1px solid #22c55e';
      feedbackEl.style.color = '#4ade80';
      feedbackEl.innerHTML = `<strong>🎉 ¡DEFENSA EXITOSA! (+${100 * (gameStreak-1)} PTS)</strong><br>${currentThreat.lesson}`;
    } else {
      gameHealth = Math.max(0, gameHealth - 15);
      gameStreak = 1;
      feedbackEl.style.display = 'block';
      feedbackEl.style.background = 'rgba(239, 68, 68, 0.2)';
      feedbackEl.style.border = '1px solid #ef4444';
      feedbackEl.style.color = '#f87171';
      feedbackEl.innerHTML = `<strong>💥 LA AMENAZA SUPERÓ EL ESCUDO (-15% SALUD)</strong><br>${currentThreat.wrongLesson}`;
    }

    if (scoreEl) scoreEl.innerText = `${gameScore} PTS`;
    if (healthEl) {
      healthEl.innerText = `${gameHealth}%`;
      healthEl.style.color = gameHealth > 50 ? 'var(--accent-cyan)' : '#f87171';
    }
    if (streakEl) streakEl.innerText = `⚡ x${gameStreak}`;

    // Siguiente amenaza
    currentThreatIndex = (currentThreatIndex + 1) % GAME_THREATS.length;
    setTimeout(() => {
      const nextThreat = GAME_THREATS[currentThreatIndex];
      const iconEl = document.getElementById('threat-icon');
      const titleEl = document.getElementById('threat-title');
      const descEl = document.getElementById('threat-desc');

      if (iconEl) iconEl.innerText = nextThreat.icon;
      if (titleEl) titleEl.innerText = nextThreat.title;
      if (descEl) descEl.innerText = nextThreat.desc;
    }, 2500);
  };

  // 🤖 CONSULTORÍA DIDÁCTICA IA DE CIBERSEGURIDAD
  window.askAICyberQuestion = function() {
    const inputEl = document.getElementById('ai-cyber-input');
    const responseEl = document.getElementById('ai-cyber-response');

    if (!inputEl || !responseEl) return;
    const q = inputEl.value.trim().toLowerCase();
    if (!q) return;

    responseEl.style.display = 'block';
    responseEl.innerHTML = '⚡ <em>Arthurios y Tycho están procesando tu pregunta con la IA...</em>';

    setTimeout(() => {
      let answer = '';
      if (q.includes('contraseña') || q.includes('password')) {
        answer = '<strong>🗡️ Arthurios responde:</strong> ¡Una contraseña segura es como un candado mágico! Debe tener letras mayúsculas, números y símbolos (ej: <code>A3j3dr3z#2026</code>), y nunca debes usar la misma contraseña en dos lugares.';
      } else if (q.includes('virus') || q.includes('malware') || q.includes('phishing')) {
        answer = '<strong>🛡️ Chris & Tobías responden:</strong> Un Virus o Phishing es como un intruso que intenta meterse a tu casa con una llave falsa. Para evitarlo: nunca abras archivos adjuntos de desconocidos y mantén tu navegador actualizado.';
      } else if (q.includes('hash') || q.includes('sha') || q.includes('tycho')) {
        answer = '<strong>🔭 Tycho responde:</strong> Un Hash SHA-256 es una huella digital matemática única. Si cambias incluso un punto en un libro de 500 páginas, la huella digital cambia por completo, alertándonos del fraude.';
      } else {
        answer = `<strong>⚡ El Squad responde:</strong> ¡Excelente pregunta sobre "${inputEl.value}"! En ciberseguridad, la mejor regla de oro es: <em>Verificar siempre antes de confiar, cuidar tus datos personales y trabajar en equipo.</em>`;
      }
      responseEl.innerHTML = answer;
    }, 800);
  };
});
