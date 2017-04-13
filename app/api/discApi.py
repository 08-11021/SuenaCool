from flask import Blueprint, json, request, session
from app.models.disc import *
from app.models.band import *
from app.utility.util import checkLenght

disc = Blueprint('disc', __name__,)

'''Crear nuevo disco'''
@disc.route('/disc', methods=['POST'])
def createDisc():
    #required args
    name = request.args.get('name')
    date = request.args.get('date')
    genre = request.args.get('genre')
    band = request.args.get('band')
    #non required args
    score = request.args.get('score')
    cover = request.args.get('cover')
    review = request.args.get('review')

    if checkLenght(name) and checkLenght(date) and checkLenght(genre) and checkLenght(band):
        checkBand = Band.getBandById(int(band))
        if checkBand != None and len(checkBand) > 0:
            res = Disc.createDisc(name, date, genre, int(band))
            if res['status'] == 'success':
                disc = Disc.getDiscById(res['id'])
                if checkLenght(score):
                    disc.setDiscScore(score)
                if checkLenght(cover):
                    disc.setDiscCover(cover)
                if checkLenght(review):
                    disc.setDiscReview(review)
                res2 = disc.update()
                if res2['status'] == 'failure':
                    res = res2
        else:
            res = {'status': 'failure', 'msg': 'La banda seleccionada no existe'}
    else:
        res = {'status': 'failure', 'msg': 'Alguno de los campos obligatorios esta vacio'}

    return json.dumps(res)

'''Obtener disco por ID'''
@disc.route('/disc/<int:disc_id>', methods=['GET'])
def getDisc(disc_id):
    disc = Disc.getDiscById(disc_id)[0]
    res = {'name': disc.name,
           'date': disc.date,
           'genre': disc.genre,
           'band': disc.band,
           'score': disc.score,
           'cover': disc.cover,
           'review': disc.review}

    return json.dumps(res)

'''Actualizar disco'''
@disc.route('/disc/<int:disc_id>', methods=['PUT'])
def update_new(disc_id):
    # required args
    name = request.args.get('name')
    date = request.args.get('date')
    genre = request.args.get('genre')
    band = request.args.get('band')
    # non required args
    score = request.args.get('score')
    cover = request.args.get('cover')
    review = request.args.get('review')

    if checkLenght(name) and checkLenght(date) and checkLenght(genre) and checkLenght(band):
        disc = Disc.getDiscById(disc_id)[0]
        disc.name = name
        disc.date = date
        disc.genre = genre
        disc.band = band
        disc.score = score
        disc.cover = cover
        disc.review = review
        res = disc.update()
    else:
        res = {'status': 'failure', 'msg': 'Todos los campos son requeridos, ninguno puede estar vacio'}
    return json.dumps(res)

'''Borrar disco'''
@disc.route('/disc/<int:disc_id>', methods=['DELETE'])
def delete_new(disc_id):
    disc = Disc.getDiscById(disc_id)[0]
    try:
        res = disc.delete()
    except:
        res = {'status': 'failure', 'msg': 'Error al eliminar disco'}
    return res

'''Obtener discos'''
@disc.route('/discs', methods=['GET'])
def getDiscs():
    discs = Disc.getDiscs()
    result = []
    for disc in discs:
        result.append(
            {'name': disc.name,
             'date': disc.date,
             'genre': disc.genre,
             'band': disc.band,
             'score': disc.score,
             'cover': disc.cover,
             'review': disc.review})

    res = {'status': 'success', 'result': result}

    return json.dumps(res)

'''Obtener discos por fecha'''
@disc.route('/discs/date', methods=['GET'])
def getDiscsByDate():
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    discs = Disc.getDiscsByDate(startDate, endDate)
    result = []
    for disc in discs:
        result.append(
            {'name': disc.name,
             'date': disc.date,
             'genre': disc.genre,
             'band': disc.band,
             'score': disc.score,
             'cover': disc.cover,
             'review': disc.review})

    res = {'status': 'success', 'result': result}
    return json.dumps(res)

'''Obtener discos por banda'''
@disc.route('/discs/band', methods=['GET'])
def getDiscsByBand():
    band = request.args.get('band')
    discs = Disc.getDiscsByBand(band)
    result = []
    for disc in discs:
        result.append(
            {'name': disc.name,
             'date': disc.date,
             'genre': disc.genre,
             'band': disc.band,
             'score': disc.score,
             'cover': disc.cover,
             'review': disc.review})

    res = {'status': 'success', 'result': result}
    return json.dumps(res)

'''Obtener discos por puntaje'''
@disc.route('/discs/score', methods=['GET'])
def getDiscsByScore():
    startScore = request.args.get('startScore')
    endScore = request.args.get('endScore')
    discs = Disc.getDiscsByScore(startScore, endScore)
    result = []
    for disc in discs:
        result.append(
            {'name': disc.name,
             'date': disc.date,
             'genre': disc.genre,
             'band': disc.band,
             'score': disc.score,
             'cover': disc.cover,
             'review': disc.review})

    res = {'status': 'success', 'result': result}
    return json.dumps(res)

'''Obtener discos por nombre'''
@disc.route('/discs/name', methods=['GET'])
def getDiscsByName():
    name = request.args.get('name')
    discs = Disc.getDiscsByName(name)
    result = []
    for disc in discs:
        result.append(
            {'name': disc.name,
             'date': disc.date,
             'genre': disc.genre,
             'band': disc.band,
             'score': disc.score,
             'cover': disc.cover,
             'review': disc.review})

    res = {'status': 'success', 'result': result}
    return json.dumps(res)

'''Obtener discos por genero'''
@disc.route('/discs/genre', methods=['GET'])
def get_discs_by_genre():
    genre = request.args.get('genre')
    discs = Disc.getDiscsByGenre(genre)
    result = []
    for disc in discs:
        result.append(
            {'name': disc.name,
             'date': disc.date,
             'genre': disc.genre,
             'band': disc.band,
             'score': disc.score,
             'cover': disc.cover,
             'review': disc.review})

    res = {'status': 'success', 'result': result}
    return json.dumps(res)
