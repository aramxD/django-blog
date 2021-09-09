//Animaciones 
AOS.init();

// Ocultar Menu
let ubicacionPrincipal = window.pageYOffset;

window.addEventListener("scroll", function() {
    let desplazamientoActual = window.pageYOffset;


    if (ubicacionPrincipal >= desplazamientoActual) {
        document.getElementsByTagName("nav")[0].style.top = "0px"
    } else {
        document.getElementsByTagName("nav")[0].style.top = "-100px"
    }


    let delta = ubicacionPrincipal - desplazamientoActual
    console.log(delta)
})


// Menu

let enlacesHeader = document.querySelectorAll(".enlaces-header")[0];
let semaforo = true;

document.querySelectorAll(".boton-menu")[0].addEventListener("click", () => {
    enlacesHeader.classList.toggle("menudos")
})