<?php
    require './includes/head.html';
    require './includes/body.html';
	require './includes/footer.html';
?>
<script src="./scripts/js3.js"></script>
<script type="text/javascript">
	document.getElementById("titulo").innerHTML = "Ejercicio 3";
	document.getElementById("enunciado").innerHTML = "LOS CUATRO ATLETAS. De cuatro corredores de atletismo se sabe que C ha llegado inmediatamente detrás de B, y D ha llegado en medio de A y C. ¿Podría calcular el orden de llegada?<br>B, C, D, A";
	document.getElementById('resultado').setAttribute('rows', '30');
	document.getElementById('resultado').setAttribute('cols', '50');
</script>