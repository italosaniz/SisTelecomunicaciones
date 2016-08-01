
import getpass
import sqlite3
import os
import sys



def salir():
    o=input("¿\t\nDESEA SALIR DEL PROGRAMA ?")
    if o=="Si" or o=="SI" or o=="si":
        print("\t\nEL PROGRAMA SE ESTA CERRANDO")
        sys.exit(3)
    elif o=="NO" or o=="no" or o=="No":
        os.system("clear")
        login()

def login():
    
    print("\t\t\t\t\n**LOGIN**\n")
    user=input("\t\nUSUARIO: ")
    passw=getpass.getpass("\t\nPASSWORD: ")
    con=sqlite3.connect("seguridad.s3db")
    cursor=con.cursor()
    cursor.execute("SELECT * FROM seguridad1")
    users=cursor.fetchall()
    x=True
    for i in users:
        if i[1]==user:
            if i[2]==passw:
                os.system("clear")
                print("\t\n BIENVENIDO ",user)
                #AQUI COLOCAR  O LLAMAR LA SIGUIENTE FUNCION QUE SERIA LA DEL MENU
                x=False
                
    if x==True:
        e=input("\t\n USUARIO O CONTRASEÑA INCORRECTO ")
        e=input("INTENTELO DE NUEVO DIGITANDO '(I)' O APRETE '(S)' PARA SALIR ")
        if e=="S" or e=="s":
            print("\t\nEL PROGRAMA SE ESTA CERRANDO...")
            sys.exit(3)
        elif e=="I" or e=="i":
            os.system("clear")
            print("\t\nEscuela Profesional de Ingeniería de Telecomunicaciones")
            print("\t\nUniversidad Nacional de San Agustín")
            login()
        
        
              
    
            
             
def newlogin():
    REGISTRADOS = ['erick','fatima','italo','danitza','henry','Erick','Fatima','Danitza','Italo','Henry']
    CONTRASEÑAS = ['74601614']
    os.system("clear")
    print("\t\t\nEscuela Profesional de Ingeniería de Telecomunicaciones")
    print("\t\t\t\nUniversidad Nacional de San Agustín")
    print("\t\t\n**CREACION DE ACCESO PARA NUEVO USUARIO**\n")
    newuser=input("\t\nNUEVO USUARIO: ")
    if newuser in REGISTRADOS:
        print("\t\nEL NOMBRE DE USUARIO YA ESTA EN USO INGRESE OTRO PORFAVOR\n")
        newlogin()
    pas=getpass.getpass("\t\nPASSWORD: ")

    print("\t\n¿Desea desenmascarar la password?")
    re=input("\t\n¿ SI O NO ?\n")

    if re=="Si" or re=="SI" or re=="si":
        # VARIABLE RE : RESPUESTA DE LA PREGUNTA DESENMASCARAR LA CONTRASEÑA?
        print("\t\n \n",pas)
        reppas=getpass.getpass("\t\nREPITA PASSWORD: ")
        # VARIABLE REPPAS : REPETIR PASSWORD  
        if reppas==pas:
            cod=input("\t\nIngrese codigo de autorizacion: ")

            print("\t\nV2cz5FK4")

            bot=input("\t\nCOMPRUEBE QUE NO ES UN BOT INGRESE LOS SIGUIENTES CARACTERES: ")
                    
            if cod=="74601614":
                if bot=="V2cz5FK4":
                    con=sqlite3.connect("seguridad.s3db")
                    cursor=con.cursor()
                    cursor.execute("insert into seguridad1 (USUARIO, PASSWORD) values ('"+newuser+"','"+pas+"')")
                    con.commit()
                    con.close()
                    print("\t\nUSUARIO REGISTRADO CON EXITO")
                    os.system("clear")
                    login()
                 
            else:
                print("\t\nACCESO DENEGADO - CODIGO DE AUTOR. INVALIDO CONTACTE A SU SUPERIOR\n")
                seguridad()
        else:
            print("\t\nLAS CONTRASEÑAS NO COINCIDEN INTENTELO DE NUEVO\n")
            newlogin()
    
    elif re=="NO" or re=="no" or re=="No":
        reppas=getpass.getpass("\t\nREPITA PASSWORD: ")
        if reppas==pas:
            cod=int(input("\t\nIngrese codigo de autorizacion:\n"))
            print("\t\nV2cz5FK4\n")

            bot=input("\t\nCOMPRUEBE QUE NO ES UN BOT INGRESE LOS SIGUIENTES CARACTERES: ")
                    
            if cod=="74601614":
                if bot=="V2cz5FK4":
                    con=sqlite3.connect("seguridad.s3db")
                    cursor=con.cursor()
                    cursor.execute("insert into seguridad1 (USUARIO, PASSWORD) values ('"+newuser+"','"+pas+"')")
                    con.commit()
                    con.close()
                    print("\t\nUSUARIO REGISTRADO CON EXITO")
                    os.system("clear")
                    login()
                    
                
            else:
                print("\t\nACCESO DENEGADO - CODIGO DE AUTOR. INVALIDO CONTACTE A SU SUPERIOR\n")
                seguridad()
        else:
            print("\t\nLAS PASSWORD NO COINCIDEN INTENTELO DE NUEVO\n")
            newlogin()
                    

    
def seguridad():
    print("\t\t\n      Escuela Profesional de Ingeniería de Telecomunicaciones")
    print("\t\t\t\n             Universidad Nacional de San Agustín")
    print("\t\n¿ES USTED NUEVO USUARIO ?\n")
    r=input(" si      o    no \n")
    if r=="Si" or r=="SI" or r=="si":
        newlogin()
    
    elif r=="NO" or r=="no" or r=="No":
        login()
    else:
        print("\t\nOPCION NO VALIDA INTENTELO DE NUEVO ")
        seguridad()

seguridad()


