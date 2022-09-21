const materias = {
    fisica:[90,6,4,'fisica'],
    logica:[90,7,4,'logica'],
    tecnologia:[90,7,4,'tecnologia'],
    fisicas:[3,7,4,'fisicas'],
    quimica:[32,7,4,'quimica'],
    mundo:[90,2,4,'mundo'],
}
const aprobo = ()=>{
    for(materia in materias){ 

        let asistencia = materias[materia][0];
        let promedio = materias[materia][1];
        let trabajos = materias[materia][2];

        console.log(materias[materia][3]);
// asistencias
        if(asistencia>=90){
            console.log("%c   Asistencias en orden","color:green");
        }
        else{
            
            console.log("%c   Falta de asistencias","color:red");
// promedio   
        }
        if(promedio >=7){
            console.log("%c   Promedio en orden","color:green")
        }
        else{
            console.log("%c   Promedio desaprovado", "color:red");
        }
    // trabajos
        if(trabajos>=3){
            console.log("%c  Trabajos en orden","color:green");
        }
        else{
            console.log("%c   Trabajos desaprobados","color:red");
        }
    }
}
aprobo()