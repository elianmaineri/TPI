# Variables
import random
import os 
mina=int(6)
carita=(":)")
vista=str("?")
ganaste=(False)
perdiste=(False)    
x=int(0)
y=int(0)
co=int(0)
orden=str("")
op=int(0)

#Funciones
def crea_tabla(v):
    tabl = [[0 for x in range(6)] for y in range(6)] 
    for i in range(6):
        for j in range(6):
            tabl[i][j]=(v)
    return (tabl) 

def mos_tabl(tabl):
    print(carita," 0  1  2  3  4  5")
    print("----------------------")
    for i in range (6):
        for j in range (6):
            if (j == 0):
                print(i,"|",tabl[i][j],end=("  "))
            elif (j == 5):
                print(tabl[i][j],"|",end=("  "))
            else:
                print(tabl[i][j],end=("  "))
        print()
    print("----------------------")
    return (tabl)

def ganador(tabl):
    global vista,co,carita
    co=(0)
    for i in range(6):
        for j in range(6):
            if tabl[i][j] == (vista):
                return False
            elif(tabl[i][j]=="*"):
                co += (1)
            if (co>3):
                print("Tiene demaciadas minas marcadas")
                return False

    return True

def selec_cas():
    global y,x,orden,co
    co=(0)
    while(co==0):
        print("Ingrese las cordenadas en (y,x) dentro del tablero del (0,5) ")
        y=int(input("y : "))
        x=int(input("x : "))
        if(y>5) or (y<0):
            co=(0)
        elif (x>5) or (x<0):
            co=(0)
        else:
            co=(1)
    co=(0)
    while(co==0):
        print("Seleccione (-) para abrir la casilla y (*) para marcar como bomba ")  
        orden=str(input("ingrese una accion: "))
        if (orden!="-") and (orden!="*"):
            co=(0)
        else:
            co=(1)
    return

def abrir_casilla(x,y,tabl):
    global perdiste,visible,carita,mina
    elemento_actual = tabl[y][x]
    if (elemento_actual == mina):
        perdiste = (True)
        carita=":("
        print("Has perdido")
        return
    elif (elemento_actual != mina):
        for k in range(-1,2):
                    for l in range(-1,2):
                        if (0 <= (y+k) <= 5) and (0 <= (x+l) <= 5):
                            if (tabl[y+k][x+l] != mina):
                                visible[y+k][x+l]=oculto[y+k][x+l]
    return
        
def mete_mina(tabl):
    global co,oculto,mina
    min_p:[int] * 3 = [0] * 3
    co=(0)
    while (co<3):
        y=random.randint(0,5)
        x=random.randint(0,5)
        if tabl[y][x] != (mina):
            tabl[y][x]=mina
            min_p[co]=(y,x)
            co += 1
    oculto=tabl      
    return 

def pistas(tabl):
    global mina 
    for i in range (6):
        for j in range(6):
            if tabl[i][j]==(mina):
                for k in range(-1,2):
                    for l in range(-1,2):
                        if (0 <= (i+k) <= 5) and (0 <= (j+l) <= 5):
                            if (tabl[i+k][j+l] != mina):
                                tabl[i+k][j+l] += (1)
    return (tabl)

#Juego
visible=(crea_tabla(str(vista)))
oculto=(crea_tabla(int(0)))
mete_mina(oculto)
oculto=pistas(oculto)
while(op==0):
    while (ganaste==False)and(perdiste==False):
        mos_tabl(visible)
        selec_cas()
        if (orden == "-"):
            abrir_casilla(x,y,oculto)
        elif(orden == "*"):
            visible[y][x]=("*")
        if ((visible[y][x])==(str(vista))):
            visible[y][x]=str("*")
        ganaste=ganador(visible)
        if (ganaste==True):
            carita=(":D")
            mos_tabl(visible)  
            print("Felicidades ganaste ")
        if (perdiste==(True)):
            mos_tabl(oculto)
    carita=(":)")
    visible=(crea_tabla(str(vista)))
    oculto=(crea_tabla(int(0)))
    mete_mina(oculto)
    oculto=pistas(oculto)
    ganaste=(False)
    perdiste=(False)
    op=int(input("Precione (0) para jugar de nuevo o (1) para volver al menu "))
