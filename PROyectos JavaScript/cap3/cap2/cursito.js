class Animal {
    constructor(especie,edad,color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} años y
        soy de color ${this.color}`;
    }
        verInfo(){
            document.write(this.info + "<br>");
        }

    }
    
    class Perro extends Animal{
        constructor(especie,edad,color,raza){
            super(especie,edad,color);
            this.raza = null;
        }
        set setRaza(newName){
            this.raza =  newName
        }
        get getRaza(){
            return this.raza;
        }
    }

  

const perro = new Perro('Perro',5,'Verde','Pug')
const gato = new Animal('gato',1,'negro');
const pajaro = new Animal('pajaro',3,'verde');

perro.setRaza    = 'pedro';
document.write(perro.getRaza)










