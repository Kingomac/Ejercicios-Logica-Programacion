'''
LA NOTA MEDIA. La nota media conseguida en una clase de 20 alumnos ha sido de 6. 
Ocho alumnos han suspendido con un 3 y el resto superó el 5. 
¿Cuál es la nota media de los alumnos aprobados? Suponiendo que sacaran la misma nota

Suspensos --> 8 alumnos con 3
Aprobados --> 12 alumnos > 5
'''
i = 0
#notaMedia = (8*3+12*x)/20
for i in range(10):
    notaMedia = (8*3+12*i)/20
    if notaMedia == 6:
        break
print(f"La nota media de los no suspensos es: {i}")