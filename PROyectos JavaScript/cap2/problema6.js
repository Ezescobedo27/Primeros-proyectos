class App{
    constructor(descargas,puntuacion,peso){
        this.descargas = descargas;
        this.puntuacion = puntuacion;
        this.peso = peso;
        this.iniciada = false;
        this.instalada = false;
    }
    instalar(){
        if(this.instalada == false){
            this.instalada = true;
            alert('app instalada')
        
        }
    }
    desinstalar(){
        if(this.instalada == true){
            this.instalada = false;
            alert('app desinstalada')
        
        }
    }
    abrir(){
        if(this.iniciada == false && this.instalada == true){
            this.iniciada = true;
            alert('App iniciada');
        }
    }
    cerrar(){
        if(this.iniciada == true && this.instalada == true){
            this.iniciada = false;
            alert('App cerrada');
        }
    }
    appInfo(){
        return `
        Descargas: <b>${this.descargas}</b> <br>
        Puntuacion: <b>${this.puntuacion}</b> <br>
        Peso: <b>${this.peso}</b>
        
        `
    }

}
const aplicacion1 = new App('13,000','2 estrellas','1000mb');
const aplicacion2 = new App('16,000','5 estrellas','900mb');
const aplicacion3 = new App('12,000','3 estrellas','220mb');
const aplicacion4 = new App('11,000','5 estrellas','900mb');
const aplicacion5 = new App('15,000','2 estrellas','1000mb');
const aplicacion6 = new App('16,000','5 estrellas','900mb');
const aplicacion7 = new App('13,000','3 estrellas','300mb');

// aplicacion1.instalar();
// aplicacion1.abrir();
// aplicacion1.cerrar();
// aplicacion1.desinstalar();

document.write(`
${aplicacion1.appInfo()} <br><br>
${aplicacion2.appInfo()} <br><br>
${aplicacion3.appInfo()} <br><br>
${aplicacion4.appInfo()} <br><br>
${aplicacion5.appInfo()} <br><br>
${aplicacion6.appInfo()} <br><br>
${aplicacion7.appInfo()} <br>

`);