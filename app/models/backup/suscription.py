# -*- coding: utf-8 -*-.

from app.models.db import db
from app.models.user import User
from app.models.category import Category


class Suscription(db.Model):
    '''Clase que define el modelo suscripcion'''

    __tablename__ = 'suscription'
    suscriptionId = db.Column(db.Integer, primary_key=True, index=True)
    category = db.Column(db.String(30), db.ForeignKey('category.name'))
    user = db.Column(db.String(30), db.ForeignKey('user.email'))

    def __init__(self, category=None, user=None):
        '''Constructor del modelo suscripcion'''
        self.category = category
        self.user = user

    def __repr__(self):
        '''Representacion en string del modelo suscripcion'''
        return \
            '<category %r, user %r >' % (
                self.category, self.user)

    def getSuscriptionsByUser(self,user):
        '''Permite obtener todos las suscripciones de un usuario'''

        result = self.query.filter_by(user=user).all()
        return result

    def getSuscriptionByCategoryUser(self,category, user):
        '''Permite obtener todos la suscripcion de un usuario a una categoria'''

        result = self.query.filter_by(user=user).filter_by(category=category).all()
        return result

    def getSuscriptionById(self, id):
        '''Permite buscar una suscripcion por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            suscriptions = self.query.filter_by(suscriptionId=id).all()
            if suscriptions == []:
                return []
            return suscriptions[0]

    def createSuscription(self, category, user):
        '''Permite insertar un suscripcion'''

        # None checks
        category = category or ""
        user = user or ""

        findSuscription = self.getSuscriptionByCategoryUser(category, user)

        if findSuscription == []:

            c = Category()
            findCategory = c.getCategoryByName(category)

            if findCategory != None:

                u = User()
                findUser = u.getUserByEmail(user)

                if findUser != []:

                    newSuscription = Suscription(category, user)
                    db.session.add(newSuscription)
                    db.session.commit()
                    return {'status': 'success', 'reason': 'Suscription Created'}

                else:
                    return {'status': 'failure', 'reason': 'User not found'}
            else:
                return {'status': 'failure', 'reason': 'Category not found'}

        return {'status': 'failure', 'reason': 'The suscription is already created'}

    def deleteSuscription(self, id):
        '''Permite eliminar una suscripcion'''

        findSuscription = self.getSuscriptionById(id)

        if findSuscription != []:
            self.query.filter_by(suscriptionId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'Suscription deleted'}

        return {'status': 'failure', 'reason': 'Couldnt find suscription :('}

    def updateSuscription(self, suscriptionId, category=None, user=None):
        '''Permite actualizar un servicio'''

        # None checks
        category = category or ""
        user = user or ""

        findSuscription = self.getSuscriptionById(suscriptionId)

        if findSuscription != []:

            if category != "":
                c = Category()
                findCategory = c.getCategoryByName(category)

                if findCategory != None:
                    newCategory = category
                else:
                    return {'status': 'failure', 'reason': 'Category not found'}
            else:
                newCategory = findSuscription.category

            if user != "":
                u = User()
                findUser = u.getUserByEmail(user)

                if findUser != []:
                    newUser = user
                else:
                    return {'status': 'failure', 'reason': 'User not found'}
            else:
                newUser = findSuscription.user

            findSuscription.category = newCategory
            findSuscription.user = newUser
            db.session.commit()
            return {'status': 'success', 'reason': 'Suscription updated'}

        return {'status': 'failure', 'reason': 'Suscription does not exist, use create instead'}
