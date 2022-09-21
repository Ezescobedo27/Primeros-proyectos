class Calculadora{
    constructor(){}
    
 sumar(num1,num2){
    return parseInt(num1) + parseInt(num2);
}
 restar(num1,num2){
    return parseInt(num1) - parseInt(num2);
}
 multiplicar(num1,num2){
    return parseInt(num1) * parseInt(num2);
}
 dividir(num1,num2){
    return parseInt(num1) / parseInt(num2);
}
potenciar(num,exp){
    return num**exp;
}
rainCuadrada(num){
   return Math.sqrt(num);
}
rainCubica(num){
    return Math.cbrt(num)
}
}

const calculadora = new Calculadora()

alert('Que operacion quieres realizar?');

let opc = prompt('1:sumar 2:restar 3:multiplicar 4:dividir 5:potenciar 6:raiz cuadrada 7:ra cubica' );

if(opc == '1'){
    let numero1 = prompt('Ingresa el numero 1?');
    let numero2 = prompt('Ingresa el numero 2?');
    let resultado = calculadora.sumar(numero1,numero2);
    alert(`Tu resultado es ${resultado}`)
}
else if(opc == '2'){
    let numero1 = prompt('Ingresa el numero 1?');
    let numero2 = prompt('Ingresa el numero 2?');
    let resultado = calculadora.restar(numero1,numero2);
    alert(`Tu resultado es ${resultado}`)
}
else if(opc == '3'){
    let numero1 = prompt('Ingresa el numero 1?');
    let numero2 = prompt('Ingresa el numero 2?');
    let resultado = calculadora.multiplicar(numero1,numero2);
    alert(`Tu resultado es ${resultado}`)
}
else if(opc == '4'){
    let numero1 = prompt('Ingresa el numero 1?');
    let numero2 = prompt('Ingresa el numero 2?');
    let resultado = calculadora.dividir(numero1,numero2);
    alert(`Tu resultado es ${resultado}`)
}
else if(opc == '5'){
    let numero1 = prompt('Ingresa el numero que quieras potenciar');
    let potencia1 = prompt('Ingresa el exponente');
    let resultado = calculadora.potenciar(numero1,potencia1)
    document.write(`Tu resultado es ${resultado}`);
}
else if(opc == '6'){
    let numero1 = prompt('Ingresa el numero al que quieras sacar raiz cuadrada');
    let resultado = calculadora.rainCuadrada(numero1)
    document.write(`Tu resultado es ${resultado}`);
}
else if(opc == '7'){
    let numero1 = prompt('Ingresa el numero que quieras sacar raiz cubica');
    let resultado = calculadora.rainCubica(numero1)
    document.write(`Tu resultado es ${resultado}`);
}

else{
    alert('No se ha encontrado ese valor')
}