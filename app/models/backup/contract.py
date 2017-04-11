# -*- coding: utf-8 -*-.

from app.models.db import db
from app.models.user import User
from app.models.service import Service
from app.models.quotation import Quotation

import datetime

class Contract(db.Model):
    '''Clase que define el modelo contrato'''

    __tablename__   = 'contract'
    contractId      = db.Column(db.Integer, primary_key=True, index=True)
    service         = db.Column(db.Integer, db.ForeignKey('service.serviceId'))
    client          = db.Column(db.Integer, db.ForeignKey('user.userId'))
    operator        = db.Column(db.Integer, db.ForeignKey('user.userId'))
    price           = db.Column(db.Float)
    payment         = db.Column(db.Float)
    date            = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, service=None, client=None, operator=None, price=None, payment=None):
        '''Constructor del modelo contrato'''
        self.service    = service
        self.client     = client
        self.operator   = operator
        self.price      = price
        self.payment    = payment

    def __repr__(self):
        '''Representacion en string del modelo contrato'''
        return \
            '<service %r, client %r, operator %r price %r payment %r date %r>' % (
                self.service, self.client, self.operator, self.price, self.payment, self.date)

    def getContracts(self):
        '''Permite obtener todos los contratos'''

        result = self.query.all()
        return result

    def getContractById(self, id):
        '''Permite buscar un contrato por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            contract = self.query.filter_by(contractId=id).all()
            if contract == []:
                return []
            return contract[0]

    def checkContract(self,contractId,client,operator):
        '''Permite verificar si un contrato existe con ese cliente y operador'''

        contract = self.query.filter_by(contractId=contractId,client=client,operator=operator).all()
        if contract == []:
            return []
        return contract[0]

    def createContract(self, service, client, operator, price, payment):
        '''Permite insertar un contrato'''

        # None checks
        service     = service or ""
        client      = client or ""
        operator    = operator or ""
        price       = price or ""
        payment     = payment or ""

        if client != operator:
            s = Service()
            findService = s.getServiceById(service)

            if findService != []:
                u = User()
                findClient = u.getUserById(client)

                if findClient != []:
                    findOperator = u.getUserById(operator)

                    if findOperator != []:
                        checkServOpe = s.query.filter_by(serviceId=service,user=findOperator[0].email).all()

                        if checkServOpe !=[]:
                            q = Quotation()
                            checkQuotation = q.checkQuotation(service,client,operator) 

                            if checkQuotation !=[]:

                                if ((payment > 0)and(price > 0)):

                                    if(payment >= (price/2)):

                                        newContract = Contract(service, client, operator, price, payment)
                                        db.session.add(newContract)
                                        db.session.commit()
                                        return {'status': 'success', 'reason': 'Contract Created'}
                    
                                    else:
                                        return {'status': 'failure', 'reason': 'Payment must be at least 50%'}
                                else:
                                    return {'status': 'failure', 'reason': 'Payment and price cant be negative'}
                            else:
                                return {'status': 'failure', 'reason': 'Quotation doesnt exist'}
                        else:
                            return {'status': 'failure', 'reason': 'Operator doesnt offer that service'}
                    else:
                        return {'status': 'failure', 'reason': 'Operator not found'}
                else:
                    return {'status': 'failure', 'reason': 'Client not found'}
            else:
                return {'status': 'failure', 'reason': 'Service not found'}
            
        else:
            return {'status': 'failure', 'reason': 'The client and operator cant be the same'}



    def deleteContract(self, id):
        '''Permite eliminar un contrato'''

        findContract = self.getContractById(id)

        if findContract != []:
            self.query.filter_by(contractId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'Contract deleted'}

        return {'status': 'failure', 'reason': 'Couldnt find contract :('}


    def updateContract(self, contractId, service=None, client=None, operator=None, price=None, payment=None):
        '''Permite actualizar un contrato'''

        # None checks
        service     = service or ""
        client      = client or ""
        operator    = operator or ""
        price       = price or ""
        payment     = payment or ""

        findContract= self.getContractById(contractId)

        if findContract != []:

            if service != "":
                s = Service()
                findService = s.getServiceById(service)

                if findService != []:
                    newService = service
                else:
                    return {'status': 'failure', 'reason': 'Service not found'}
            else:
                newService = findContract.service

            if client != "":
                c = User()
                findClient = c.getUserById(client)

                if findClient != []:
                    newClient = client
                else:
                    return {'status': 'failure', 'reason': 'Client not found'}
            else:
                newClient = findContract.client

            if operator != "":
                o = User()
                findOperator = o.getUserById(operator)

                if findOperator != []:
                    newOperator = operator
                else:
                    return {'status': 'failure', 'reason': 'Operator not found'}
            else:
                newOperator = findContract.operator

            if price != "":
                newPrice = price
            else:
                newPrice = findContract.price

            if payment != "":
                newPayment = payment
            else:
                newPayment = findContract.payment

            if newClient != newOperator:
                u = User()
                checkOpe = u.getUserById(newOperator)
                s2 = Service()
                checkServOpe = s2.query.filter_by(serviceId=newService,user=checkOpe[0].email).all()

                if checkServOpe !=[]:
                    q = Quotation()
                    checkQuotation = q.checkQuotation(newService,newClient,newOperator) 

                    if checkQuotation !=[]:

                        if ((newPayment > 0)and(newPrice > 0)):

                            if (newPayment >= (newPrice/2)):
                                findContract.service   = newService
                                findContract.client    = newClient
                                findContract.operator  = newOperator
                                findContract.price     = newPrice
                                findContract.payment   = newPayment
                                db.session.commit()
                                return {'status': 'success', 'reason': 'Contract updated'}

                            else:
                                return {'status': 'failure', 'reason': 'Payment must be at least 50%'}
                        else:
                            return {'status': 'failure', 'reason': 'Payment and price cant be negative'}
                    else:
                        return {'status': 'failure', 'reason': 'Quotation doesnt exist'}
                else:
                    return {'status': 'failure', 'reason': 'Operator doesnt offer that service'}
            else:
                return {'status': 'failure', 'reason': 'The client and the operator cant be the same'}
        else:
            return {'status': 'failure', 'reason': 'Contract does not exist, use create instead'}