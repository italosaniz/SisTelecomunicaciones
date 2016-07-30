def menu():
    import os, sys
    print("************** Acceso al Sistema de Telecomunicaciones **************")
    print("")
    print("1.- Agregar alumnos: ")
    print("2.- Mostrar lista de alumnos: ")
    print("3.- Clasificarlos segun su año: ")
    print("4.- Modificar lista de alumnos")
    print("5.- Salir")
    try:
        op=int(input("Introduzca el numero de la opcion deseada: "))
    except:
        print("Esto no es un numero, porfavor elija algun numero de las opciones mostradas")
        print("")
        menu()
    os.system("cls")
    if op==1:
        agregar()
    elif op==2:
        ver()
    elif op==3:
        clasificar()
    elif op==4:
        modificar()
    elif op==5:
        salir()
    else:
        print("Por favor digite un numero de los mencionados en la opcion")
        menu()
        
def agregar():
    import os,sys,sqlite3
    con = sqlite3.connect('partes.s3db')
    print("Estas en el menu agregado")
    print("")

    name=input("Digite el nombre completo del Alumno: ")
    cui=input("Digite el cui del Alumno: ")
    os.system("cls")
    cursor=con.cursor()
    cursor.execute("insert into grado (Nombre, Cui) values('"+name+"','"+cui+"')")
    con.commit()
    con.close()
    menu()
def modificar():
    import os, sys, sqlite3
    grad=[]
    con=sqlite3.connect('partes.s3db')
    cursor=con.cursor()
    cursor.execute("select * from grado")
    print("Estas en la opcion modificar alumnos")
    print("")
    print("\t  Cod   \t Nombre \t CUI")
    print("***************************************************************** ")
    for grado in cursor:
        grad.append(grado)
        grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])
        print(str(grad))
        print('')
    cod=input("DIGITE EL CODIDO DEL ALUMNO A MODIFICAR: ")
    global nombre
    global cui
    for grado in grad:
        if int(grado[0]==int(cod)):
            nombre=grado[1]
            cui=grado[2]
            encontrado=True
            break
    
    nombre=input("Digite el nombre nuevo"+nombre+": ")
    cui=input("Digite el CUI nuevo"+str(cui)+": ")
    sql="update grado set Nombre='"+name+"', CUI="+cui+"' where Cod ="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    os.sytem("cls")
    print("El producto a sido modificado")
    print("")
    menu()
      
def ver():
    import os, sys, sqlite3
    con = sqlite3.connect('partes.s3db')
    cursor=con.cursor()
    cursor.execute("select * from grado")
    print("Estas en la opcion ver alumnos")
    print("")
    print("\t  Cod   \t Nombre \t CUI")
    print("***************************************************************** ")
    for grado in cursor:
        grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])
        print(str(grad))
    con.close()
    print('')
    menu()
def salir():
    import sys
    res=input("Esta seguro que desea salir? SI/NO: ")
    if(res.lower()=="no"):
        menu()
    elif(res.lower()=="si"):
        import sys
        sys.exit(2)
        
menu()
