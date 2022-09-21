dineroCofla = prompt('Cuanto dinero tiene cofla?')
dineroRoberto = prompt('Cuanto dinero tiene Roberto?')
dineroPedro = prompt('Cuanto dinero tiene Pedro')
dineroCofla = parseInt(dineroCofla)

if(dineroCofla >= 0.6 && dineroCofla < 1) {
    alert('Compra el helado de agua');
    alert('Y te sobran'+(dineroCofla - 0.6));

}
else if(dineroCofla > 1 && dineroCofla < 1.6) {
    alert('Compra el helado de crema')
    alert('Y te sobran'+(dineroCofla - 1.6))

}
else if(dineroCofla > 1.6 && dineroCofla < 1.7) {
    alert('Compra el helado de heladix')
    alert('Y te sobran'+(dineroCofla - 1.7))

}
else if(dineroCofla > 1.7 && dineroCofla < 1.8) {
    alert('Compra el helado de heladobich')
    alert('Y te sobran'+(dineroCofla - 1.8))

}
else if(dineroCofla > 1.8 && dineroCofla < 2.9) {
    alert('Compra el helado de helardo')
    alert('Y te sobran'+(dineroCofla - 2.9))

}
else if( dineroCofla >= 2.9){
    alert('Compra el helado de confites o el pote de 1/4kg')
    alert('Y te sobran'+(dineroCofla - 0.6))

    
}
else{
    alert('No te alcanza para ninguno')
}
//  
if(dineroRoberto >= 0.6 && dineroRoberto < 1) {
    alert('Compra el helado de agua')

}
else if(dineroRoberto > 1 && dineroRoberto < 1.6) {
    alert('Compra el helado de crema')
}
else if(dineroRoberto > 1.6 && dineroRoberto < 1.7) {
    alert('Compra el helado de heladix')
}
else if(dineroRoberto > 1.7 && dineroRoberto < 1.8) {
    alert('Compra el helado de heladobich')
}
else if(dineroRoberto > 1.8 && dineroRoberto < 2.9) {
    alert('Compra el helado de helardo')
}
else if( dineroRoberto >= 2.9){
    alert('Compra el helado de confites o el pote de 1/4kg')
    
}
else{
    alert('No te alcanza para ninguno')
}
// 
if(dineroPedro >= 0.6 && dineroPedro < 1) {
    alert('Compra el helado de agua')

}
else if(dineroPedro > 1 && dineroPedro < 1.6) {
    alert('Compra el helado de crema')
}
else if(dineroPedro > 1.6 && dineroPedro < 1.7) {
    alert('Compra el helado de heladix')
}
else if(dineroPedro > 1.7 && dineroPedro < 1.8) {
    alert('Compra el helado de heladobich')
}
else if(dineroPedro > 1.8 && dineroPedro < 2.9) {
    alert('Compra el helado de helardo')
}
else if( dineroPedro >= 2.9){
    alert('Compra el helado de confites o el pote de 1/4kg')
    
}
else{
    alert('No te alcanza para ningun helado')}