import logging

from app import properties
from app.models.db import db


class State(db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(30))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return \
            '<name %r >' % (self.name)

    def getStates(self):
        logging.info("Obteniendo estados")
        result = self.query.all()
        return result

    def createState(self, name):
        logging.info('Creando Estado: %r' % name)

        checkLongName = len(name) <= properties.maxStateName

        if checkLongName:
            foundState = self.getStatesByName(name)

            if foundState == None:
                state = State(name)
                state.save()

        logging.info('Estado creado')

    def getStateById(self, id):
        logging.info('Obteniendo estado por id: %r' % id)
        try:
            state = self.query.filter_by(id=id).first()
            return state
        except:
            return None

    def getStatesByName(self, name):
        try:
            logging.info('Obteniendo estado por nombre: %r' % name)
            state = self.query.filter(State.name.like("%" + name + "%")).all()
            return state
        except:
            return []

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def save(self):
        try:
            db.session.add(self)

            db.session.commit()
        except:
            db.session.rollback()

    def delete(self):
        try:
            state = self.getStateById(self.id)
            db.session.delete(state)

            db.session.commit()
        except:
            db.session.rollback()
