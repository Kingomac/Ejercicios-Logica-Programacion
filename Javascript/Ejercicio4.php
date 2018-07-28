<?php
    require './includes/head.html';
    require './includes/body.html';
	require './includes/footer.html';
?>
<script type="text/javascript" src="./scripts/js4.js"></script>
<script type="text/javascript">
	document.getElementById("titulo").innerHTML = "Ejercicio 4";
	document.getElementById("enunciado").innerHTML = "SEIS AMIGOS DE VACACIONES. Seis amigos desean pasar sus vacaciones juntos y deciden, cada dos, utilizar diferentes medios de transporte; sabemos que Alejandro no utiliza el coche ya que éste acompaña a Benito que no va en avión. Andrés viaja en avión. Si Carlos no va acompañado de Darío ni hace uso del avión, podría Vd. decirnos en qué medio de transporte llega a su destino Tomás.";
	document.getElementById("resultado").setAttribute('rows', '5');
	document.getElementById("resultado").setAttribute('cols', '50');
</script>