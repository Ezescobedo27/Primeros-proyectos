#include<iostream>
#include<math.h>
#include<conio.h>

using namespace std;

int main(){
	float x,y,f,resultado;
	
	cout<<"Dame el valor de x: "; cin>>x;	
	cout<<"Dame el valor de y: "; cin>>y;
	
	resultado = (sqrt(x)) / (pow(y,2)-1);
	
	cout<<"El resultado de la funcion es: "<<resultado; 
	
	return 0;
}