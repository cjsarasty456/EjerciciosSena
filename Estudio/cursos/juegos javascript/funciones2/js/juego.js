var vida=100;

function ataqueEnemigo(potencia, nombreAtaque){
    vida-=potencia;
    muestraVida(nombreAtaque);
}
function bebePocion(){
}
function muestraVida(nombre){
    console.log("Has sido Atacado con: "+nombreAtaque);
    console.log("Nivel de vida del Heroe");
    console.log(vida);
}