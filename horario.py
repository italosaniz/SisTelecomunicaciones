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
            print("\t  Cod  \t Hora \t Lunes \t Martes \t Miercoles \t Jueves \t Viernes")
            print("********************************************************************** ")
            for grado in cursor:
                grad='\t'+str(grado[0])+'\t'+str(grado[1])+'\t'+str(grado[2])+'\t'+str(grado[3])+'\t'+str(grado[4])+'\t'+str(grado[5])+'\t'+str(grado[6])
                print(str(grad))
            con.close()
            print('')
                                                                                                                              
    elif op==2:
        vermi()
    elif op==3:
        mhor()
    elif op==4:
        salir()
    else:
        print("Por favor digite un numero de los mencionados en la opcion")
        menu()
menu()

