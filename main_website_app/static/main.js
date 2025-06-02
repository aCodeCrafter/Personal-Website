// Add listeners for expandable clicks
var list = document.getElementsByClassName("expandable");
for (var i = 0; i < list.length; i++) {
  list[i].addEventListener('click', (e) => {
    e.target.parentElement.querySelector('.content').classList.toggle('visible');
  });
}

// Create particles
const particlesDiv = document.querySelector('.particles');
for (var i = 0; i < 60; i++) {
  const particle = document.createElement('div');
  particle.classList.add('particle');
  particle.style.left = (Math.random()*100 - 30)+"%";
  particle.style.animationDelay = -(Math.random()*100)+"s";
  particle.style.opacity = Math.random()+0.5;
  particle.style.scale = Math.random()+1;
  particlesDiv.appendChild(particle);
}