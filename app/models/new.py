import datetime
import logging

from sqlalchemy import and_

from app import properties
from app.models.db import db


class New(db.Model):
    __tablename__ = 'new'
    id = db.Column(db.Integer, primary_key=True, index=True)
    type = db.Column(db.String(30))
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    title = db.Column(db.String(100))
    pic = db.Column(db.String(200))
    content = db.Column(db.String(5000))

    def __init__(self, type, date, title, pic, content):
        self.type = type
        self.date = date
        self.title = title
        self.pic = pic
        self.content = content

    def __repr__(self):
        return \
            '<title %r, date %r>' % (
                self.title, self.date)

    def createNew(self, type, date, title, pic, content):
        logging.info('Creando Noticia: %r' % title)

        checkNewType = type in properties.newTypes

        if checkNewType:

            new = New(type, date, title, pic, content)
            res = new.save()
            logging.info('Noticia creada')
            return res
        else:
            logging.info('Error al crear noticia')
            return properties.responseNewInvalidType



    def getNews(self, type):
        logging.info("Obteniendo noticia")
        result = self.query.filter(New.type.like(type)).all()
        return result

    def getNewById(self, id):
        logging.info('Obteniendo noticia por id: %r' % id)
        new = self.query.filter_by(id=id).first()
        return new

    def getNewsByDate(self, type, startDate, endDate):
        logging.info('Obteniendo noticia por fecha: %r hasta %r ' % (startDate, endDate))
        if startDate is None:
            news = self.query.filter(and_(New.date <= endDate, New.type == type)).all()
        else:
            news = self.query.filter(and_(New.date <= endDate, New.date >= startDate, New.type == type)).all()
        return news

    def getNewsByTitle(self, type, title):
        logging.info('Obteniendo noticia por titulo: %r' % title)
        news = self.query.filter(and_(New.name.like("%name%"), New.type == type)).all()
        return news

    def update(self):
        try:
            db.session.commit()
            return properties.responseNewUpdated
        except:
            db.session.rollback()
            return properties.responseNewNotUpdated

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return properties.responseNewCreated
        except:
            db.session.rollback()
            return properties.responseNewNotCreated

    def delete(self):
        try:
            new = self.getBandById(self.id)
            db.session.delete(new)

            db.session.commit()
            return properties.responseNewDeleted
        except:
            db.session.rollback()
            return properties.responseNewNotDeleted
