const obtenerInformacion = (materia)=>{
    materias = {
        fisica: ['perez','pedro','juan','pepitos'],
        programacion: ['rodrigez','juan','pepito','cofla','maria'],
        logica: ['hernandez','pedro','juan','cofla','maria'],
        quimica: ['juanez','pedro','juan','pepitos','maria'],

    }
    if(materias[materia] !== undefined) {
        return [materias[materia],materia,materias];
    }  else{
        return materias;
    }
}

const mostrarInformacion = (materia)=>{
    let informacion = obtenerInformacion(materia)

if(informacion !== false){
    let profesor = informacion[0][0];
    alumnos = informacion[0];
    alumnos.shift()
    document.write(`El profesor de <b>${informacion[1]}</b>: <b style = 'color:red'>${profesor}:</b><br>
    Los alumnos son: <b styl="color:blue">${alumnos}</b><br><br>
    `);
    
    ;
}
}
const cantidadDeClases = (alumnos)=>{
    let informacion = obtenerInformacion();
    let clasesPresentes = [];
    let cantidadTotal = 0;
    for(info in informacion){
        if(informacion[info].includes(alumnos)){
            cantidadTotal++;
            clasesPresentes.push([" " + info])
            }
        }
        
    return alumnos + ` esta en: <b> ${cantidadTotal} clases:</b> <b style = "color:red">${clasesPresentes}</b>
    <br><br>
    `;

    
}
mostrarInformacion('fisica');
mostrarInformacion('quimica');
mostrarInformacion('programacion');
mostrarInformacion('logica');

document.write(cantidadDeClases('pedro'));