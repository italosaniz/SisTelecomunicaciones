import os
import sys
import sqlite3
def matricula():
    con=sqlite3.connect('constancia.s3db')
    print("ESTAS EN EL MENU DE MATRICULA")
    print("")
    print("DATOS DEL ALUMNO")
    nombre=input("Digite el Nombre del alumno:_")
    apellido1=input("Digite el Apellido Paterno:_")
    apellido2=input("Digite el Apellido Materno:_")
    cui=input("Digite su cui:_")
    nacimiento=input("Digite su fecha de nacimiento(Anho,Mes,Dia):_")
    dni=input("Digite su documento de identidad:_")
    cursor=con.cursor()
    print("CURSOS A MATRICULAR")
    cont=int(input("Ingreso numero de cursos a matricular:_"))
    for i in range (1, cont+1):
        curso=input("Ingrese el nombre del curso a matricular:_")
        codigo=input("Ingrese el codigo del curso:_")
        ciclo=input("Ingrese el ciclo del curso (A, B):_")
        grupo=input("Ingrese el grupo a matricularse:_")
        matricula=input("Ingrese su n° de matricula del curso:_")
        credito=input("Ingrese la cantidad de creditos del curso:_")
        cursor.execute("insert into Curso(codigo, NombreAsignatura, Ciclo, Grupo, Matricula, Creditos, Cui) values ('"+codigo+"', '"+curso+"', '"+ciclo+"', '"+grupo+"', '"+matricula+"', '"+credito+"', '"+cui+"')")
    os.system('cls')
    cursor.execute("insert into alumno(nombre, ApellidoPaterno, ApellidoMaterno, Cui, Dni, FechaNacimiento) values('"+nombre+"', '"+apellido1+"','"+apellido2+"','"+cui+"','"+dni+"','"+nacimiento+"')")
    con.commit()
    con.close()

def modificar():
    estudiante=[]
    con=sqlite3.connect('constancia.s3db')
    cursor=con.cursor()
    cursor.execute("select * from alumno")
    for alumno in cursor:
        estudiante.append(alumno)
    cod=input("Ingrese su cui:_")
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
    apellido1=input("Digite el Apellido Paterno:_")
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
    print("**************CONSTANCIA DE MATRICULA*************")
    print("")
    print("DATOS DEL ALUMNO:")
    print("C.U.I:  \tNOMBRE Y APELLIDOS:  \t\tFECHA DE NACIMIENTO(AAAMMDD):  \tDNI:  ")
    print("==============================================================================================")
    for alumno in cursor:
        alu=str(alumno[3])+'\t'+str(alumno[0])+""+str(alumno[1])+""+str(alumno[2])+'\t'+'\t'+str(alumno[4])+'\t'+'\t'+'\t'+str(alumno[5])
        print(str(alu))
    print("")
    print("DATOS DE ESCUELA")
    print("===============================")
    print("NIVEL: Pregrado \tESCUELA: ")
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
    print("Se ha matriculado con exito")
    sys.exit()
