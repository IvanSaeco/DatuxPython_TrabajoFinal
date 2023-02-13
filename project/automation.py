import pandas as pd
import os
import db
import requests

def insertData():
    print("Se insertará la data más actual hasta la fecha de acuerdo con la SUNAT.")
    com_ven = requests.get('https://api.apis.net.pe/v1/tipo-cambio-sunat').json()
    data=(com_ven["compra"],com_ven["venta"],com_ven["fecha"])
    query = "INSERT INTO TASA_CAMBIO VALUES (NULL,?,?,?)"
    try:
        conn=db.Conection('tienda.db')
        cursor=conn.getCursor()
        cursor.execute(query,data).fetchall()
        conn.con.commit()
        print("La data se inserto satisfactoriamente")
    except:
        print("Ocurrio una excepcion durante la insersion de data")
    

def updateDolar():
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    iD_Tasa_Cambio=int(input('Ingrese el ID de la tasa de cambio a actualizar: '))
    if(existeID(iD_Tasa_Cambio)==True):        
        data2=(input("Ingresa el nuevo valor de compra: "), input("Ingresa el nuevo valor de venta: "), iD_Tasa_Cambio)
        query = "UPDATE TASA_CAMBIO SET COMPRA =?, VENTA=? WHERE ID_TASA_CAMBIO=?"
        try:
            cursor.execute(query,data2)
            conn.con.commit()
            print ("La data fue actualizada satisfactoriamente")
        except:
            print("Ocurrio una excepción durante el update de data")
    else:
        print("El ID ingresado NO EXISTE")


def readDolar():
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    query="SELECT * FROM TASA_CAMBIO"
    try:
        list_curs=cursor.execute(query).fetchall()

        list_ID = [list_curs[i][0] for i in range(len(list_curs))]
        list_COMPRA = [list_curs[i][1] for i in range(len(list_curs))]
        list_VENTA = [list_curs[i][2] for i in range(len(list_curs))]
        list_FECHA = [list_curs[i][3] for i in range(len(list_curs))]

        dict = {"ID_TASA_CAMBIO" :  list_ID,
                "COMPRA": list_COMPRA,
                "VENTA": list_VENTA,
                "FECHA": list_FECHA}
        
        print(pd.DataFrame(dict))
    except:
        print("Ocurrio una excepcion durante la lectura")


def existeID(iD_Tasa_Cambio):
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    query="SELECT ID_TASA_CAMBIO FROM TASA_CAMBIO WHERE ID_TASA_CAMBIO ="+str(iD_Tasa_Cambio)
    try:
        if(len(cursor.execute(query).fetchall()) >= 1):
            return True
        else:
            return False
    except:
        print("Ocurrio una excepcion verificando la existencia del ID_TASA_CAMBIO")
        return False


# Menu Iterativo para la insercion y actualizacion de data (compra-venta de dolares)
while True:
    print("""
            1) Insert data
            2) Update data del dolar
            3) Read data ingresada
            4) Salir
            """
    )
    opc=int(input('Ingrese la tarea a realizar: '))
    if(opc==1):
        insertData()
    elif(opc==2):
        updateDolar()
    elif(opc==3):
        readDolar()
    elif(opc==4):
        print("Gracias por usar la aplicacion")
        break
    else:
        print("Opcion desconocida, vuelva a intentarlo")