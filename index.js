// AndreTaker — BabaYaga Core Portal JavaScript
document.addEventListener('DOMContentLoaded', () => {
  const navBtns = document.querySelectorAll('.nav-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.getAttribute('data-tab');

      navBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      document.getElementById(tabId).classList.add('active');
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
      // Get target coordinate
      const targetLeft = node.style.left;
      const targetTop = node.style.top;
      
      // Move avatar
      avatar.style.left = targetLeft;
      avatar.style.top = targetTop;

      // Update active states
      nodes.forEach(n => n.classList.remove('active'));
      node.classList.add('active');
      node.classList.add('visited');

      // Update dialog text
      const title = node.getAttribute('data-title');
      const desc = node.getAttribute('data-desc');
      dialogTitle.innerText = title;
      dialogContent.innerText = desc;
    });
  });
});
