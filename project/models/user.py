import db

class ModelUser():
    def __init__(self):
        print('model user')
        self.db=db.Conection('tienda.db')

    def getUser(self):
        cursor=self.db.getCursor()
        data=cursor.execute('select * from USUARIOS').fetchall()
        return data
    
    def insertUser(self,data):
        inserSentence="INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES(?,?,?,?,0,?)"
        cursor=self.db.getCursor()
        cursor.execute(inserSentence,data)
        self.db.con.commit()

    def updateUser(self,data):
        query ="UPDATE USUARIOS SET USUARIO =?,PASSWORD =?,EMAIL=?,FULLNAME=?,SCORE=?, TIPOUSUARIO=? WHERE ID = ?"
        cursor=self.db.getCursor()
        cursor.execute(query,data)
        self.db.con.commit()

    def deleteUser(self,id_User):
        query ="DELETE FROM USUARIOS WHERE ID ="+str(id_User)
        cursor=self.db.getCursor()
        cursor.execute(query)
        self.db.con.commit()

    def existeUsuario(self,id_User):
        query="SELECT * FROM USUARIOS WHERE ID ="+str(id_User)
        cursor=self.db.getCursor()
        if(len(cursor.execute(query).fetchall())>=1):
            return True
        else:
            return False
        
    def esContraseniaDelUser(self,id_User,passwordUser):
        query="SELECT * FROM USUARIOS WHERE ID = "+str(id_User)+" AND PASSWORD= '"+str(passwordUser)+"'"
        cursor=self.db.getCursor()
        if(len(cursor.execute(query).fetchall())>=1):
            return True
        else:
            return False

