var podenco, alano, dogo, galgo;
var intentos = 0;
var texto = document.getElementById("resultado");
function Comprobar(){
	if(podenco>galgo && alano>galgo && alano<dogo) return true;
	else return false;
}
function Barato(){
	var resultado = Math.min(podenco,alano,dogo,galgo);
	if(resultado == podenco) return "podenco";
	else if(resultado == alano) return "alano";
	else if(resultado == dogo) return "dogo";
	else return "galgo";
}
function Ejecutar(){
	while(!Comprobar()){
		podenco = Math.floor(Math.random() * 3);
		alano = Math.floor(Math.random() * 3);
		dogo = Math.floor(Math.random() * 3);
		galgo = Math.floor(Math.random() * 3);
		intentos++;
		texto.value += "\r**********************\rNo se ha conseguido";
		texto.value += "podenco: " + podenco.toString() + "\ralano: " + alano.toString() +"\rdogo: " + dogo.toString() + "\rgalgo: " + galgo.toString();
	}
	texto.value +=  "\rIntentos: " + intentos + "\rEl más barato de mantener es el " + Barato();
		alert("El más barato de mantener es " + Barato());
}