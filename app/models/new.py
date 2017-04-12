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
            new.save()

        logging.info('Noticia creada')

    def getNews(self):
        logging.info("Obteniendo noticia")
        result = self.query.all()
        return result

    def getNewById(self, id):
        logging.info('Obteniendo noticia por id: %r' % id)
        new = self.query.filter_by(id=id).first()
        return new

    def getNewsByDate(self, startDate, endDate):
        logging.info('Obteniendo noticia por fecha: %r hasta %r ' % (startDate, endDate))
        if startDate is None:
            news = self.query.filter(New.date <= endDate).all()
        else:
            news = self.query.filter(and_(New.date <= endDate, New.date >= startDate)).all()
        return news

    def getNewsByTitle(self, title):
        logging.info('Obteniendo noticia por titulo: %r' % title)
        news = self.query.filter(New.name.like("%name%")).all()
        return news

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
        new = self.getBandById(self.id)
        db.session.delete(new)
        try:
            db.session.commit()
        except:
            db.session.rollback()
