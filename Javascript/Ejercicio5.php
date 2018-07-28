<?php
    require './includes/head.html';
    require './includes/body.html';
	require './includes/footer.html';
?>
<script src="./scripts/js5.js"></script>
<script type="text/javascript">
	document.getElementById("titulo").innerHTML = "Ejercicio 5";
	document.getElementById("enunciado").innerHTML = "LOS CUATRO PERROS. Tenemos cuatro perros: un galgo, un dogo, un alano y un podenco. Éste último come más que el galgo; el alano come más que el galgo y menos que el dogo, pero éste come más que el podenco. ¿Cuál de los cuatro será más barato de mantener?.<br>podenco<br>alano<br>dogo<br>->galgo<-";
	document.getElementById("resultado").setAttribute('rows', '5');
	document.getElementById("resultado").setAttribute('cols', '50');
</script>