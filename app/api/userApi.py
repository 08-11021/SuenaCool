from flask import Blueprint, json, request, session

from app.models.user import User
from app.utility.encoder import toMd5

user = Blueprint('user', __name__,)
USER_ROLES = {'admin': 1, 'user': 2}

'''Crear nuevo usuario'''
@user.route('/user', methods=['POST'])
def create_user():
    email = request.args.get('email')
    fullName = request.args.get('fullName')
    rol = request.args.get('rol')
    password = request.args.get('password')

    if email is None or len(email) == 0:
        res = {'status': 'failure', 'msg': 'Debe introducir email y password'}
    else:
        if password is None or len(password) == 0:
            res = {'status': 'failure', 'msg': 'Debe introducir email y password'}
        else:

            userInstance = User()
            encodedPassword = toMd5(password.encode('utf-8'))
            result = userInstance.createUser(
                email, fullName, encodedPassword, int(rol))

            res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''obtener usuario'''
@user.route('/user', methods=['GET'])
def get_user():
    id = request.args.get('id')
    UserInstance = User()
    result = UserInstance.getUserById(int(id))[0]
    res = {'id': result.userId,
           'rol': result.rol,
           'email': result.email,
           'fullName': result.fullname
            }

    return json.dumps(res)

'''obtener lista de usuarios'''
@user.route('/users', methods=['GET'])
def get_users():
    UserInstance = User()
    users = UserInstance.getUsers()
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
@user.route('/user/changePassword', methods=['PUT'])
def change_password():
    email = request.args.get('email')
    password = request.args.get('password')
    newPasswordr1 = request.args.get('passwordr1')
    newPasswordr2 = request.args.get('passwordr2')

    passwordLength = not (len(newPasswordr1) == 0 or newPasswordr1 is None)
    user = User.getUserByEmail(email)
    if user.password == toMd5(password.encode('utf-8')):
        if newPasswordr1 == newPasswordr2 and passwordLength:
            user.password = toMd5(newPasswordr1.encode('utf-8'))
            user.update()
            res = {'status': 'success', 'msg': 'La clave ha sido actualizada'}
        else:
            res = {'status': 'failure', 'msg': 'Las claves no coinciden'}
    else:
        res = {'status': 'failure', 'msg': 'Clave invalida'}
    return json.dumps(res)

'''actualizar informacion de usuario'''
@user.route('/user', methods=['PUT'])
def update_user():
    email = request.args.get('email')
    password = request.args.get('password')
    fullname = request.args.get('fullName')
    rol = request.args.get('rol')

    user = User.getUserByEmail(email)
    if user.password == toMd5(password.encode('utf-8')):
        user.fullname = fullname
        user.rol = rol
        user.update()
        res = {'status': 'success', 'msg': 'La informacion de usuario ha sido actualizada'}
    else:
        res = {'status': 'failure', 'msg': 'Clave invalida'}
    return json.dumps(res)

'''borrar usuario'''
@user.route('/user', methods=['DELETE'])
def delete_user():
    userId = request.args.get('userId')
    user = User.getUserById(userId)
    try:
        user.delete()
        result = {'status': 'success', 'msg': 'Usuario eliminado'}
    except:
        result = {'status': 'failure', 'msg': 'Error al eliminar el usuario'}
    return result






