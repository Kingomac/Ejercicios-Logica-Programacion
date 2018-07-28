var AlejandroBenito, AndresDario, CarlosTomas;
var intentos = 0;
var transportes = ["tren", "avion", "coche"];
function Comprobar(){
	if(AlejandroBenito == "tren" && AndresDario == "avion" && CarlosTomas == "coche") return true;
	else return false;
}
function Ejecutar(){
	var texto = document.getElementById("resultado");
	while(!Comprobar()){
		AlejandroBenito = transportes[Math.floor(Math.random() * 3)];
		AndresDario = transportes[Math.floor(Math.random() * 3)];
		CarlosTomas = transportes[Math.floor(Math.random() * 3)];
		intentos++;
		texto.value += "\r*********************";
		texto.value += "\rAlejandro y Benito: " + AlejandroBenito + "\rAndrés y Darío: " + AndresDario + "\rCarlos y Tomás: " + CarlosTomas; 
	}
	alert("Completado\nAlejandro y Benito: " + AlejandroBenito + "\nAndrés y Darío: " + AndresDario + "\nCarlos y Tomás: " + CarlosTomas + "\nIntentos: " + intentos.toString());
}