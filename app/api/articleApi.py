from flask import Blueprint, json, request, session
from bandApi import *
from discApi import *
from newApi import *
from stateApi import *
from userApi import *

article = Blueprint('article', __name__,)

'''Crear nuevo articulo'''
@article.route('/article', methods=['POST'])
def createArticle():
    return None

'''Obtener articulo por ID'''
@article.route('/article', methods=['GET'])
def getArticle():
    return None

'''Obtener articulo (por tipo)'''
@article.route('/articles', methods=['GET'])
def getArticles():
    return None

'''Obtener articulo por fecha'''
@article.route('/articles/date', methods=['GET'])
def getArticlesByDate():
    return None

'''Obtener articulo por titulo'''
@article.route('/articles/title', methods=['GET'])
def getArticlesByTitle():
    return None

'''Actualizar articulo'''
@article.route('/article', methods=['PUT'])
def updateArticle():
    return None

'''Borrar articulo'''
@article.route('/article', methods=['DELETE'])
def deleteArticle():
    return None
