from flask import Blueprint, json, request, session
from articleApi import *
from bandApi import *
from discApi import *
from stateApi import *
from userApi import *

new = Blueprint('new', __name__,)

'''Crear nueva noticia'''
@new.route('/new', methods=['POST'])
def create_new():
    return None

'''Obtener noticia por ID'''
@new.route('/new', methods=['GET'])
def get_new():
    return None

'''Obtener noticias (por tipo)'''
@new.route('/news', methods=['GET'])
def get_news():
    return None

'''Obtener noticias por fecha'''
@new.route('/news/date', methods=['GET'])
def get_news_by_date():
    return None

'''Obtener noticias por titulo'''
@new.route('/news/title', methods=['GET'])
def get_news_by_title():
    return None

'''Actualizar noticia'''
@new.route('/new', methods=['PUT'])
def update_new():
    return None

'''Borrar noticia'''
@new.route('/new', methods=['DELETE'])
def delete_new():
    return None
