print("******************** INGIENERIA EN TELECOMUNICACIONES ********************")
print("")
def principal():
    print(" Ingrese en que modo se encuentra: ")
    print("    1.-Secretaria")
    print("    2.-Estudiante")
    print("    3.-Docente")
    print("    4.-SALIR")
    try:
        op=int(input(" Su opcion es: "))
    except:
        print("Esto no es un numero, porfavor elija algun numero de las opciones mostradas")
        print("")
        principal()

    if op==1:
        secretaria ()
    elif op==2:
        estudiante()
    elif op==3:
        docente()
    elif op==4:
        salir()
    else :
        print("Digite un numero de las opciones mostradas")
        principal()
        
principal()
