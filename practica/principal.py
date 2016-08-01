print("******* MATRICULA *******")
import os
import sys
from modulog import *
def menu():
    print("Estas en el menu principal")
    print("1) MATRICULA")
    print("2) MODIFICAR MATRICULA")
    print("3) CONSTANCIA DE MATRICULA")
    print("4) SALIR")
    try:
        opc=int(input("Seleccione la opccion a realizar:_"))
    except:
        print("No ingreso un numero,porfavor introduzca un numero")
        print("")
        menu()
    os.system('cls')
    if opc==1:
        matricula()
        menu()
    elif opc==2:
        modificar()
        menu()
    elif opc==3:
        constancia()
        menu()
    elif opc==4:
        salir()
    else:
        print("Por favor digite un numero de los mencionados en la opcion")
        menu()

menu()
