var numero1;
var numero2;
var resultado;

function suma(num1, num2){
    var valor;
    num1=parseInt(num1);
    num1=parseInt(num2);
    valor=num1+num2;
    return(valor);
}

function accion(){
    /*
    permite mostrar un mensaje y solicitar un valor
    */
    numero1=prompt('Introduce el primer número');
    numero2=prompt('Introduce el segundo número');
    resultado=suma(numero1,numero2);
    console.log(resultado);
}