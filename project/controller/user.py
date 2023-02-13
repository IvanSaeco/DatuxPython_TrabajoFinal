import models.user as md

def controllerUser():
    user=md.ModelUser()
    data=user.getUser()
    return data

def insertUser(data):
    user=md.ModelUser()
    user.insertUser(data)

def updateUser(data):
    user=md.ModelUser()
    user.updateUser(data)

def deleteUser(id_User):
    user=md.ModelUser()
    user.deleteUser(id_User)

def existeUsuario(id_User):
    user=md.ModelUser()
    return user.existeUsuario(id_User)

def esContraseniaDelUser(id_User,passwordUser):
    user=md.ModelUser()
    return user.esContraseniaDelUser(id_User,passwordUser)