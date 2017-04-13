from flask import Blueprint, json, request, session
from bandApi import *
from discApi import *
from newApi import *
from stateApi import *
from userApi import *

article = Blueprint('article', __name__,)

'''Crear nuevo articulo'''
@article.route('/article', methods=['POST'])
def create_article():
    return None

'''Obtener articulo por ID'''
@article.route('/article', methods=['GET'])
def get_article():
    return None

'''Obtener articulo (por tipo)'''
@article.route('/articles', methods=['GET'])
def get_articles():
    return None

'''Obtener articulo por fecha'''
@article.route('/articles/date', methods=['GET'])
def get_articles_by_date():
    return None

'''Obtener articulo por titulo'''
@article.route('/articles/title', methods=['GET'])
def get_articles_by_title():
    return None

'''Actualizar articulo'''
@article.route('/article', methods=['PUT'])
def update_article():
    return None

'''Borrar articulo'''
@article.route('/article', methods=['DELETE'])
def delete_article():
    return None
