from os import system, name # Para limpiar la terminal.
#Procedimiento para limpiar la terminal
def clear():
    if name == 'nt': # En caso de Windows
        _ = system('cls')
    else: # Para Mac o Linux
        _ = system('clear')

import controller as ctr
import re

def registerUser():
    clear()
    usuario=input('Ingrese el nombre de usuario: ')
    password=input('Ingrese la password: ')
    email=input('Ingrese el email: ')
    while esEmail(email)==False:
        email=input('\nIngrese un email VALIDO: ')
    fullname=input('Ingrese el el fullname: ')
    tipousuario=input('Ingrese el tipo de usuario: ')
    data=(usuario,password,email,fullname,tipousuario)
    try:
        ctr.insertUser(data)
    except Exception as e:
         print("Error al ingresar data")
         print(e)

def updateUser():
    clear()
    idUsuario = int(input("Ingrese el ID del usuario: ")) 
    if ctr.existeUsuario(idUsuario)==True:
        if ctr.esContraseniaDelUser(idUsuario,input('Ingrese la password: '))==True:
            print("Permiso concedido, se procederá a actualizar los datos.")
            usuario=input('Ingrese el nuevo nombre de usuario: ')
            password=input('Ingrese la nueva password: ')
            email=input('Ingrese el nuevo email: ')
            while esEmail(email)==False:
                email=input('\nIngrese un email VALIDO: ')
            fullname=input('Ingrese el nuevo fullname: ')
            score=int(input('Ingrese el nuevo score: '))
            tipousuario=input('Ingrese el nevo data tipousuario: ')
            data=(usuario,password,email,fullname,score,tipousuario,idUsuario)
            try:
                ctr.updateUser(data)
            except Exception as e:
                print('Hubo una excepcion al momento de hacer un Update de Usuario')
                print(e)
        else:
            print("Contraseña incorrecta, cancelando operacion")
    else:
        print("No existe dicho usuario.")

def deleteUser():
    clear()
    idUsuario = int(input("Ingrese el ID del usuario: ")) 
    if ctr.existeUsuario(idUsuario)==True:
        if ctr.esContraseniaDelUser(idUsuario,input('Ingrese la password: '))==True:
            print("Permiso concedido, se procederá a eliminar los datos.")
            try:
                ctr.deleteUser(idUsuario)
            except Exception as e:
                print ('Error al intentar eliminar al usuario')
                print(e)
        else:
            print("Contraseña incorrecta, cancelando operacion")
    else:
        print("No existe dicho usuario.")

def listUser():
    clear()
    data=ctr.controllerUser()
    for row in data:
        print(row)

def esEmail(email):
    if(re.search('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}',email)):   
        return True
    else:   
        return False

if __name__=='__main__':
    clear()
    # Menu Iterativo para la ADMINISTRACION DE USUARIOS (Insert, Delete y Update)
    while True:
        print("""
Menu Iterativo para la ADMINISTRACION DE USUARIOS (Insert, Delete y Update)        
                1) Insert Usuario
                2) Update Usuario
                3) Delete Usuario
                4) Ver Lista de Usuarios
                5) Salir
                """
        )
        opc=int(input('Ingrese la tarea a realizar: '))
        if(opc==1):
            registerUser()
        elif(opc==2):
            updateUser()
        elif(opc==3):
            deleteUser()
        elif(opc==4):
            listUser()
        elif(opc==5):
            print("Gracias por usar la aplicacion")
            break
        else:
            print("Opcion desconocida, vuelva a intentarlo")

