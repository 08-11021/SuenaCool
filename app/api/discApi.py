from flask import Blueprint, json, request, session
from articleApi import *
from bandApi import *
from newApi import *
from stateApi import *
from userApi import *

disc = Blueprint('disc', __name__,)

'''Crear nuevo disco'''
@disc.route('/disc', methods=['POST'])
def createDisc():
    return None

'''Obtener disco por ID'''
@disc.route('/disc', methods=['GET'])
def getDisc():
    return None

'''Obtener score de disco'''
@disc.route('/disc/score', methods=['GET'])
def getDiscScore():
    return None

'''Obtener discos'''
@disc.route('/discs', methods=['GET'])
def getDiscs():
    return None

'''Obtener discos por fecha'''
@disc.route('/discs/date', methods=['GET'])
def getDiscsByDate():
    return None

'''Obtener discos por banda'''
@disc.route('/news/band', methods=['GET'])
def getDiscsByBand():
    return None

'''Obtener discos por estado'''
@disc.route('/news/state', methods=['GET'])
def getDiscsByState():
    return None

'''Obtener discos por nombre'''
@disc.route('/news/name', methods=['GET'])
def getDiscsByName():
    return None

'''Obtener discos por genero'''
@disc.route('/news/genre', methods=['GET'])
def get_discs_by_genre():
    return None

'''Actualizar disco'''
@disc.route('/disc', methods=['PUT'])
def update_new():
    return None

'''Borrar disco'''
@disc.route('/disc', methods=['DELETE'])
def delete_new():
    return None
