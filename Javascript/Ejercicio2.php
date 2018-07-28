<?php
    require './includes/head.html';
    require './includes/body.html';
	require './includes/footer.html';
?>
<script type="text/javascript">
	document.getElementById("titulo").innerHTML = "Ejercicio 2";
	document.getElementById("enunciado").innerHTML ="LA NOTA MEDIA. La nota media conseguida en una clase de 20 alumnos ha sido de 6. Ocho alumnos han suspendido con un 3 y el resto superó el 5. ¿Cuál es la nota media de los alumnos aprobados? Suponiendo que sacaran la misma nota<br>Suspensos --> 8 alumnos con 3 || Aprobados --> 12 alumnos > 5"
	document.getElementById("resultado").setAttribute("rows", "1");
	document.getElementById("resultado").setAttribute("cols", "50");
</script>
<script src="./scripts/js2.js"></script>