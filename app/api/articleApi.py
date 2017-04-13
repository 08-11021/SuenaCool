from flask import Blueprint, json, request, session
from app.models.article import *
from app.utility.util import checkLenght

article = Blueprint('article', __name__,)

'''Crear nueva noticia'''
@article.route('/article', methods=['POST'])
def createArticle():
    type = request.args.get('type')
    date = request.args.get('date')
    title = request.args.get('title')
    pic = request.args.get('pic')
    content = request.args.get('content')

    if checkLenght(type) and checkLenght(date) and checkLenght(title) and checkLenght(pic) and checkLenght(content):
        res = Article.createArticle(type, date, title, pic, content)
    else:
        res = {'status': 'failure', 'msg': 'Todos los campos son requeridos, ninguno puede estar vacio'}

    return json.dumps(res)

'''Obtener noticia por ID'''
@article.route('/article/<int:article_id>', methods=['GET'])
def getArticle(article_id):
    article = Article.getArticleById(article_id)[0]
    res = {'type': article.type,
           'date': article.date,
           'title': article.title,
           'pic': article.pic,
           'content': article.content}

    return json.dumps(res)

'''Obtener articulos (por tipo)'''
@article.route('/articles/<article_type>', methods=['GET'])
def getArticles(article_type):
    articles = Article.getArticles(article_type)
    result = []
    for article in articles:
        result.append(
            {'type': article.type,
             'date': article.date,
             'title': article.title,
             'pic': article.pic,
             'content': article.content})

    res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''Obtener articulos por fecha'''
@article.route('/articles/<article_type>/date', methods=['GET'])
def getArticlesByDate(article_type):
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    articles = Article.getArticlesByDate(article_type, startDate, endDate)
    result = []
    for article in articles:
        result.append(
            {'type': article.type,
             'date': article.date,
             'title': article.title,
             'pic': article.pic,
             'content': article.content})

    res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''Obtener articulos por titulo'''
@article.route('/articles/<article_type>/title', methods=['GET'])
def getArticlesByTitle(article_type):
    title = request.args.get('title')
    articles = Article.getArticlesByDate(article_type, title)
    result = []
    for article in articles:
        result.append(
            {'type': article.type,
             'date': article.date,
             'title': article.title,
             'pic': article.pic,
             'content': article.content})

    res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''Actualizar articulo'''
@article.route('/article/<int:article_id>', methods=['PUT'])
def updateArticle(article_id):
    type = request.args.get('type')
    date = request.args.get('date')
    title = request.args.get('title')
    pic = request.args.get('pic')
    content = request.args.get('content')
    if checkLenght(type) and checkLenght(date) and checkLenght(title) and checkLenght(pic) and checkLenght(content):
        article = Article.getArticleById(article_id)
        article.type = type
        article.date = date
        article.title = title
        article.pic = pic
        article.content = content
        res = article.update()
    else:
        res = {'status': 'failure', 'msg': 'Todos los campos son requeridos, ninguno puede estar vacio'}
    return json.dumps(res)

'''Borrar articulo'''
@article.route('/article/<int:article_id>', methods=['DELETE'])
def deleteArticle(article_id):
    article = Article.getArticleById(article_id)
    try:
        result = article.delete()
    except:
        result = {'status': 'failure', 'msg': 'Error al eliminar articulo'}
    return result
