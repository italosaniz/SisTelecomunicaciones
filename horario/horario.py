#HORARIO
def menu():
    import os, sys
    print("****************************")
    print("         HORARIOS")
    print("****************************")
    print("")
    print("[1] Ver horarios ")
    print("[2] Ver mi horario")
    print("[3] Hacer mi horario ")
    print("[4] Salir ")
    try:
        op=int(input("Seleccione la opcion deseada: "))
    except:
        print("No es una opcion valida, Ingrese nuevamente la opcion")
        print("")
        menu()
    os.system("cls")
    if op==1:
        ver()
    elif op==2:
        vermi()
    elif op==3:
        mhor()
    elif op==4:
        salir()
    else:
        print("Por favor digite un numero de los mencionados en la opcion")
        menu()
        
def ver():
    print("Horario")
