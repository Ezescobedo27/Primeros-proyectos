#include <iostream>

using namespace std;

int main(){
	string preguntarCono,adquirirCono,esperar,graduarse,preguntarCarrera,inscribirteCarrera;
	cout<<"Incripcion a Ingenieria Electrica\n\n";
// CONOCIMIENTOS NECESARIOS
	cout<<"Pregunta a la Universidad los conocimientos requeridos para asistir a la carrera de Ingenieria Electrica\n\n";
	
	cout<<"Ya preguntaste cuales son los conocimientos necesarios para asistir a la carrera?";
	cin>>preguntarCono;
	
	while(preguntarCono == "no"){
	system("cls");
	cout<<"Pregunta a la Universidad los conocimientos requeridos para asistir a la carrera de Ingenieria Electrica\n\n";
	
	cout<<"Ya preguntaste cuales son los conocimientos necesarios para asistir a la carrera?";
	cin>>preguntarCono;		
	}
	system("cls");
// ADQUIRIR CONOCIMIENTOS
	cout<<"Adquiere los conocimientos requeridos para asistir a la carrera de Ingenieria Electrica\n\n";
	
	cout<<"Ya adquiriste los conocimientos necesarios para asistir a la carrera?";
	cin>>adquirirCono;
	
	while(adquirirCono == "no"){
	system("cls");
	cout<<"Adquiere los conocimientos requeridos para asistir a la carrera de Ingenieria Electrica\n\n";
	
	cout<<"Ya adquiriste los conocimientos necesarios para asistir a la carrera?";
	cin>>adquirirCono;	
	}
	system("cls");
// ESPERAR A QUE ACABE LA PREPA
	cout<<"Espera a que acabe la prepa\n\n";
	
	cout<<"Ya acabaste la prepa?";
	cin>>esperar;
	
	while(esperar == "no"){
	system("cls");
	cout<<"Espera a que acabe la prepa\n\n";
	
	cout<<"Ya acabaste la prepa?";
	cin>>esperar;	
	}
	system("cls");
// GRADUARSE DE LA PREPA
	cout<<"Graduate de la prepa\n\n";
	
	cout<<"Ya graduaste de la prepa?";
	cin>>graduarse;
	
	while(graduarse == "no"){
	system("cls");
	cout<<"Graduate de la prepa\n\n";
	
	cout<<"Ya graduaste de la prepa?";
	cin>>graduarse;	
	system("cls");
	}
//	PREGUNTAR DATOS DE INSCRIPCION
	cout<<"Pregunta sobre la inscripccion de la Universidad\n\n";
	
	cout<<"Ya preguntaste sobre la carrera?";
	cin>>preguntarCarrera;
	
	while(preguntarCarrera == "no"){
	system("cls");
	cout<<"Pregunta sobre la inscripccion de la Universidad\n\n";
	
	cout<<"Ya preguntaste sobre la carrera?";
	cin>>preguntarCarrera;
	}
	system("cls");
// INSCRIBETE A LA CARRERA
	cout<<"Inscribete a la carrera\n\n";
	
	cout<<"Ya te inscribiste a la carrera?";
	cin>>inscribirteCarrera;
	
	while(inscribirteCarrera == "no"){
	system("cls");
	cout<<"Inscribete a la carrera\n\n";
	
	cout<<"Ya te inscribiste a la carrera?";
	cin>>inscribirteCarrera;
	}
	system("cls");
	cout<<"TE HAZ INSCRITO DE MANERA SATISFACTORIA A LA INGENIERIA ELECTRICA, TE ESPERAMOS ESTE REGRESO A CLASES";
	
	
	return 0;
}