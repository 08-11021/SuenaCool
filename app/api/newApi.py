from flask import Blueprint, json, request, session
from app.models.new import *
from app.utility.util import checkLenght

new = Blueprint('new', __name__,)

'''Crear nueva noticia'''
@new.route('/new', methods=['POST'])
def createNew():
    type = request.args.get('type')
    date = request.args.get('date')
    title = request.args.get('title')
    pic = request.args.get('pic')
    content = request.args.get('content')

    if checkLenght(type) and checkLenght(date) and checkLenght(title) and checkLenght(pic) and checkLenght(content):
        res = New.createNew(type, date, title, pic, content)
    else:
        res = {'status': 'failure', 'msg': 'Todos los campos son requeridos, ninguno puede estar vacio'}

    return json.dumps(res)

'''Obtener noticia por ID'''
@new.route('/new/<int:new_id>', methods=['GET'])
def getNew(new_id):
    new = New.getNewById(new_id)[0]
    res = {'type': new.type,
           'date': new.date,
           'title': new.title,
           'pic': new.pic,
           'content': new.content}

    return json.dumps(res)


'''Actualizar noticia'''
@new.route('/new/<int:new_id>', methods=['PUT'])
def updateNew(new_id):
    type = request.args.get('type')
    date = request.args.get('date')
    title = request.args.get('title')
    pic = request.args.get('pic')
    content = request.args.get('content')
    if checkLenght(type) and checkLenght(date) and checkLenght(title) and checkLenght(pic) and checkLenght(content):
        new = New.getNewById(new_id)
        new.type = type
        new.date = date
        new.title = title
        new.pic = pic
        new.content = content
        res = new.update()
    else:
        res = {'status': 'failure', 'msg': 'Todos los campos son requeridos, ninguno puede estar vacio'}
    return json.dumps(res)

'''Borrar noticia'''
@new.route('/new/<int:new_id>', methods=['DELETE'])
def deleteNew(new_id):
    new = New.getNewById(new_id)
    try:
        result = new.delete()
    except:
        result = {'status': 'failure', 'msg': 'Error al eliminar noticia'}
    return result

'''Obtener noticias (por tipo)'''
@new.route('/news/<new_type>', methods=['GET'])
def getNews(new_type):
    news = New.getNews(new_type)
    result = []
    for new in news:
        result.append(
            {'type': new.type,
             'date': new.date,
             'title': new.title,
             'pic': new.pic,
             'content': new.content})

    res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''Obtener noticias por fecha'''
@new.route('/news/<new_type>/date', methods=['GET'])
def getNewsByDate(new_type):
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    news = New.getNewsByDate(new_type, startDate, endDate)
    result = []
    for new in news:
        result.append(
            {'type': new.type,
             'date': new.date,
             'title': new.title,
             'pic': new.pic,
             'content': new.content})

    res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''Obtener noticias por titulo'''
@new.route('/news/<new_type>/title', methods=['GET'])
def getNewsByTitle(new_type):
    title = request.args.get('title')
    news = New.getNewsByDate(new_type, title)
    result = []
    for new in news:
        result.append(
            {'type': new.type,
             'date': new.date,
             'title': new.title,
             'pic': new.pic,
             'content': new.content})

    res = {'status': 'success', 'result': result}

    return json.dumps(res)

