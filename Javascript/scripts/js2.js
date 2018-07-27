function Ejecutar(){
    var i;
    for(i = 0; i < 10; i++){
        var n = (8*3+12*i)/20;
        if(n == 6) break;
    }
    document.getElementById("resultado").value = "La nota media de los no suspensos es: " + i.toString();
}