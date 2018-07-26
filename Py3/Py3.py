'''
LOS CUATRO ATLETAS. De cuatro corredores de atletismo se sabe que C ha llegado inmediatamente 
detrás de B, y D ha llegado en medio de A y C. ¿Podría calcular el orden de llegada?

B
C
D
A
'''
import random
A = 0
B = 0
C = 0
D = 0
intentos = 0
def Comprobar():
    if C > B and D > C and D < A:
        return True
    else:
        return False
while Comprobar() == False:
    A = random.randint(0,4)
    B = random.randint(0,4)
    C = random.randint(0,4)
    D = random.randint(0,4)
    if Comprobar() == True:
        break
    else:
        print("No se ha conseguido")
        print("*******************")
        intentos += 1
print(f"Ha llevado {intentos} intentos")
print("Éxito, orden:")
print(f"B: {B + 1}")
print(f"C: {C + 1}")
print(f"D: {D + 1}")
print(f"A: {A + 1}")
