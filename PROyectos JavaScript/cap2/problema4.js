class Celular{
    constructor(color,peso,tamaño,rdc,ram){
        this.color = color;
        this.peso = peso;
        this.tamaño = tamaño;
        this.resolucionDeCamara = rdc;
        this.memoriaRam = ram;
        this.encendido = false;
    }
    presionarBotonEncendido(){
        if(this.encendido == false){
            alert('Celular prendido')
            this.encendido = true;
        } else{
            alert('Apagado')
            this.encendido = false;
        }
    }
    reiniciar(){
        if(this.encendido == true){
            alert('reiniciando celular');
        } else{
            alert('el celular se esta reiniciando')

        }
    }
    tomarFotos(){
        alert(`Foto tomada en la resolucion de: ${this.resolucionDeCamara}`)
    }
    grabarVideo(){
        alert(`Grabando video en ${this.resolucionDeCamara}`)
         
    }
    mobileInfo(){
        return `
        Color: <b>${this.color}</b> <br>
        Peso: <b>${this.peso}</b> <br>
        Tamaño: <b>${this.tamaño}</b> <br>
        Resolucion de Video: <b>${this.resolucionDeCamara}</b> <br>
        Memoria Ram: <b>${this.memoriaRam   }</b> <br>
        `
    }
}

const celular1 = new Celular('rojo','150g','5pg ','full hd','1GB ');
const celular2 = new Celular('verde','155g','5.4pg','full hd','2GB');
const celular3 = new Celular('azul','146g','5pg','hd','2GB');
// celular1.presionarBotonEncendido();
// celular1.tomarFotos();
// celular1.grabarVideo();
// celular1.reiniciar(); 
// celular1.presionarBotonEncendido();

document.write(`
${celular1.mobileInfo()} <br>
${celular2.mobileInfo()} <br>
${celular3.mobileInfo()} <br>
`);