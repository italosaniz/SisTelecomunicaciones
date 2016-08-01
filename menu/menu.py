import os
import sys
import time
def principal():
    os.system("cls")
    print("")
    print("******************** INGIENERIA EN TELECOMUNICACIONES ********************")
    print("")
    print(" Ingrese en que modo se encuentra: ")
    print("    1.-Secretaria")
    print("    2.-Estudiante")
    print("    3.-SALIR")
    try:
        op=int(input(" Su opcion es: "))
    except:
        print("Esto no es un numero, porfavor elija algun numero de las opciones mostradas")
        print("")
        principal()
    if op==1:
        menu()
    elif op==2:
        estudiante()
    elif op==3:
        salir()
    else :
        print("Digite un numero de las opciones mostradas")
        principal()
    time.sleep(2)
        
def salir():
    os.system("cls")
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
    time.sleep(2)
        
def operacion():
    os.system("cls")
    op=input("Desea realizar otra operacion? SI/NO: ")
    if op.lower()=="no":
        principal()
    elif op.lower()=="si":
        menu()
    else:
        print("Usted no digito una respuesta adecuada")
        operacion()
    time.sleep(2)
        
def menu():
    os.system("cls")
    print("")
    print("************** Acceso al Sistema de Telecomunicaciones **************")
    print("")
    print("1.- Agregar alumnos: ")
    print("2.- Mostrar lista de alumnos: ")
    print("3.- Modificar lista de alumnos")
    print("4.- Eliminar")
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
        modificar()
    elif op==4:
        eliminar()
    elif op==5:
        salir()
    else:
        print("Por favor digite un numero de los mencionados en la opcion")
        menu()
    time.sleep(2)
        
def agregar():
    import sqlite3
    con = sqlite3.connect('partes.s3db')
    print("")
    print("                     Estas en el menu agregado")
    print("")
    name=input("Digite el nombre completo del Alumno: ")
    cui=input("Digite el cui del Alumno: ")
    os.system("cls")
    cursor=con.cursor()
    cursor.execute("insert into grado (Nombre, Cui) values('"+name+"','"+cui+"')")
    con.commit()
    con.close()
    resp=input("Deseas agregar otro alumno? SI/NO?: ")
    if resp.lower()== "no":
        operacion()
    elif resp.lower()=="si":
        agregar()
    else:
        print("Usted no respondio correctamente")
        menu()
        
def modificar():
    import sqlite3
    os.system("cls")
    grad=[]
    con=sqlite3.connect('partes.s3db')
    cursor=con.cursor()
    cursor.execute("select * from grado")
    print("Estas en la opcion modificar alumnos")
    print("")
    print("\tCod   \t              Nombre \t               CUI")
    print("***************************************************************** ")
    for grado in cursor:
        grad.append(grado)
        gra='\t'+str(grado[0])+'\t   '+str(grado[1])+'\t    '+str(grado[2])
        print(str(gra))
        print('')
    cod=input("DIGITE EL CODIDO DEL ALUMNO A MODIFICAR: ")
    for grado in grad:
        if int(grado[0])==int(cod):
            nombre=grado[1]
            cui=grado[2]
            encontrado=True
            break
    nombre=input("Digite el nombre nuevo "+nombre+": ")
    cui=input("Digite el CUI nuevo "+str(cui)+": ")
    sql="update grado set nombre='"+nombre+"', cui='"+cui+"' where cod="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    print("El alumno ha sido modificado")
    print("")
    time.sleep(3)
    operacion()
    
def eliminar():
    import os, sys, sqlite3
    os.system("cls")
    con = sqlite3.connect('partes.s3db')
    cursor=con.cursor()
    cursor.execute("select * from grado")
    print("")
    print("        Estas en la opcion borrar alumno de la lista")
    print("")
    print("\t  Cod   \t        Nombre    \t        CUI")
    print("***************************************************************** ")
    for grado in cursor:
        grad='\t'+str(grado[0])+'\t   '+str(grado[1])+'\t       '+str(grado[2])
        print(str(grad))
        print("")
    cod=input("Digite el codigo del alumno del que desea borrar: ")
    sql="delete from grado where Cod="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    print("El alumno ha sido borrado de la lista")
    print('')
    time.sleep(3)
    operacion()
    
def ver():
    import sqlite3
    os.system("cls")
    con = sqlite3.connect('partes.s3db')
    cursor=con.cursor()
    cursor.execute("select * from grado")
    print("")
    print("             Estas en la opcion ver alumnos")
    print("")
    print("\tCod   \t             Nombre \t                CUI")
    print("***************************************************************** ")
    for grado in cursor:
        grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])
        print(str(grad))
    print('')
    op=input("Desea realizar otra operacion? SI/NO: ")
    if op.lower()=="no":
        principal()
    elif op.lower()=="si":
        menu()
    else:
        print("Usted no digito una respuesta adecuada")
        operacion()
    time.sleep(2)
    
def salir():
    import sys
    res=input("Esta seguro que desea salir? SI/NO: ")
    if(res.lower()=="no"):
        menu()
    elif(res.lower()=="si"):
        import sys
        sys.exit(2)
        
principal()
