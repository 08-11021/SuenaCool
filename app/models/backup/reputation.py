# -*- coding: utf-8 -*-.

from app.models.db import db
from app.models.user import User
from app.models.contract import Contract

CONST_MIN_VALUE = 1
CONST_MAX_VALUE = 5

class Reputation(db.Model):
    '''Clase que define el modelo reputacion'''

    __tablename__   = 'reputation'
    reputationId    = db.Column(db.Integer, primary_key=True, index=True)
    contract        = db.Column(db.Integer, db.ForeignKey('contract.contractId'))
    user            = db.Column(db.Integer, db.ForeignKey('user.userId'))
    ratedUser       = db.Column(db.Integer, db.ForeignKey('user.userId'))
    value           = db.Column(db.Integer)

    def __init__(self, contract=None, user=None, ratedUser=None, value=None):
        '''Constructor del modelo reputacion'''
        self.contract    = contract
        self.user       = user
        self.ratedUser  = ratedUser
        self.value      = value

    def __repr__(self):
        '''Representacion en string del modelo reputacion'''
        return \
            '<contract %r, user %r, ratedUser %r value %r>' % (
                self.contract, self.user, self.ratedUser, self.value)

    def getReputations(self):
        '''Permite obtener todas las reputaciones'''

        result = self.query.all()
        return result

    def getReputationById(self, id):
        '''Permite buscar una reputacion por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            reputation = self.query.filter_by(reputationId=id).all()
            if reputation == []:
                return []
            return reputation[0]

    def getReputationFromUser(self, user):
        '''Permite calcular una reputacion de un usuario'''

        if (type(user) != int):
            return {'status': 'failure', 'reason': ' User not integer'}
        else:
            totalRep = self.query.filter_by(ratedUser=user).all()
            if totalRep != []:
                rep = 0
                numRep = 0
                for i in totalRep:
                    rep = rep + i.value
                    numRep = numRep + 1

                return rep/numRep  
            else:
                return {'status': 'failure', 'reason': 'This user doesnt have reputation'}
                

    def createReputation(self, contract, user, ratedUser, value):
        '''Permite insertar una reputacion'''

        # None checks
        contract    = contract or ""
        user        = user or ""
        ratedUser   = ratedUser or ""
        value       = value or ""

        if user != ratedUser:
            u = User()
            findUser = u.getUserById(user)

            if findUser != []:
                findRatedUser = u.getUserById(ratedUser)

                if findRatedUser != []:

                    if (findUser[0].rol & 2) == 2:
                        operator = findUser[0]
                        client = findRatedUser[0]
                    else:
                        if (findRatedUser[0].rol & 2) == 2:
                            operator = findRatedUser[0]
                            client = findUser[0]
                        else:
                            return {'status': 'failure', 'reason': 'None of the users is a operator'}

                    c = Contract()
                    checkContract = c.getContractById(contract)

                    if checkContract != []:

                        if ((checkContract.client == client.userId) and (checkContract.operator == operator.userId)):

                            if ((value >= CONST_MIN_VALUE) and (value <= CONST_MAX_VALUE)):

                                newReputation = Reputation(contract, user, ratedUser, value)
                                db.session.add(newReputation)
                                db.session.commit()
                                return {'status': 'success', 'reason': 'Reputation Created'}

                            else:
                                return {'status': 'failure', 'reason': 'Value must be between 1 and 5'}
                        else:
                            return {'status': 'failure', 'reason': 'User and ratedUser doens match the contract'}  
                    else:
                        return {'status': 'failure', 'reason': 'Contract not found'}
                else:
                    return {'status': 'failure', 'reason': 'RatedUser not found'}
            else:
                return {'status': 'failure', 'reason': 'User not found'}
            
        else:
            return {'status': 'failure', 'reason': 'The user and ratedUser cant be the same'}



    def deleteReputation(self, id):
        '''Permite eliminar una reputacion'''

        findReputation = self.getReputationById(id)

        if findReputation != []:
            self.query.filter_by(reputationId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'Reputation deleted'}

        return {'status': 'failure', 'reason': 'Couldnt find reputation :('}


    def updateReputation(self, reputationId, contract=None, user=None, ratedUser=None, value=None):
        '''Permite actualizar una reputacion'''

        # None checks
        contract    = contract or ""
        user        = user or ""
        ratedUser   = ratedUser or ""
        value       = value or ""

        findReputation = self.getReputationById(reputationId)

        if findReputation != []:

            if contract != "":
                c = Contract()
                findContract = c.getContractById(contract)

                if findContract != []:
                    newContract = contract
                else:
                    return {'status': 'failure', 'reason': 'Contract not found'}
            else:
                newContract = findReputation.contract

            if user != "":
                u = User()
                findUser = u.getUserById(user)

                if findUser != []:
                    newUser = user
                else:
                    return {'status': 'failure', 'reason': 'User not found'}
            else:
                newUser = findReputation.user

            if ratedUser != "":
                u2 = User()
                findRatedUser = u2.getUserById(ratedUser)

                if findRatedUser != []:
                    newRatedUser = ratedUser
                else:
                    return {'status': 'failure', 'reason': 'RatedUser not found'}
            else:
                newRatedUser = findReputation.ratedUser

            if value != "":
                if ((value >= CONST_MIN_VALUE) and (value <= CONST_MAX_VALUE)):
                    newValue = value
                else:
                    return {'status': 'failure', 'reason': 'Value must be between 1 and 5'} 
            else:
                newValue = findReputation.value

            if newUser != newRatedUser:

                u3 = User()
                findUser2 = u3.getUserById(newUser)
                findRatedUser2 = u3.getUserById(newRatedUser)

                if (findUser2[0].rol & 2) == 2:
                    operator = findUser2[0]
                    client = findRatedUser2[0]
                else:
                    if (findRatedUser2[0].rol & 2) == 2:
                        operator = findRatedUser2[0]
                        client = findUser2[0]
                    else:
                        return {'status': 'failure', 'reason': 'None of the users is a operator'}

                c2 = Contract()
                checkContract = c2.getContractById(newContract)

                if ((checkContract.client == client.userId) and (checkContract.operator == operator.userId)):
                    findReputation.contract     = newContract
                    findReputation.user         = newUser
                    findReputation.ratedUser    = newRatedUser
                    findReputation.value        = newValue
                    db.session.commit()
                    return {'status': 'success', 'reason': 'Reputation updated'}

                else:
                    return {'status': 'failure', 'reason': 'User and ratedUser doens match the contract'}
            else:
                return {'status': 'failure', 'reason': 'The user and the ratedUser cant be the same'}
        else:
            return {'status': 'failure', 'reason': 'Reputation does not exist, use create instead'}
