a=int(0)
while(a!=5):
    a=int(input("Para jugar siga las instrucciones \n Ingrese [1] para 'NAVECITA' \n Ingrese [2] para 'BUSCAMINA' \n Ingrese [3] para 'SOPA DE LETRAS' \n Ingrese [4] para 'h'\n Ingrese [5] para salir del menu \n "))
    if(a==1):
        import JUEGO1
    elif(a==2): 
        print("BUSCAMINA")
    elif(a==3):   
        print("SOPA DE LETRAS")
    elif(a==4): 
        print("h")
    elif(a==5):
        print("SALIDA")
    elif(a>5):
        print("NUMERO INCORRECTO")
