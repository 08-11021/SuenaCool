# -*- coding: utf-8 -*-.

from app.models.db import db
from app.models.user import User
from app.models.service import Service


class Quotation(db.Model):
    '''Clase que define el modelo cotizacion'''

    __tablename__ = 'quotation'
    quotationId = db.Column(db.Integer, primary_key=True, index=True)
    service = db.Column(db.Integer, db.ForeignKey('service.serviceId'))
    client = db.Column(db.Integer, db.ForeignKey('user.userId'))
    operator = db.Column(db.Integer, db.ForeignKey('user.userId'))
    price = db.Column(db.Float)

    def __init__(self, service=None, client=None, operator=None, price=None):
        '''Constructor del modelo cotizacion'''
        self.service = service
        self.client = client
        self.operator = operator
        self.price = price

    def __repr__(self):
        '''Representacion en string del modelo cotizacion'''
        return \
            '<service %r, client %r, operator %r price %r>' % (
                self.service, self.client, self.operator, self.price)

    def getQuotations(self):
        '''Permite obtener todas las cotizaciones'''

        result = self.query.all()
        return result

    def getQuotationById(self, id):
        '''Permite buscar una cotizacion por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            quotation = self.query.filter_by(quotationId=id).all()
            if quotation == []:
                return []
            return quotation[0]

    def checkQuotation(self, service, client, operator):
        '''Permite buscar una cotizacion dado el servicio, cliente y operador'''

        quotation = self.query.filter_by(
            service=service, client=client, operator=operator).all()
        if quotation == []:
            return []
        return quotation[0]

    def createQuotation(self, service, client, operator, price):
        '''Permite insertar una cotizacion'''

        # None checks
        service = service or ""
        client = client or ""
        operator = operator or ""
        price = price or ""

        if client != operator:
            checkQuotation = self.checkQuotation(service, client, operator)

            if checkQuotation == []:
                s = Service()
                findService = s.getServiceById(service)

                if findService != []:
                    u = User()
                    findClient = u.getUserById(client)

                    if findClient != []:
                        findOperator = u.getUserById(operator)
                        print(findOperator)

                        if findOperator != []:
                            checkServOpe = s.query.filter_by(
                                serviceId=service, user=findOperator[0].email).all()

                            if checkServOpe != []:
                                if (price > 0):
                                    newQuotation = Quotation(
                                        service, client, operator, price)
                                    db.session.add(newQuotation)
                                    db.session.commit()
                                    return {'status': 'success', 'reason': 'Quotation Created'}

                                else:
                                    return {'status': 'failure', 'reason': 'Price cant be negative'}
                            else:
                                return {'status': 'failure', 'reason': 'Operator doesnt offer that service'}
                        else:
                            return {'status': 'failure', 'reason': 'Operator not found'}
                    else:
                        return {'status': 'failure', 'reason': 'Client not found'}
                else:
                    return {'status': 'failure', 'reason': 'Service not found'}
            else:
                return {'status': 'failure', 'reason': 'The quotation is already created'}
        else:
            return {'status': 'failure', 'reason': 'The client and operator cant be the same'}

    def deleteQuotation(self, id):
        '''Permite eliminar una cotizacion'''

        findQuotation = self.getQuotationById(id)

        if findQuotation != []:
            self.query.filter_by(quotationId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'Quotation deleted'}

        return {'status': 'failure', 'reason': 'Couldnt find quotation :('}

    def updateQuotation(self, quotationId, service=None, client=None, operator=None, price=None):
        '''Permite actualizar una cotizacion'''

        # None checks
        service = service or ""
        client = client or ""
        operator = operator or ""
        price = price or ""

        findQuotation = self.getQuotationById(quotationId)

        if findQuotation != []:

            if service != "":
                s = Service()
                findService = s.getServiceById(service)

                if findService != []:
                    newService = service
                else:
                    return {'status': 'failure', 'reason': 'Service not found'}
            else:
                newService = findQuotation.service

            if client != "":
                c = User()
                findClient = c.getUserById(client)

                if findClient != []:
                    newClient = client
                else:
                    return {'status': 'failure', 'reason': 'Client not found'}
            else:
                newClient = findQuotation.client

            if operator != "":
                o = User()
                findOperator = o.getUserById(operator)

                if findOperator != []:
                    newOperator = operator
                else:
                    return {'status': 'failure', 'reason': 'Operator not found'}
            else:
                newOperator = findQuotation.operator

            if price != "":
                newPrice = price
            else:
                newPrice = findQuotation.price

            if newClient != newOperator:
                u = User()
                checkOpe = u.getUserById(newOperator)
                s2 = Service()
                checkServOpe = s2.query.filter_by(
                    serviceId=newService, user=checkOpe[0].email).all()

                if checkServOpe != []:
                    if (newPrice > 0):
                        findQuotation.service = newService
                        findQuotation.client = newClient
                        findQuotation.operator = newOperator
                        findQuotation.price = newPrice
                        db.session.commit()
                        return {'status': 'success', 'reason': 'Quotation updated'}

                    else:
                        return {'status': 'failure', 'reason': 'Price cant be negative'}
                else:
                    return {'status': 'failure', 'reason': 'Operator doesnt offer that service'}

            else:
                return {'status': 'failure', 'reason': 'The client and the operator cant be the same'}
        else:
            return {'status': 'failure', 'reason': 'Quotation does not exist, use create instead'}
