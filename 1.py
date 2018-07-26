'''
SILENCIO. Si Ángela habla más bajo que Rosa y Celia habla más alto que Rosa,
¿habla Ángela más alto o más bajo que Celia?
C
R
A
'''
import random

C = 0
R = 0
A = 0

def Comprobar():
    if A < R and C > R:
        return True
    else: return False

while Comprobar() == False:
    C = random.randrange(3)
    R = random.randrange(3)
    A = random.randrange(3)
    print("-------------------------------")
    print("Ángela: " + str(A))
    print("Rosa: " + str(R))
    print("Celia: " + str(C))
    if Comprobar():
        print("*******************************")
        print("Ángela habla más bajo que Celia")
    print("-------------------------------")