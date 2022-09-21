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
 class celularAltaGama extends Celular{
     constructor(color,peso,tamaño,rdc,ram,rdce){
     super(color,peso,tamaño,rdc,ram);
     this.resolucionDeCamaraExtra = rdce;
     }
     grabarVideoLento(){
         alert('Estas grabando en camara lenta')
     }
     reconocimientoFacial(){
         alert('Vamos a iniciar un reconocimiento facial')
     }
     infoAltaGama(){
             return this.mobileInfo() + `Resolucion de camara extra: ${this.resolucionDeCamaraExtra}`
         }

     }
    

// const celular1 = new Celular('rojo','150g','5pg ','full hd','1GB ');
// const celular2 = new Celular('verde','155g','5.4pg','full hd','2GB');
// const celular3 = new Celular('azul','146g','5pg','hd','2GB');
// celular1.presionarBotonEncendido();
// celular1.tomarFotos();
// celular1.grabarVideo();
// celular1.reiniciar(); 
// celular1.presionarBotonEncendido();

celular1 = new celularAltaGama('rojo','130g','5.2pg','4k','3GB','Full hd');
celular2 = new celularAltaGama('negro','142g','6pg','4k','4GB','Hd');

document.write(`
${celular1.infoAltaGama()} <br><br>
${celular2.infoAltaGama()} <br>
`);