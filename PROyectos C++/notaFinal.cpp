#include <iostream>

using namespace std;

int main(){
//	Leer nota final de 4 alumnos y calcular la media de los cuatro

float nota1,nota2,nota3,nota4,notaFinal;

cout<<"Dame tu nota final Pacho: "; cin>>nota1;
cout<<"Dame tu nota final Pepe: "; cin>>nota2;
cout<<"Dame tu nota final Jose: "; cin>>nota3;
cout<<"Dame tu nota final Pancrasio: "; cin>>nota4;

notaFinal = (nota1+nota2+nota3+nota4) / 4;
cout<<"La nota final de los alumnos es: "<<notaFinal;
	
	
	
	return 0;
}