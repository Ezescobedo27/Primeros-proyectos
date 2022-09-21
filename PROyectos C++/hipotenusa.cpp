#include <iostream>
#include <math.h>

using namespace std;

int main(){
	float cateto1,cateto2,hipotenusa;
	
	cout<<"Dame el lado del primer cateto: ";	cin>>cateto1;
	cout<<"Dame el lado del segundo cateto: ";	cin>>cateto2;
	
	hipotenusa = (pow(cateto1,2)+pow(cateto2,2));
	
	hipotenusa = sqrt(hipotenusa);
	
	cout<<"El resultado de la hipotenusa es: "<<hipotenusa;	
	
	return 0;
}