#include <iostream>

using namespace std;

int main(){
	float a,b,c,d,resultado;
	cout<<"Dame el valor de a: "; cin>>a;
	cout<<"Dame el valor de b: "; cin>>b;
	cout<<"Dame el valor de c: "; cin>>c;
	cout<<"Dame el valor de d: "; cin>>d;
	
	resultado = a + (b/(c-d));
	
	cout<<"El resultado de la operacion es: "<<resultado;
	
	
	
	return 0;
}