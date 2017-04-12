import logging

from app import properties
from app.models.db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(30), unique=True)
    fullname = db.Column(db.String(50))
    password = db.Column(db.String(200))
    rol = db.Column(db.Integer)

    def __init__(self, email, fullname, password, rol):
        self.email = email
        self.fullname = fullname
        self.password = password
        self.rol = rol

    def __repr__(self):
        return \
            '<fullname %r, email %r, password %r, rol %r >' % (
                self.fullname, self.email, self.password, self.rol)

    def getUsers(self):
        logging.info("Obteniendo usuarios")
        result = self.query.all()
        return result

    def getUserByEmail(self, email):
        logging.info('Obteniendo usuario por email: %r' % email)
        user = self.query.filter_by(email=email).first()
        return user

    def getUserById(self, id):
        logging.info('Obteniendo usuario por id: %r' % id)
        user = self.query.filter_by(id=id).first()
        return user

    def createUser(self, email, fullname, password, rol):
        logging.info('Creando Usuario: %r' % email)
        rol = rol or 1

        checkLongEmail = len(email) <= properties.maxEmail
        checkLongFullname = len(fullname) <= properties.maxFullName
        checkLongPassword = len(password) <= properties.maxPassword

        if checkLongEmail and checkLongFullname and checkLongPassword:
            foundUser = self.getUserByEmail(email)

            if foundUser == None:
                user = User(email, fullname, password, rol)
                user.save()
                logging.info('Usuario creado')
                result = {'status': 'success', 'msg': 'El usuario fue creado exitosamente'}
            else:
               result = {'status': 'failure', 'msg': 'El usuario ya existe'}
        else:
            result = {'status': 'failure', 'msg': 'Los campos no pueden ser vacios'}
        return result

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def delete(self):
        user = self.getUserById(self.id)
        db.session.delete(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
