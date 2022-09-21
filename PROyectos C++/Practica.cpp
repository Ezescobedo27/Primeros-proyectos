#include <iostream>

using namespace std;

int main(){
	
	float a,b,resultado;
	
	cout<<"Dame el valor de 'a': ";
	cin>>a;
	
	cout<<"Dame el valor de 'b': ";
	cin>>b;
	
	resultado = (a/b) + 1;
	cout.precision(2);
	
	cout<<"\nEl resultado de "<<a<<"/"<<b<<" + 1 "<<"es igual a: "<<resultado;
	
	
	
	return 0;
}