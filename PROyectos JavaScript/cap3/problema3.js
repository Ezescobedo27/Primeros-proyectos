let materias ={
        fisica: ['perez','pedro','juan','pepitos'],
        programacion: ['rodrigez','juan','pepito','cofla','maria'],
        logica: ['hernandez','pedro','juan','cofla','maria'],
        quimica: ['juanez','pedro','juan','pepitos','maria'],

    }
const inscribir = (alumno,materia)=>{
    personas = materias[materia];
    if(personas.length >= 21){
    document.write(`Lo siento <b>${alumno}</b>, las clases de <b>${materia}</b> ya estan llenas <br><br>`);
   
    } else{
        personas.push(alumno)
        if(materia=="fisica"){
            materias ={
                fisica: personas,
                programacion: materias['programacion'],
                logica: materias['logica'],
                quimica: materias['quimica'],
        
            }
        } else if(materia=="programacion"){
            materias ={
                fisica: materias['fisica'],
                programacion: personas,
                logica: materias['logica'],
                quimica: materias['quimica'],
        
            }
            
        }else if(materia=="logica"){
            materias ={
                fisica: materias['fisica'],
                programacion:  materias['programacion'],
                logica: personas,
                quimica: materias['quimica'],
        
            }
       }
       else if(materia=="quimica"){
        materias ={
            fisica: materias['fisica'],
            programacion:  materias['programacion'],
            logica: materias['logica'],
            quimica: personas,
    
            } 
        }
        document.write(`Felicidades ${alumno}, te has inscrito a ${materia}  <br><br>`);

    } 
}

document.write(materias['fisica'] + "<br>");
inscribir('pedrito','fisica'); 
inscribir('','fisica'); 
inscribir('pedrito','fisica'); 
inscribir('juan','fisica'); 
inscribir('pedro','fisica'); 
inscribir('ramses','fisica'); 
inscribir('pedrito','fisica'); 
inscribir('juan','fisica'); 
inscribir('pedro','fisica'); 
inscribir('ramses','fisica'); 
inscribir('pedrito','fisica'); 
inscribir('juan','fisica'); 
inscribir('pedro','fisica'); 
inscribir('ramses','fisica'); 
inscribir('pedrito','fisica'); 
inscribir('juan','fisica'); 
inscribir('pedro','fisica'); 
inscribir('ramses','fisica'); 
inscribir('pedrito','fisica'); 
inscribir('juan','fisica'); 
inscribir('pedro','fisica'); 
inscribir('ramses','fisica'); 

document.write("<br>" + materias['fisica']);