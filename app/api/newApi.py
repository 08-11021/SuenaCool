from flask import Blueprint, json, request, session
from articleApi import *
from bandApi import *
from discApi import *
from stateApi import *
from userApi import *

new = Blueprint('new', __name__,)

'''Crear nueva noticia'''
@new.route('/new', methods=['POST'])
def createNew():
    return None

'''Obtener noticia por ID'''
@new.route('/new', methods=['GET'])
def getNew():
    return None

'''Obtener noticias (por tipo)'''
@new.route('/news', methods=['GET'])
def getNews():
    return None

'''Obtener noticias por fecha'''
@new.route('/news/date', methods=['GET'])
def getNewsByDate():
    return None

'''Obtener noticias por titulo'''
@new.route('/news/title', methods=['GET'])
def getNewsByTitle():
    return None

'''Actualizar noticia'''
@new.route('/new', methods=['PUT'])
def updateNew():
    return None

'''Borrar noticia'''
@new.route('/new', methods=['DELETE'])
def deleteNew():
    return None
