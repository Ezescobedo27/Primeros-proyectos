let free = false;

const Validarcliente = (time)=>{
    let edad = prompt('cual es tu edad?');
    if(edad>18){
        if(time >= 2 && time < 7 && free == false){
            alert(`Son las ${time} y puedes pasar gratis porque eres la primer persona despues de las 2am`);
            free = true
        }
        else{
            alert(`Son las ${time}, tienes que pagar`);
        }
    }
    else{
        alert('no puedes pasar');
    }

}

Validarcliente(23);
Validarcliente(1);
Validarcliente(2);
Validarcliente(2);
Validarcliente(5);


