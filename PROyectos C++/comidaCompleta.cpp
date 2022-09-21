#include <iostream>
#include <conio.h>

using namespace std;

int main(){
	string pensarComida,comprarIngredientes,finDeSemana,comidaPreparada,comidaServida;
	
//	PENSAR COMIDA COMPLETA
	cout<<"Vamos a preparar una comida completa para 5 personas el proximo fin de semana\n\n";
	
	cout<<"Piensa que comida completa prepararas"<<endl;
	
	cout<<"Ya pensaste que comida completa prepararas?"<<endl;
	cin>>pensarComida;
	
	while(pensarComida == "no"){
	
	                
		cout<<"Piensa que comida completa prepararas"<<endl;
		
		cout<<"Ya pensaste que comida completa prepararas?"<<endl;
		cin>>pensarComida;
	}
	
	
//	COMPRAR INGREDIENTES
	
	cout<<"Ve a comprar los ingredientes necesarios para preparar la comida\n\n";
	
	cout<<"Ya compraste los ingredientes?"<<endl;
	cin>>comprarIngredientes;
	
	
	while(comprarIngredientes == "no"){
		cout<<"Ve a comprar los ingredientes necesarios para preparar la comida"<<endl;
		
		cout<<"Ya compraste los ingredientes?"<<endl;
		cin>>comprarIngredientes;
	}
	
//	ESPERAR FIN DE SEMANA
	cout<<"Espera a que sea fin de semana\n\n";
	
	cout<<"Ya es fin de semana?"<<endl;
	cin>>finDeSemana;
	
	
	while(finDeSemana == "no"){
		cout<<"Espera a que sea fin de semana"<<endl;
		
		cout<<"Ya es fin de semana?"<<endl;
		cin>>finDeSemana;
	}
	
//	PREPARAR COMIDA
	cout<<"Prepara la comida\n\n";
	
	cout<<"Ya preparaste la comida?"<<endl;
	cin>>comidaPreparada;
	
	
	while(comidaPreparada == "no"){
		cout<<"Prepara la comida"<<endl;
		
		cout<<"Ya preparaste la comida?"<<endl;
		cin>>comidaPreparada;
	}
	
//	SERVIR COMIDA
	cout<<"Sirve la comida\n\n";
	
	cout<<"Ya serviste la comida?"<<endl;
	cin>>comidaServida;
	
	
	while(comidaServida == "no"){
		cout<<"Sirve la comida"<<endl;
		
		cout<<"Ya serviste la comida ?"<<endl;
		cin>>comidaServida;
	}

	cout<<"\n\n\nGRAN TRABAJO!!!";

	        	
	
	
	return 0;
}