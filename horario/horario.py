#HORARIO
def menu():
    import os, sys
    print("****************************")
    print("         HORARIOS")
    print("****************************")
    print("")
    print("[1] Ver horarios ")
    print("[2] Hacer mi horario")
    print("[3] Ver mi horario")
    print("[4] Salir ")
    try:
        op=int(input("Seleccione la opcion deseada: "))
    except:
        print("No es una opcion valida, Ingrese nuevamente la opcion")
        print("")
        menu()
    os.system("cls")
    if op==1:
        print("")
        print("[1] Aula 105-B")
        print("[2] Aula 304-B")
        print("[3] Aula 405-B")
        print("[4] Lab-Informatica")
        print("")
        x=int(input("Seleccione el numero de Aula: "))
        if x==1:
            import os, sys, sqlite3
            con = sqlite3.connect('horario105-b.s3db')
            cursor=con.cursor()
            cursor.execute("SELECT * from horario105b")
            print("")
            print("             Horarios")
            print("")
            print("\t  Cod  \t Hora \t\t Lunes \t\t Martes \t\t Miercoles \t\t Jueves \t\t Viernes")
            print("************************************************************************************** ")
            for grado in cursor:
                grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])+'\t'+str(grado[3])+'\t'+str(grado[4])+'\t'+str(grado[5])+'\t'+str(grado[6])
                print(str(grad))
            con.close()
            print('')
        elif x==2:
            import os, sys, sqlite3
            con = sqlite3.connect('horario304-b.s3db')
            cursor=con.cursor()
            cursor.execute("SELECT * from horario304b")
            print("")
            print("             Horarios")
            print("")
            print("\t  Cod  \t Hora \t\t Lunes \t\t Martes \t\t Miercoles \t\t Jueves \t\t Viernes")
            print("**************************************************************************************** ")
            for grado in cursor:
                grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])+'\t'+str(grado[3])+'\t'+str(grado[4])+'\t'+str(grado[5])+'\t'+str(grado[6])
                print(str(grad))
            con.close()
            print('')
            os.system("cls")
            menu()
        elif x==3:
            import os, sys, sqlite3
            con = sqlite3.connect('horario405-b.s3db')
            cursor=con.cursor()
            cursor.execute("SELECT * from horario405b")
            print("")
            print("             Horarios")
            print("")
            print("\t  Cod  \t Hora \t\t Lunes \t\t Martes \t\t Miercoles \t\t Jueves \t\t Viernes")
            print("***************************************************************************************** ")
            for grado in cursor:
                grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])+'\t'+str(grado[3])+'\t'+str(grado[4])+'\t'+str(grado[5])+'\t'+str(grado[6])
                print(str(grad))
            con.close()
            print('')
            os.system("cls")
            menu()
        elif x==4:
            import os, sys, sqlite3
            con = sqlite3.connect('labinfo.s3db')
            cursor=con.cursor()
            cursor.execute("SELECT * from labinfo")
            print("")
            print("             Horarios")
            print("")
            print("\t  Cod  \t Hora \t\t Lunes \t\t Martes \t\t Miercoles \t\t Jueves \t\t Viernes")
            print("***************************************************************************************** ")
            for grado in cursor:
                grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])+'\t'+str(grado[3])+'\t'+str(grado[4])+'\t'+str(grado[5])+'\t'+str(grado[6])
                print(str(grad))
            con.close()
            print('')
        else:
            print("Por favor Ingrese la opcion correcta")
            print("")
            os.system("cls")
            menu()
                                                                                                                  
    elif op==2:
        hacer()
    elif op==3:
        ver()
    elif op==4:
        salir()
    else:
        print("Por favor digite un numero de los mencionados en la opcion")
        menu()
def hacer():
    import os,sys,sqlite3
    con = sqlite3.connect('crear.s3db')
    print("")
    print("                     registrar cursos")
    print("")

    hora=input("Digite la hora del curso: ")
    lunes=input("Ingrese curso del dia Lunes: ")
    martes=input("Ingrese curso del dia Martes: ")
    miercoles=input("Ingrese curso del dia Miercoles: ")
    jueves=input("Ingrese curso del dia Jueves: ")
    viernes=input("Ingrese curso del dia Viernes: ")
    os.system("cls")
    cursor=con.cursor()
    cursor.execute("insert into crear (hora, lunes ,martes ,miercoles ,jueves ,viernes) values('"+hora+"','"+lunes+"','"+martes+"','"+miercoles+"','"+jueves+"','"+viernes+"')")
    con.commit()
    con.close()
    resp=input("Seguir agregando los demas cursos ? SI/NO?: ")
    if resp.lower()== "no":
        menu()
    elif resp.lower()=="si":
        agregar()
    else:
        print("Usted no respondio correctamente")
        menu()
def ver():
    import os, sys, sqlite3
    con = sqlite3.connect('crear.s3db')
    cursor=con.cursor()
    cursor.execute("select * from crear")
    print("")
    print("             Estas en la opcion ver alumnos")
    print("")
    print("\t Hora \t\tLunes \t\t Martes \t Miercoles \t Jueves \t Viernes")
    print("***************************************************************************** ")
    for grado in cursor:
        grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t\t'+str(grado[2])+'\t\t'+str(grado[3])+'\t\t'+str(grado[4])+'\t\t'+str(grado[5])
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
