<?php
    require './includes/head.html';
?>
<body>
    <h1>Ejercicio 2 - Javascript</h1>
    <p>LA NOTA MEDIA. La nota media conseguida en una clase de 20 alumnos ha sido de 6. 
    Ocho alumnos han suspendido con un 3 y el resto superó el 5. 
    ¿Cuál es la nota media de los alumnos aprobados? Suponiendo que sacaran la misma nota</p>
    <p>Suspensos --> 8 alumnos con 3 || Aprobados --> 12 alumnos > 5</p>
    <textarea rows="1" cols="50" readonly="readonly" id="resultado">Aquí se mostrará el resultado</textarea>
    <input type="button" value="Ejecutar" onclick="Ejecutar()">
</body>