document.addEventListener("DOMContentLoaded", function() {
    let btnLanzar = document.getElementById("lanzar-btn");
    btnLanzar.addEventListener("click", lanzarProyectil);
  });

function lanzarProyectil() {
    let proyectil = document.querySelector(".proyectil");
    let tiempo = 0;
    let angulo = 45;
    let velocidad = 50;
    let gravedad = 9.8;
  
    let x = 0;
    let y = 0;
  
    let radianes = angulo * Math.PI / 180;
    let velocidadX = velocidad * Math.cos(radianes);
    let velocidadY = velocidad * Math.sin(radianes);
  
    let animacion = setInterval(() => {
      tiempo += 0.1;
  
      x = velocidadX * tiempo;
      y = velocidadY * tiempo - 0.5 * gravedad * Math.pow(tiempo, 2);
  
      proyectil.style.left = x + "px";
      proyectil.style.bottom = y + "px";
  
      if (y < 0) {
        clearInterval(animacion);
      }
    }, 10);
}

