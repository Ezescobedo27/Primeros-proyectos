#include <iostream>

using namespace std;
// Programa que lea edad, sexo y altura, lo mostrara en la salida estandar
int main(){
	int age; char gender[10]; float height;
	
	cout<<"Wich is your age?";
	cin>>age;
	
	cout<<"Wich is your sexo?(female or male)";
	cin>>gender;
	
	cout<<"Wich is your height?(in meters)";
	cin>>height;																												
	
	cout<<"You have: "<<age<<" years"<<"\nYour gender is: "<<gender<<"\nYour height is: "<<height<<" metros.";
	
	
	
	return 0;
}