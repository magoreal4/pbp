import Typewriter from "typewriter-effect/dist/core";
document.addEventListener('DOMContentLoaded', function () {

    var i = 0;
    var firstTime = true;
    var image = [];
    var fondo = document.getElementsByClassName('imgBanner');
    var ultimo = false;

    image[i] = new Image();
    image[i].src = imgBanner[i];

    function changePicture() {
        if (ultimo) {
            textoBanner.classList.add('invisible');
            logoSVG.classList.remove("invisible");
            logoSVG.classList.add("animate-fade-in-fwd");
        } else {
            changeText();
        }
        
        fondo[0].style.backgroundImage = "url(" + image[i].src + ")";
        fondo[1].style.backgroundImage = "url(" + image[i].src + ")";
        fondo[2].style.backgroundImage = "url(" + image[i].src + ")";
        fondo[3].style.backgroundImage = "url(" + image[i].src + ")";
        fondo[4].style.backgroundImage = "url(" + image[i].src + ")";
        fondo[5].style.backgroundImage = "url(" + image[i].src + ")";
        fondo[6].style.backgroundImage = "url(" + image[i].src + ")";

        if (firstTime) {
            imgBanner.forEach((e, i) => {
                image[i] = new Image();
                image[i].src = imgBanner[i]
                image[i].onload = function () {
                    console.log("ok");
                };
            })
            firstTime = false;
        }
        if (i < (imgBanner.length - 1)) {
            i++;
            setTimeout(changePicture, slideTime);
        } else {
            ultimo = true;
            if (repeat) {
                i = 0;
                setTimeout(changePicture, slideTime);
            } else {
                setTimeout(()=>{
                    textoBanner.classList.add('invisible');
                    logoSVG.classList.remove("invisible");
                    logoSVG.classList.add("animate-fade-in-fwd");
                }, slideTime);
            }
        }
    }
    window.onload = changePicture;

    function changeColor2ndword(word) {
        let segundaPalabra;
        let texto = word.split(' ');
        if (texto.length > 1) {
            segundaPalabra = texto[1];
            for (let i = 2; i <= texto.length - 1; i++) {
                segundaPalabra += ` ${texto[i]} `;
            }
            texto[1] = `<br><span class="text-primary "> ${segundaPalabra} </span> `;
            return texto[0] + texto[1];
        } else {
            return texto[0];
        }
    }

    // Texto Principal y descripcion
    var textoPrin = textoBanner.querySelectorAll('h2');

    function changeText() {
        let texto;
        textoPrin[i].classList.toggle("invisible");
        effects_text ?
        textoPrin[i].classList.add("animate-text-flicker-in-glow") :            null
        texto = textoPrin[i].textContent;
        textoPrin[i].innerHTML = changeColor2ndword(texto);

        new Typewriter('#typewriter', {
            strings: desBanner[i],
            autoStart: true,
            delay: 30
        });
        if (i > 0) {
        textoPrin[i - 1].classList.toggle("invisible");
        } else {
            if (i == 0 && !firstTime) {
                textoPrin[imgBanner.length - 1].classList.toggle("invisible");
            }
        }

    }

});