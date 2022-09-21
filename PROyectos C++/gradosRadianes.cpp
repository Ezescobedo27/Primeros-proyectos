#include <iostream>

using namespace std;

int main(){
	
	float grados,radianes; string entrada;
	
	cout<<"Que quieres sacar? G)Grados, R) Radianes"<<endl;
	cin>>entrada;
		
	if(entrada=="G"){
		cout<<"Ingresa los radianes: ";
		cin>>radianes;
		
		cout<<radianes<<" es igual a "<<((radianes*180)/3.1416)<<" grados";
	}
	
	else if(entrada == "R"){
		cout<<"Ingresa los grados: ";
		cin>>grados;
		
		cout<<grados<<" es igual a "<<((grados*3.1416)/180)<<" radianes";

	}

	else{
		cout<<"Opcion no valida";
	}
	
	return 0;
}