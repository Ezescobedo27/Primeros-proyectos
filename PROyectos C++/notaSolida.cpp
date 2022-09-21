#include <iostream>

using namespace std;
// PRACTICA 3 TEORICA 6 PARTICIPACION 1
int main(){
	float notaPractica,notaTeorica,notaParticipacion, notaFinal;
	
	cout<<"Cual es la calificacion de tu nota practica?(1-10) "; cin>>notaPractica;
	cout<<"Cual es la calificacion de tu nota teorica?(1-10) "; cin>>notaTeorica;
	cout<<"Cual es la calificacion de tu nota de participacion?(1-10) "; cin>>notaParticipacion;
	
	notaPractica *= .30;
	notaTeorica *= .60;
	notaParticipacion *= .10;
	
	notaFinal = notaPractica + notaTeorica + notaParticipacion;
	
	cout<<"Tu nota es de: "<<notaFinal;
	
	
	
	return 0;
}