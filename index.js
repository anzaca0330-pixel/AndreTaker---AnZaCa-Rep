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
    nav_chris: "🛡️ Panel de Chris"
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
    nav_chris: "🛡️ Chris Panel"
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
    nav_chris: "🛡️ Panneau de Chris"
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
    arthurios: { name: 'Arthurios', pitch: 1.35, rate: 1.05, slogan: "Mess with me and moma won't play nice!", lang: 'en-US' }
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
    // Si se hace clic en el botón del personaje (sin texto largo), reproducir la voz real del Soundtrack
    if ((!text || text.trim() === '') && AUDIO_CLIPS[agentKey]) {
      if (!window.agentAudioPlayers) window.agentAudioPlayers = {};
      
      // Detener cualquier audio previo
      Object.values(window.agentAudioPlayers).forEach(a => { if (a) a.pause(); });

      const audioSrc = AUDIO_CLIPS[agentKey];
      if (!window.agentAudioPlayers[agentKey]) {
        window.agentAudioPlayers[agentKey] = new Audio(audioSrc);
      }
      const player = window.agentAudioPlayers[agentKey];
      player.currentTime = 0;
      player.play().catch(err => {
        console.log("Error reproduciendo voz real de soundtrack:", err);
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
  }
});
