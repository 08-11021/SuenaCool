import logging

from app import properties
from app.models.db import db


class Band(db.Model):
    __tablename__ = 'band'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(30))
    state = db.Column(db.Integer, db.ForeignKey('state.id'))
    pic = db.Column(db.String(200))
    review = db.Column(db.String(5000))

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def __repr__(self):
        return \
            '<name %r, state %r' % (
                self.name, self.state)

    def createBand(self, name, state):
        logging.info('Creando Banda: %r' % name)

        checkBandName = len(name) <= properties.maxBandName

        if checkBandName:

            band = Band(name, state)
            band.save()

        logging.info('Banda creada')


    def getBands(self):
        logging.info("Obteniendo bandas")
        result = self.query.all()
        return result

    def getBandsByStateId(self, state):
        logging.info('Obteniendo bandas por estado: %r' % state)
        bands = self.query.filter_by(state=state).all()
        return bands

    def getBandsByName(self, name):
        logging.info('Obteniendo bandas por nombre: %r' % name)
        bands = self.query.filter(Band.name.like("%name%")).all()
        return bands

    def getBandById(self, id):
        logging.info('Obteniendo banda por id: %r' % id)
        band = self.query.filter_by(id=id).first()
        return band

    def setBandPic(self, pic):
        self.pic = pic

    def setBandReview(self, review):
        self.review = review

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
        band = self.getBandById(self.id)
        db.session.delete(band)
        try:
            db.session.commit()
        except:
            db.session.rollback()
