# -*- coding: utf-8 -*-.

from app.models.db import db
from app.models.user import User
from app.models.category import Category


class Service(db.Model):
    '''Clase que define el modelo Servicio'''

    __tablename__ = 'service'
    serviceId = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(100), unique=True)
    category = db.Column(db.String(30), db.ForeignKey('category.name'))
    user = db.Column(db.String(30), db.ForeignKey('user.email'))

    def __init__(self, name=None, category=None, user=None):
        '''Constructor del modelo servicio'''
        self.name = name
        self.category = category
        self.user = user

    def __repr__(self):
        '''Representacion en string del modelo servicio'''
        return \
            '<name %r, category %r, user %r >' % (
                self.name, self.category, self.user)

    def getServices(self):
        '''Permite obtener todos los servicios'''

        result = self.query.all()
        return result

    def getServicesByUser(self,user):
        '''Permite obtener todos los servicios'''

        result = self.query.filter_by(user=user).all()
        return result

    def getServicesByCategory(self, category):
        '''Permite obtener todos los servicios'''

        result = self.query.filter_by(category=category).all()
        return result

    def getServiceById(self, id):
        '''Permite buscar un servicio por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            service = self.query.filter_by(serviceId=id).all()
            if service == []:
                return []
            return service[0]

    def getServiceByName(self, name):
        '''Permite buscar un servicio por nombre'''

        service = self.query.filter_by(name=name).all()

        if service:
            serv = service[0]
        else:
            serv = None

        return serv

    def createService(self, name, category, user):
        '''Permite insertar un servicio'''

        # None checks
        name = name or ""
        category = category or ""
        user = user or ""

        findService = self.getServiceByName(name)

        if findService is None:

            c = Category()
            findCategory = c.getCategoryByName(category)

            if findCategory != None:

                u = User()
                findUser = u.getUserByEmail(user)

                if findUser != []:

                    newService = Service(name, category, user)
                    db.session.add(newService)
                    db.session.commit()
                    return {'status': 'success', 'reason': 'Service Created'}

                else:
                    return {'status': 'failure', 'reason': 'User not found'}
            else:
                return {'status': 'failure', 'reason': 'Category not found'}

        return {'status': 'failure', 'reason': 'The service is already created'}

    def deleteService(self, id):
        '''Permite eliminar un servicio'''

        findService = self.getServiceById(id)

        if findService != []:
            self.query.filter_by(serviceId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'Service deleted'}

        return {'status': 'failure', 'reason': 'Couldnt find service :('}

    def updateService(self, serviceId, name=None, category=None, user=None):
        '''Permite actualizar un servicio'''

        # None checks
        name = name or ""
        category = category or ""
        user = user or ""

        findService = self.getServiceById(serviceId)

        if findService != []:

            if name != "":
                newName = name
            else:
                newName = findService.name

            if category != "":
                c = Category()
                findCategory = c.getCategoryByName(category)

                if findCategory != None:
                    newCategory = category
                else:
                    return {'status': 'failure', 'reason': 'Category not found'}
            else:
                newCategory = findService.category

            if user != "":
                u = User()
                findUser = u.getUserByEmail(user)

                if findUser != []:
                    newUser = user
                else:
                    return {'status': 'failure', 'reason': 'User not found'}
            else:
                newUser = findService.user

            findService.name = newName
            findService.category = newCategory
            findService.user = newUser
            db.session.commit()
            return {'status': 'success', 'reason': 'Service updated'}

        return {'status': 'failure', 'reason': 'Service does not exist, use create instead'}
