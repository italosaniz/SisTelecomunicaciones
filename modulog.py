import os
import sys
import sqlite3
def verificar(x):
    for i in x:
        if (ord(i)<65 or ord(i)>90) and (ord(i)<97 or ord(i)>122) and ord(i)!=32:
            return False
    return True
def matricula():
    con=sqlite3.connect('constancia.s3db')
    print("ESTAS EN EL MENU DE MATRICULA")
    print("")
    print("DATOS DEL ALUMNO")
    nombre=input("Digite el Nombre del alumno:_")
    while(not verificar(nombre)):
        print("Intentelo de nuevo")
        nombre=input("Digite el Nombre del alumno:_")
    apellido1=input("Digite el Apellido Paterno:_")
    while (not verificar(apellido1)):
        print("Intentelo de nuevo")
        apellido1=input("Digite el Apellido Paterno:_")
    apellido2=input("Digite el Apellido Materno:_")
    while (not verificar(apellido2)):
        print("Intentelo de nuevo")
        apellido2=input("Digite el Apellido Materno:_")
    salida1=True
    while salida1:
        try:
            cui=int(input("Digite su cui:_"))
            nacimiento=int(input("Digite su fecha de nacimiento(Anho,Mes,Dia):_"))
            dni=int(input("Digite su documento de identidad:_"))
            salida1=False
        except:
            print("Ingreso no valido, ingrese solo numeros")
    cursor=con.cursor()
    print("CURSOS A MATRICULAR")
    cont=int(input("Ingreso numero de cursos a matricular:_"))
    for i in range (1, cont+1):
        curso=input("Ingrese el nombre del curso a matricular:_")
        salida2=True
        while salida2:
            try :
                codigo=int(input("Ingrese el codigo del curso:_"))
                matricula=int(input("Ingrese su n° de matricula del curso:_"))
                credito=float(input("Ingrese la cantidad de creditos del curso:_"))
                salida2=False
            except:
                print("Ingreso no valido, ingrese solo numeros")
        ciclo=input("Ingrese el ciclo del curso (A, B):_")
        while (not verificar(ciclo)):
            print("Intentelo de nuevo")
            ciclo=input("Ingrese el ciclo del curso (A,B):_")
        grupo=input("Ingrese el grupo a matricularse:_")
        while (not verificar(grupo)):
            print("Intentelo de nuevo")
            grupo=input("Ingrese el grupo a matricularse:_")
        cursor.execute("insert into Curso(codigo, NombreAsignatura, Ciclo, Grupo, Matricula, Creditos, Cui) values ('"+str(codigo)+"', '"+curso+"', '"+ciclo+"', '"+grupo+"', '"+str(matricula)+"', '"+str(credito)+"', '"+str(cui)+"')")
    os.system('cls')
    cursor.execute("insert into alumno(nombre, ApellidoPaterno, ApellidoMaterno, Cui, Dni, FechaNacimiento) values('"+nombre+"', '"+apellido1+"','"+apellido2+"','"+str(cui)+"','"+str(dni)+"','"+str(nacimiento)+"')")
    con.commit()
    con.close()

def modificar():
    estudiante=[]
    con=sqlite3.connect('constancia.s3db')
    cursor=con.cursor()
    cursor.execute("select * from alumno")
    for alumno in cursor:
        estudiante.append(alumno)
    salida3=True
    while salida3:
        try:
            cod=int(input("Ingrese su cui:_"))
            salida3=False
        except:
            print("Ingreso no valido, ingrese solo numeros")
    for alumno in estudiante:
        if int(alumno[3])==int(cod):
            nombre=alumno[0]
            apellido1=alumno[1]
            apellido2=alumno[2]
            nacimiento=alumno[4]
            dni=alumno[5]
            encotrado=True
            break
    nombre=input("Digite el Nombre del alumno:_")
    while(not verificar(nombre)):
        print("Intentelo de nuevo")
        nombre=input("Digite el Nombre del alumno:_")
    apellido1=input("Digite el Apellido Paterno:_")
    while(not verificar(apellido1)):
        print("Intentelo de nuevo")
        apellido1=input("Digite el Apellido Paterno:_")
    apellido2=input("Digite el Apellido Materno:_")
    while(not verificar(apellido2)):
        print("Intentelo de nuevo")
        apellido2=input("Digite el Apellido Materno:_")
    nacimiento=input("Digite su fecha de nacimiento(Anho,Mes,Dia):_")
    dni=input("Digite su documento de identidad:_")
    sql="update alumno set Nombre='"+nombre+"', ApellidoPaterno='"+apellido1+"', ApellidoMaterno='"+apellido2+"', Dni='"+dni+"', FechaNacimiento='"+nacimiento+"' where Cui="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    os.system("cls")
    print("Ha modificado su matricula")
    print("")
    
def constancia():
    con=sqlite3.connect('constancia.s3db')
    cursor=con.cursor()
    cursor.execute("select * from alumno")
    print("*********UNIVERSIDAD NACIONAL DE SAN AGUSTIN*********")
    print("")
    print("***** ESTUDIA INFORMATICA, CURSOS MENSUALES CON CERTIFICACION OFICIAL-INFOUNSA***")
    print("")
    print("**************CONSTANCIA DE MATRICULA*************")
    print("")
    print("DATOS DEL ALUMNO:")
    print("C.U.I:  \tNOMBRE Y APELLIDOS:  \t\tFECHA DE NACIMIENTO(AAAMMDD):  \tDNI:  ")
    print("==============================================================================================")
    cod=int(input("Ingrese su cui:_"))
    for alumno in cursor:
        if int(alumno[3])==cod:
            alu=str(alumno[3])+'\t'+str(alumno[0])+""+str(alumno[1])+""+str(alumno[2])+'\t'+'\t'+str(alumno[4])+'\t'+'\t'+'\t'+str(alumno[5])
            print(str(alu))
        else:
            print("usted no se ha matriculado")
            break
    print("")
    print("DATOS DE ESCUELA")
    print("==============================================================================================")
    print("NIVEL: Pre-grado \tESCUELA:Ingenieria en Telecomunicaciones ")
    print("")
    print("Queda matriculado en la(s) siguiente(s) asignatura(s):")
    print("Codigo  \tNombre de la Asignatura  \tCiclo  \tGrupo  \tMatricula  \tCreditos")
    print("=====================================================================================================")
    cursor.execute("select * from Curso")
    for Curso in cursor:
        curso=str(Curso[0])+'\t'+'\t'+str(Curso[1])+'\t'+'\t'+'\t'+'\t'+str(Curso[2])+'\t'+str(Curso[3])+'\t'+'\t'+str(Curso[4])+'\t'+'\t'+str(Curso[5])
        print(str(curso))
    con.close
    print('')
    
def salir():
    os.system("cls")
    import horario
    horario.menu()
