import os
import sys
from modulog import *
os.system("cls")
print("\n******* MATRICULA E IMPRIME LA CONSTANCIA DE MATRICULA *******")

def menu1():
    print("\nEstas en el menu principal")
    print("1) MATRICULA")
    print("2) MODIFICAR MATRICULA")
    print("3) CONSTANCIA DE MATRICULA")
    print("4) HORARIOS")
    print("5) REGRESAR AL MENU ANTERIOR")
    try:
        opc=int(input("Seleccione la opccion a realizar:_"))
    except:
        print("No ingreso un numero,porfavor introduzca un numero")
        print("")
        menu1()
    os.system('cls')
    if opc==1:
        matricula()
        menu1()
    elif opc==2:
        modificar()
        menu1()
    elif opc==3:
        constancia()
        menu1()
    elif opc==4:
        salir()
    elif opc==5:
        import menu
        menu.principal()
    else:
        print("Por favor digite un numero de los mencionados en la opcion")
        menu1()

menu1()
