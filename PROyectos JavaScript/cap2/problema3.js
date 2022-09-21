

const sumar = (num1,num2)=>{
    return parseInt(num1) + parseInt(num2);
}
const restar = (num1,num2)=>{
    return parseInt(num1) - parseInt(num2);
}
const dividir = (num1,num2)=>{
    return parseFloat(num1) / parseFloat(num2);
}
const multiplicar = (num1,num2)=>{
    return parseInt(num1) * parseInt(num2);
}

alert('Elige una opcion');
let opc = prompt('1)Suma, 2)Resta, 3)Division, 4)Multiplicacion');

if(opc ==1){
    let numero1 = prompt('Escribe el primer numero');
    let numero2 = prompt('Escribe el segundo numero');
    let resultado = sumar(numero1,numero2);
    document.write(resultado);
}
if(opc ==2){
    let numero1 = prompt('Escribe el primer numero');
    let numero2 = prompt('Escribe el segundo numero');
    let resultado = restar(numero1,numero2);
    document.write(resultado);
}
if(opc ==3){
    let numero1 = prompt('Escribe el primer numero');
    let numero2 = prompt('Escribe el segundo numero');
    let resultado = dividir(numero1,numero2);
    document.write(resultado);
}
if(opc ==4){
    let numero1 = prompt('Escribe el primer numero');
    let numero2 = prompt('Escribe el segundo numero');
    let resultado = multiplicar(numero1,numero2);
    document.write(resultado);
}