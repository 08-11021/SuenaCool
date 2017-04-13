from flask import Blueprint, json, request, session

from app.models.user import User
from app.utility.encoder import toMd5
from app.utility.util import checkLenght

user = Blueprint('user', __name__,)
USER_ROLES = {'admin': 1, 'user': 2}

'''Crear nuevo usuario'''
@user.route('/user', methods=['POST'])
def createUser():
    email = request.args.get('email')
    fullName = request.args.get('fullName')
    rol = request.args.get('rol')
    password = request.args.get('password')

    if checkLenght(email) == 0:
        if checkLenght(password):
            encodedPassword = toMd5(password.encode('utf-8'))
            res = User.createUser(
                email, fullName, encodedPassword, int(rol))
        else:
            res = {'status': 'failure', 'msg': 'Debe introducir email y password'}
    else:
        res = {'status': 'failure', 'msg': 'Debe introducir email y password'}

    return json.dumps(res)

'''obtener usuario'''
@user.route('/user/<int:user_id>', methods=['GET'])
def getUser(user_id):
    id = user_id
    user = User.getUserById(id)[0]
    res = {'id': user.userId,
           'rol': user.rol,
           'email': user.email,
           'fullName': user.fullname}

    return json.dumps(res)

'''actualizar informacion de usuario'''
@user.route('/user/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    email = request.args.get('email')
    password = request.args.get('password')
    fullname = request.args.get('fullName')
    rol = request.args.get('rol')

    user = User.getUserById(user_id)
    if user.password == toMd5(password.encode('utf-8')) and user.email == email:
        user.fullname = fullname
        user.rol = rol
        res = user.update()
    else:
        res = {'status': 'failure', 'msg': 'Clave invalida'}
    return json.dumps(res)

'''borrar usuario'''
@user.route('/user/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    user = User.getUserById(user_id)
    try:
        result = user.delete()
    except:
        result = {'status': 'failure', 'msg': 'Error al eliminar el usuario'}
    return result

'''obtener lista de usuarios'''
@user.route('/users', methods=['GET'])
def getUsers():
    users = User.getUsers()
    result = []
    for user in users:
        result.append(
            {'id': user.userId,
             'fullName': user.fullname,
             'email': user.email,
             'rol': user.rol
             })
    res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''cambiar password de usuario'''
@user.route('/user/<int:user_id>/changePassword', methods=['PUT'])
def changePassword(user_id):
    email = request.args.get('email')
    password = request.args.get('password')
    newPasswordr1 = request.args.get('passwordr1')
    newPasswordr2 = request.args.get('passwordr2')

    passwordLength = checkLenght(newPasswordr1)
    user = User.getUserById(user_id)
    if user.password == toMd5(password.encode('utf-8')) and user.email == email:
        if newPasswordr1 == newPasswordr2 and passwordLength:
            user.password = toMd5(newPasswordr1.encode('utf-8'))
            user.update()
            res = {'status': 'success', 'msg': 'La clave ha sido actualizada'}
        else:
            res = {'status': 'failure', 'msg': 'Las claves no coinciden'}
    else:
        res = {'status': 'failure', 'msg': 'Clave invalida'}
    return json.dumps(res)








