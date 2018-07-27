var A,B,C,D;
function Ejecutar(){
    var resultado = document.getElementById("resultado");
    var intentos = 0;
    while(!Comprobar()){
        A = Math.floor(Math.random() * 4);
        B = Math.floor(Math.random() * 4);
        C = Math.floor(Math.random() * 4);
        D = Math.floor(Math.random() * 4);
        intentos++;
        resultado.value += "\rNo se ha conseguido\r*****************\r";
    }
    resultado.value += "\rHa llevado " + intentos + " intentos";
    resultado.value += "\r Éxito, orden:\rB: " + (B+1);
    resultado.value += "\rC: " + (C+1);
    resultado.value += "\rD: " + (D+1);
    resultado.value += "\rA: " + (A+1); 
    alert("Operación completada");
}
function Comprobar(){
    if(C > B && D > C && D < A) return true;
    else return false;
}