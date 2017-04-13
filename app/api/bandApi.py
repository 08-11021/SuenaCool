from flask import Blueprint, json, request, session
from articleApi import *
from discApi import *
from newApi import *
from stateApi import *
from userApi import *

band = Blueprint('band', __name__,)

'''Crear nueva banda'''
@band.route('/band', methods=['POST'])
def createBand():
    return None

'''Obtener banda por ID'''
@band.route('/band', methods=['GET'])
def getBand():
    return None

'''Obtener score de banda'''
@band.route('/band/score', methods=['GET'])
def getBandScore():
    return None

'''Obtener bandas'''
@band.route('/bands', methods=['GET'])
def getBands():
    return None

'''Obtener bandas por score'''
@band.route('/bands/score', methods=['GET'])
def getBandsByScore():
    return None

'''Obtener bandas por estado'''
@band.route('/bands/state', methods=['GET'])
def getBandsByState():
    return None

'''Obtener bandas por nombre'''
@band.route('/bands/name', methods=['GET'])
def getBandsByName():
    return None


'''Actualizar banda'''
@band.route('/band', methods=['PUT'])
def updateBand():
    return None

'''Borrar banda'''
@band.route('/band', methods=['DELETE'])
def deleteBand():
    return None
