import datetime
import logging

from sqlalchemy import and_

from app import properties
from app.models.db import db


class Article(db.Model):
    __tablename__ = 'article'
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

    def createArticle(self, type, date, title, pic, content):
        logging.info('Creando Articulo: %r' % title)

        checkArticleType = type in properties.articleTypes

        if checkArticleType:
            article = Article(type, date, title, pic, content)
            logging.info('Articulo creado')
            return article.save()
        else:
            logging.info('Error al crear el articulo')
            return {'status': 'failure', 'msg': 'El articulo no pudo ser creado'}



    def getArticles(self, type):
        logging.info("Obteniendo articulos")
        result = self.query.filter(Article.type.like(type)).all()
        return result

    def getArticleById(self, id):
        logging.info('Obteniendo articulo por id: %r' % id)
        article = self.query.filter_by(id=id).first()
        return article

    def getArticlesByDate(self, type, startDate, endDate):
        logging.info('Obteniendo articulos por fecha: %r hasta %r ' % (startDate, endDate))
        if startDate is None:
            news = self.query.filter(and_(Article.date <= endDate, Article.type == type)).all()
        else:
            news = self.query.filter(and_(Article.date <= endDate, Article.date >= startDate, Article.type == type)).all()
        return articles

    def getArticlesByTitle(self, type, title):
        logging.info('Obteniendo articulos por titulo: %r' % title)
        articles = self.query.filter(and_(Article.name.like("%name%"), Article.type == type)).all()
        return articles

    def update(self):
        try:
            db.session.commit()
            return {'status': 'success', 'msg': 'El articulo ha sido actualizado'}
        except:
            db.session.rollback()
            return {'status': 'failure', 'msg': 'El articulo no ha podido ser actualizado'}

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return {'status': 'success', 'msg': 'Articulo creado exitosamente'}
        except:
            db.session.rollback()
            return {'status': 'failure', 'msg': 'El articulo no pudo ser creado'}

    def delete(self):
        article = self.getBandById(self.id)
        db.session.delete(article)
        try:
            db.session.commit()
            return {'status': 'success', 'msg': 'El articulo ha sido eliminado'}
        except:
            db.session.rollback()
            return {'status': 'failure', 'msg': 'El articulo no ha podido ser eliminado'}
