from flask import Blueprint, json, request, session
from app.models.band import *
from app.models.disc import *
from app.utility.util import checkLenght

band = Blueprint('band', __name__,)

'''Crear nueva banda'''
@band.route('/band', methods=['POST'])
def createBand():
    # required args
    name = request.args.get('name')
    state = request.args.get('state')

    # non required args
    pic = request.args.get('score')
    review = request.args.get('cover')

    if checkLenght(name) and checkLenght(state):
        res = Band.createBand(name, int(state))
        if res['status'] == 'success':
            band = Band.getBandById(res['id'])
            if checkLenght(pic):
                band.setBandPic(pic)
            if checkLenght(review):
                band.setBandReview(review)

            res2 = band.update()
            if res2['status'] == 'failure':
                res = res2
    else:
        res = {'status': 'failure', 'msg': 'Alguno de los campos obligatorios esta vacio'}

    return json.dumps(res)

'''Obtener banda por ID'''
@band.route('/band/<int:band_id>', methods=['GET'])
def getBand(band_id):
    band = Band.getBandById(band_id)[0]
    score = 0

    # checking band score
    bandScore = getBandScore(band.id)
    if bandScore['status'] == 'success':
        score = bandScore['score']

    res = {'name': band.name,
           'state': band.state,
           'pic': band.pic,
           'review': band.review,
           'score': score}

    return json.dumps(res)

'''Obtener score de banda'''
@band.route('/band/<int:band_id>/score', methods=['GET'])
def getBandScore(band_id):
    discs = Disc.getDiscsByBand(band_id)
    discCounter = 0
    totalScore = 0
    for disc in discs:
        totalScore = totalScore + disc['score']
        discCounter = discCounter + 1

    res = {'status': 'success', 'msg': 'Operacion exitosa', 'score': (totalScore / discCounter)}

    return res

'''Actualizar banda'''
@band.route('/band/<int:band_id>', methods=['PUT'])
def updateBand(band_id):
    # required args
    name = request.args.get('name')
    state = request.args.get('state')

    # non required args
    pic = request.args.get('score')
    review = request.args.get('cover')

    if checkLenght(name) and checkLenght(state):
        band = Band.getBandById(band_id)[0]
        band.name = name
        band.state = state
        band.pic = pic
        band.review = review

        res = band.update()
    else:
        res = {'status': 'failure', 'msg': 'Todos los campos son requeridos, ninguno puede estar vacio'}
    return json.dumps(res)

'''Borrar banda'''
@band.route('/band/<int:band_id>', methods=['DELETE'])
def deleteBand(band_id):
    band = Band.getBandById(band_id)[0]
    try:
        res = disc.delete()
    except:
        res = {'status': 'failure', 'msg': 'Error al eliminar banda'}
    return res

'''Obtener bandas'''
@band.route('/bands', methods=['GET'])
def getBands():
    bands = Band.getBands()
    result = fillBands(bands)
    res = {'status': 'success', 'result': result}
    return json.dumps(res)

'''Obtener bandas por score
@band.route('/bands/score', methods=['GET'])
def getBandsByScore():
    return None
'''

'''Obtener bandas por estado'''
@band.route('/bands/state', methods=['GET'])
def getBandsByState():
    state = request.args.get('state')
    bands = Band.getBandsByStateId(int(state))
    result = fillBands(bands)
    res = {'status': 'success', 'result': result}
    return json.dumps(res)

'''Obtener bandas por nombre'''
@band.route('/bands/name', methods=['GET'])
def getBandsByName():
    name = request.args.get('name')
    bands = Band.getBandsByName(name)
    result = fillBands(bands)
    res = {'status': 'success', 'result': result}
    return json.dumps(res)

def fillBands(bands):
    result = []
    for band in bands:
        score = 0

        # checking band score
        bandScore = getBandScore(band.id)
        if bandScore['status'] == 'success':
            score = bandScore['score']

        result.append(
            {'name': band.name,
             'state': band.state,
             'pic': band.pic,
             'review': band.review,
             'score': score})

    return result


