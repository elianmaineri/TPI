from random import randint

palabra: [str] * 20 = [0] * 20
palabr = palabra[randint(0, 20)]
n=int(float(palabr))
casillas: [str] * n = [0] * n
palabr = str()
aciertos = float()
turnos = float()
oportunidades = int(8)
p = int(20)
a_ = str("A") 
h_ = str("H") 
o_ = str("O") 
r_ = str("R") 
c_ = str("C") 
ax_ = str("A") 
d_ = str("D") 
ox_ = str("O") 
 


op = int(input("          |||||||||\n MENU --> AHORACADO <-- \n          |||||||||\n Ingrese [1] para 'NIVEL BASICO' \n Ingrese [2] para 'NIVEL MEDIO' \n Ingrese [3] para 'SALIR' \n "))

if op == 1:
    palabra[0] = 'duda'
    palabra[1] = 'ojo'
    palabra[2] = 'puerta'
    palabra[3] = 'dureza'
    palabra[4] = 'pua'
    palabra[5] = 'cerveza'
    palabra[6] = 'palabra'
    palabra[7] = 'acero'
    palabra[8] = 'computadora'
    palabra[9] = 'moto'
    palabra[10] = 'apoyar'
    palabra[11] = 'cigarrillo'
    palabra[12] = 'amigo'
    palabra[13] = 'copo'
    palabra[14] = 'perro'
    palabra[15] = 'pizza'
    palabra[16] = 'madera'
    palabra[17] = 'reloj'
    palabra[18] = 'celular'
    palabra[19] = 'televisor'

    a=str(' ')
    h=str(' ')
    o=str(' ')
    r=str(' ')
    c=str(' ')
    a_=str(' ')
    d=str(' ')
    o_=str(' ')

    turnos = 0
    aciertos = 0
    for i in range(0, n, 1):
        casillas[i]='_'
    while turnos>=oportunidades or aciertos>=n:
        print('')
        print('oportunidades restantes: ', oportunidades-turnos)
        for i in range(0, n, 1):
            print('', casillas[i])
        print('')
        letra=str(input('Escriba la letra: '))
        encontrado=bool(False)
        for i in range(0, n, 1):
            subcadena=str()
            chr=subcadena(palabr, i, i)
            if str.upper(letra)==str.upper(chr):
                encontrando = True
                if casillas[i]=="_":
                    casillas[i] = chr
                    aciertos = aciertos+1
        if not encontrado:
            turnos +=1
            print("Letra no encontrada.")
            if turnos==1:
                a_ = ("A") 
            elif turnos==2:
                h_ = ("H")
            elif turnos==3:
                o_ = ("O")
            elif turnos==4:
                r_ = ("R")
            elif turnos==5:
                c_ = ("C")
            elif turnos==6:
                ax = ("A")
            elif turnos==7:
                d_ = ("D")
            elif turnos==8:
                ox = ("O")
            print("",a_,h_,o_,r_,c_,ax_,d_,ox_)
    if aciertos==n:
        print("Felicidades, has ganado")
    else:
        print("Has perdido.")
    print("La palabra secreta es: ",palabr)
    print("Aciertos: ",aciertos,"  Fallos: ",turnos)
    input(print("PRESIONE CUALQUIER TECLA PARA CONTINUAR"))
if op == 2:
    palabra[0] = 'fabricacion'
    palabra[1] = 'camiseta'
    palabra[2] = 'ninguno'
    palabra[3] = 'zapatillas'
    palabra[4] = 'computadora'
    palabra[5] = 'cabeza'
    palabra[6] = 'celular'
    palabra[7] = 'frasada'
    palabra[8] = 'habilidad'
    palabra[9] = 'termotanque'
    palabra[10] = 'masita'
    palabra[11] = 'alarma'
    palabra[12] = 'bolsillo'
    palabra[13] = 'zapatos'
    palabra[14] = 'archivado'
    palabra[15] = 'espejo'
    palabra[16] = 'compilado'
    palabra[17] = 'celebracion'
    palabra[18] = 'guitarra'
    palabra[19] = 'mesada'

    a=str(' ')
    h=str(' ')
    o=str(' ')
    r=str(' ')
    c=str(' ')
    a_=str(' ')
    d=str(' ')
    o_=str(' ')

    turnos = 0
    aciertos = 0
    for i in range(0, n, 1):
        casillas[i]='_'
    while turnos>=oportunidades or aciertos>=n:
        print('')
        print('oportunidades restantes: ', oportunidades-turnos)
        for i in range(0, n, 1):
            print('', casillas[i])
        print('')
        letra=str(input('Escriba la letra: '))
        encontrado=bool(False)
        for i in range(0, n, 1):
            subcadena=str()
            chr=subcadena(palabr, i, i)
            if str.upper(letra)==str.upper(chr):
                encontrando = True
                if casillas[i]=="_":
                    casillas[i] = chr
                    aciertos = aciertos+1
        if not encontrado:
            turnos +=1
            print("Letra no encontrada.")
            if turnos==1:
                a_ = ("A") 
            elif turnos==2:
                h_ = ("H")
            elif turnos==3:
                o_ = ("O")
            elif turnos==4:
                r_ = ("R")
            elif turnos==5:
                c_ = ("C")
            elif turnos==6:
                ax = ("A")
            elif turnos==7:
                d_ = ("D")
            elif turnos==8:
                ox = ("O")
            print("",a_,h_,o_,r_,c_,ax_,d_,ox_)
    if aciertos==n:
        print("Felicidades, has ganado")
    else:
        print("Has perdido.")
    print("La palabra secreta es: ",palabr)
    print("Aciertos: ",aciertos,"  Fallos: ",turnos)
    input(print("PRESIONE CUALQUIER TECLA PARA CONTINUAR"))