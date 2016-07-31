print("******************** INGIENERIA EN TELECOMUNICACIONES ********************")
print("")
def principal():
    print(" Ingrese en que modo se encuentra: ")
    print("    1.-Profesor")
    print("    2.-Estudiante")
    print("    3.-SALIR")
    try:
        op=int(input(" Su opcion es: "))
    except:
        print("Esto no es un numero, porfavor elija algun numero de las opciones mostradas")
        print("")
        principal()

    if op==1:
        profesor()
    elif op==2:
        estudiante()
    elif op==3:
        salir()
    else :
        print("Digite un numero de las opciones mostradas")
        principal()
        
def salir():
    import sys
    res=input("Esta seguro que desea salir? SI/NO: ")
    if(res.lower()=="no"):
        principal()
    elif(res.lower()=="si"):
        import sys
        sys.exit(2)
    else:
        print("Usted no digito bien la respuesta")
        salir()

principal()
