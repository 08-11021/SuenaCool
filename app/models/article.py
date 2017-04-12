import logging
import properties
import datetime
from app.models.db import db
from sqlalchemy import and_

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
            article.save()

        logging.info('Articulo creado')

    def getArticles(self):
        logging.info("Obteniendo articulos")
        result = self.query.all()
        return result

    def getArticleById(self, id):
        logging.info('Obteniendo articulo por id: %r' % id)
        article = self.query.filter_by(id=id).first()
        return article

    def getArticlesByDate(self, startDate, endDate):
        logging.info('Obteniendo articulos por fecha: %r hasta %r ' % (startDate, endDate))
        if startDate is None:
            articles = self.query.filter(Article.date <= endDate).all()
        else:
            articles = self.query.filter(and_(Article.date <= endDate, Article.date >= startDate)).all()
        return articles

    def getArticlesByTitle(self, title):
        logging.info('Obteniendo articulos por titulo: %r' % title)
        articles = self.query.filter(Article.name.like("%name%")).all()
        return articles

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
        article = self.getBandById(self.id)
        db.session.delete(article)
        try:
            db.session.commit()
        except:
            db.session.rollback()
