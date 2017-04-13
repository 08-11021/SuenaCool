import datetime
import logging

from sqlalchemy import and_

from app import properties
from app.models.db import db


class Disc(db.Model):
    __tablename__ = 'disc'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(60))#not null
    date = db.Column(db.DateTime, default=datetime.datetime.now()) #not null
    genre = db.Column(db.String(60)) #not null
    score = db.Column(db.Integer)
    band = db.Column(db.Integer, db.ForeignKey('band.id')) #not null
    cover = db.Column(db.String(200))
    review = db.Column(db.String(5000))

    def __init__(self, name, date, genre, band):
        self.name = name
        self.date = date
        self.genre = genre
        self.band = band
        self.score = 0

    def __repr__(self):
        return \
            '<date %r, name %r, band %r >' % (
                self.date, self.name, self.band)

    def createDisc(self, name, date, genre, band):
        logging.info("Creando disco")

        checkLongName = len(name) <= properties.maxDiscName
        checkGenre = len(genre) <= properties.maxGenreName

        if checkLongName and checkGenre:
            disc = Disc(name, date, genre, band)
            logging.info("Disco creado")
            return disc.save()
        else:
            logging.info("Error creando disco")
            return {'status': 'failure', 'msg': 'El disco no pudo ser creado', 'id': self.id}

    def getDiscs(self):
        logging.info("Obteniendo discos")
        result = self.query.all()
        return result

    def getDiscsByDate(self, startDate, endDate):
        logging.info('Obteniendo discos por fecha: %r hasta %r ' % (startDate, endDate))
        if startDate is None:
            discs = self.query.filter(Disc.date <= endDate).all()
        else:
            discs = self.query.filter(and_(Disc.date <= endDate, Disc.date >= startDate)).all()
        return discs

    def getDiscsByGenre(self, genre):
        logging.info('Obteniendo discos por genero: %r' % genre)
        discs = self.query.filter_by(disc=disc).all()
        return discs

    def getDiscsByScore(self, startScore, endScore):
        logging.info('Obteniendo discos por puntuacion: %r hasta %r ' % (startScore, endScore))
        if startScore is None:
            discs = self.query.filter(Disc.score <= endScore).all()
        else:
            discs = self.query.filter(and_(Disc.score <= endScore, Disc.score >= startScore)).all()
        return discs

    def getDiscsByBand(self, band):
        logging.info('Obteniendo discos por banda: %r' % band)
        discs = self.query.filter_by(band=band).all()
        return discs

    def getDiscsByName(self, name):
        logging.info('Obteniendo discos por nombre: %r' % name)
        bands = self.query.filter(Disc.name.like("%name%")).all()
        return bands

    def getDiscById(self, id):
        logging.info('Obteniendo disco por id: %r' % id)
        disc = self.query.filter_by(id=id).first()
        return disc

    def setDiscScore(self, score):
        self.score = score

    def setDiscCover(self, cover):
        self.cover = cover

    def setDiscGenre(self, genre):
        self.genre = genre

    def setDiscReview(self, review):
        self.review = review

    def update(self):
        try:
            db.session.commit()
            return {'status': 'success', 'msg': 'El disco fue actualizado'}
        except:
            db.session.rollback()
            return {'status': 'failure', 'msg': 'El disco no pudo ser actualizado'}

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return {'status': 'success', 'msg': 'El disco fue creado'}
        except:
            db.session.rollback()
            return {'status': 'failure', 'msg': 'El disco no pudo ser creado'}

    def delete(self):
        disc = self.getDiscById(self.id)
        db.session.delete(disc)
        try:
            db.session.commit()
            return {'status': 'success', 'msg': 'El disco fue eliminado'}
        except:
            db.session.rollback()
            return {'status': 'failure', 'msg': 'El disco no pudo ser eliminado'}

