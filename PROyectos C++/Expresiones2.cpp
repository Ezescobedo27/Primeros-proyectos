#include <iostream>

using namespace std;

int main(){
	float a,b,c,d,e,f,resultado;
	
	cout<<"Dame el valor de a: ";	cin>>a;

	cout<<"Dame el valor de b: ";	cin>>b;
	
	cout<<"Dame el valor de c: ";	cin>>c;
	
	cout<<"Dame el valor de d: ";	cin>>d;
	
	cout<<"Dame el valor de e: "; 	cin>>e;
	
	cout<<"Dame el valor de f: ";	cin>>f;
	
	resultado = (a + (b/c)) / (d + (e/f));
	cout.precision(3);
	
	cout<<"El resultado de la operacion es: "<<resultado;
	
	
	return 0;
}