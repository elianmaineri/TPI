a=int(0)
while(a!=5):
    a=int(input("Para jugar siga las instrucciones \n Ingrese [1] para 'NAVECITA' \n Ingrese [2] para 'BUSCAMINA' \n Ingrese [3] para 'AHORACADO' \n Ingrese [4] para 'h'\n Ingrese [5] para salir del menu \n "))
    if(a==1):
        print("NAVECITA")
    elif(a==2): 
        print("BUSCAMINA")
    elif(a==3):   
        import AHORCADO
    elif(a==4): 
        print("h")
    elif(a==5):
        print("SALIDA")
    elif(a>5):
        print("NUMERO INCORRECTO")
