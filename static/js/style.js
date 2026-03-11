// 导航栏滚动效果
window.addEventListener('scroll', function() {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// 形状动画
const shapes = document.querySelectorAll('.shape');
shapes.forEach((shape, index) => {
  shape.style.transform = `rotate(${Math.random() * 360}deg)`;
  animateShape(shape, index);
});

function animateShape(shape, index) {
  let x = 0, y = 0;
  const speedX = (Math.random() * 0.2 + 0.1) * (index % 2 ? 1 : -1);
  const speedY = (Math.random() * 0.2 + 0.1) * (index % 3 ? 1 : -1);
  
  function move() {
    x += speedX;
    y += speedY;
    shape.style.transform = `translate(${x}px, ${y}px) rotate(${x}deg)`;
    
    const rect = shape.getBoundingClientRect();
    if (rect.left < -100 || rect.right > window.innerWidth + 100) {
      speedX = -speedX;
    }
    if (rect.top < -100 || rect.bottom > window.innerHeight + 100) {
      speedY = -speedY;
    }
    
    requestAnimationFrame(move);
  }
  
  move();
}

// 滚动动画
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate');
    }
  });
}, {
  threshold: 0.1
});

document.querySelectorAll('.floating-card, .glass-card, .food-slide, .collage-item').forEach(el => {
  observer.observe(el);
});