// Global Language Switcher (ES / EN / FR)
window.currentLang = 'es';
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
  console.log("Idioma activo:", lang);
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
  const VOICE_PROFILES = {
    babayaga: { name: 'Baba Yaga', pitch: 0.6, rate: 0.9, lang: 'es-ES' },
    tycho: { name: 'Tycho', pitch: 1.2, rate: 1.05, lang: 'es-ES' },
    kepler: { name: 'Kepler', pitch: 1.05, rate: 0.98, lang: 'es-ES' },
    andretaker: { name: 'AndreTaker', pitch: 0.95, rate: 1.0, lang: 'es-ES' }
  };

  // Multilingual voice profile mapping & Real Voice Audio for AndreTaker
  window.speakAgent = function(agentKey, text, targetLang) {
    // Si es AndreTaker, reproducir el archivo de voz real grabado por Andrea (AnZaCa)
    if (agentKey === 'andretaker') {
      if (!window.andreTakerAudio) {
        window.andreTakerAudio = new Audio('00_MUESTRAS_EVIDENCIA/VOCES/VOZ_OFICIAL_ANDRETAKER_ANZACA.mp3');
      }
      window.andreTakerAudio.currentTime = 0;
      window.andreTakerAudio.play().catch(err => {
        console.log("Error al reproducir audio grabado de AndreTaker:", err);
      });
      return;
    }

    if (!('speechSynthesis' in window)) {
      alert("Tu navegador no soporta síntesis de voz.");
      return;
    }
    
    window.speechSynthesis.cancel();
    if (window.speechSynthesis.paused) {
      window.speechSynthesis.resume();
    }
    
    const lang = targetLang || 'es-ES';
    const profile = VOICE_PROFILES[agentKey] || VOICE_PROFILES.andretaker;
    
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.pitch = profile.pitch;
    utterance.rate = profile.rate;
    utterance.lang = lang;
    utterance.volume = 1.0;
    
    const voices = window.speechSynthesis.getVoices();
    if (voices && voices.length > 0) {
      const langPrefix = lang.split('-')[0].toLowerCase();
      const matchedVoice = voices.find(v => v.lang.toLowerCase().startsWith(langPrefix));
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
});
