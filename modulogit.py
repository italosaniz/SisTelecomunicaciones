#COSTANCIA DE MATRICULA
def nombre():
    global nom
    nom=input("Ingrese su nombre: ")
    if (not verificar(nom)):
        print("Intentelo de nuevo")
        nombre()
def verificar(x):
    for i in x:
        if (ord(i)<65 or ord(i)>90) and (ord(i)<97 or ord(i)>122) and ord(i)!=32:
            return False
    return True
def apellido():
    global ape
    ape=input("Ingrese su apellido: ")
    if (not verificar(ape)):
        print("Intentelo de nuevo")
        apellido()
def numdni():
    global dni
    while True:
        try:
            dni=int(input("Ingrese el numero de su DNI: "))
            break
        except:
            print("Intentelo de nuevo")
    dni=str(dni)
    if (len(dni)!=8):
        print("Intentelo de nuevo")
        numdni()
def naci():
    global nacimiento
    while True:
        try:
            nacimiento=int(input("Ingrese la fecha de su nacimiento"))
            break
        except:
            print("Intentelo de nuevo")
def cui():
    global cui
    while True:
        try:
            cui=int(input("Ingrese el numero de su CUI"))
            break
        except:
            print("Intentelo de nuevo")
    
    
