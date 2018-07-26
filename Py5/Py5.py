'''
LOS CUATRO PERROS. Tenemos cuatro perros: un galgo, un dogo, un alano y un podenco. 
Éste último come más que el galgo; el alano come más que el galgo y menos que el dogo, 
pero éste come más que el podenco. ¿Cuál de los cuatro será más barato de mantener?.

podenco
alano
dogo
galgo <--
'''
import random
intentos = 0
podenco = 0
alano = 0
dogo = 0
galgo = 0
def Comprobar():
    if podenco > galgo and alano > galgo and alano < dogo:
        return True
    else:
        return False
def Barato():
    resultado = min(podenco,alano,dogo,galgo)
    if resultado == podenco:
        return "podenco"
    elif resultado == alano:
        return "alano"
    elif resultado == dogo:
        return "dogo"
    else:
        return "galgo"
while Comprobar() == False:
    podenco = random.randint(0,3)
    alano = random.randint(0,3)
    dogo = random.randint(0,3)
    galgo = random.randint(0,3)
    intentos += 1
print(f"Intentos: {intentos}")
print(f"El más barato de mantener es el {Barato()}")