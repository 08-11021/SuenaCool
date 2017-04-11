from flask import Blueprint, json, request, session
import hashlib

from app.models.user import User
from app.utility.encoder import toMd5

auth = Blueprint('auth', __name__,)

USER_ROLES = {'admin': 1, 'operator': 2, 'client':4, 'director': 8, 'manager':16, 'budget':32}

@auth.route('/user/check', methods=['GET'])
def check_session():
    permissions = {0: '/',
                   1: '/home'}
    securityLvl = int(request.args.get('securityLvl'))
    if "rol" in session:
        if (session["rol"] & securityLvl) != 0:
            res = {'actorName': session['name'],
                   'actorRol': session['rol'],
                   'actorId': session['userId'],
                   'actorEmail': session['email'],
                   }
        else:
            res = {'actorName': session['name'],
                   'actorRol': session['rol'],
                   'actorId': session['userId'],
                   'actorEmail': session['email'],
                   'redirect': permissions[1]}
    else:
        if securityLvl == 0:
            res = {'actorName': 'Usuario no registrado', 'actorRol': 0}
        else:
            res = {'actorName': 'Usuario no registrado', 'actorRol': 0, 'redirect':permissions[0]}
    return json.dumps(res)


@auth.route('/user/logout', methods=['GET'])
def logout():
    if "name" in session:
        session.pop("name", None)
        session.pop("rol", None)
        session.pop("userId", None)
        session.pop("email", None)
    return json.dumps({})


@auth.route('/user/authenticate', methods=['POST'])
def authenticate_user():
    results = [{'error': 'Este usuario no está registrado!!'},
               {'error': 'Contraseña invalida!!'}]
    email = request.args.get('email')
    password = request.args.get('password')

    if "actor" in session:
        session.pop("rol", None)
        session.pop("name", None)
        session.pop("userId", None)
        session.pop("email", None)

    if request.args.get('email') is None or len(request.args.get('email')) == 0:
        res = {'error': 'Debe introducir email y password'}
    elif request.args.get('password') is None or len(request.args.get('password')) == 0:
        res = {'error': 'Debe introducir email y password'}
    else:
        UserInstance = User()
        users = UserInstance.getUserByEmail(email)
        if not users:
            res = results[0]
        else:
            user = users[0]
            if user.password == toMd5(password.encode('utf-8')):
                session['name'] = user.fullname
                session['rol'] = user.rol
                session['userId'] = user.userId
                session['email'] = user.email
                res = {'rol': user.rol}
            else:
                res = results[1]

    return json.dumps(res)
