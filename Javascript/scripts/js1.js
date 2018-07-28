var C,R,A;
function Comprobar(){
    if(A<R && C>R) return true;
    else return false;
}
function Ejecutar(){
    while(!Comprobar()){
        C = Math.floor(Math.random() * 3);
        R = Math.floor(Math.random() * 3);
        A = Math.floor(Math.random() * 3);
        document.getElementById("resultado").value += "\nÁngela: " + A + "\nRosa: " + R + "\nCelia: " + C + "\n******************";
    }
    alert("Ángela: " + A + "\nRosa: " + R + "\nCelia: " + C +
            "\n Ángela habla más bajo que Celia.")
}