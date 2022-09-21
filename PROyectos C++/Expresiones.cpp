#include <iostream>

using namespace std;

int main(){
	float a,b,c,d,resultado;
	
	cout<<"Escribe el valor de 'a':";
	cin>>a;
	
	cout<<"Escribe el valor de 'b':";
	cin>>b;
	
	cout<<"Escribe el valor de 'c':";
	cin>>c;
	
	cout<<"Escribe el valor de 'd':";
	cin>>d;
	
	resultado = (a+b)/(c+d);
	
	cout.precision(3);
	
	cout<<"El resultado de la expresion es: "<<resultado;
	
	
	
	
	
	return 0;
}