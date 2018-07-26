'''
SEIS AMIGOS DE VACACIONES. Seis amigos desean pasar sus vacaciones juntos y deciden, cada dos, 
utilizar diferentes medios de transporte (tren, avión, coche); sabemos que Alejandro no utiliza el coche ya que éste acompaña 
a Benito que va en tren. Andrés viaja en avión. Si Carlos no va acompañado de Darío ni hace uso del avión, 
podría decirnos en qué medio de transporte llega a su destino cada uno.

Alejandro_Benito --> Tren
Andres_Dario --> Avión
Carlos_Tomas --> Coche
'''
import random
intentos = 0
Alejandro_Benito = ""
Andres_Dario = ""
Carlos_Tomas = ""
transportes = ["tren", "avion", "coche"]
def Comprobar():
    if Alejandro_Benito == "tren" and Andres_Dario == "avion" and Carlos_Tomas == "coche":
        return True
    else:
        return False
while Comprobar() == False:
    Alejandro_Benito = transportes[random.randint(0,2)]
    Andres_Dario = transportes[random.randint(0,2)]
    Carlos_Tomas = transportes[random.randint(0,2)]
    intentos += 1
print(f"Intentos: {intentos}")
print(f"Alejandro y Benito: {Alejandro_Benito}")
print(f"Andrés y Darío: {Andres_Dario}")
print(f"Carlos y Tomás: {Carlos_Tomas}")
