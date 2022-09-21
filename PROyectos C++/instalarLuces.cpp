#include <iostream>

using namespace std;

int main(){
	cout<<"Vamos a colocar luces en el atico"<<endl;
	string lugarLuces,tipoLuces,densidadLuces,colocar;
	int cantidadLuces;
	
	cout<<"\nQuieres las luces en la entrada o en el fondo?: ";
	cin>>lugarLuces;
	
	cout<<"\nQuieres luces sony o derma?: ";
	cin>>tipoLuces;

	cout<<"\nCuantas luces quieres que usemos?: ";
	cin>>cantidadLuces;
		
	cout<<"\nQuieres iluminacion fuerte o suave?: ";
	cin>>densidadLuces;  


	cout<<"\nColocaremos las luces en: "<<lugarLuces<<"\nColocaremos las luces: "<<tipoLuces<<"\n"<<"Colocaremos: "<<cantidadLuces<<" luces"<<"\nY la iluminacion sera: "<<densidadLuces;   
	                
	
	
	return 0;
}
	