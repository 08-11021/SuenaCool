from flask import Blueprint, json, request, session
from articleApi import *
from discApi import *
from newApi import *
from stateApi import *
from userApi import *

band = Blueprint('band', __name__,)

'''Crear nueva banda'''
@band.route('/band', methods=['POST'])
def create_band():
    return None

'''Obtener banda por ID'''
@band.route('/band', methods=['GET'])
def get_band():
    return None

'''Obtener score de banda'''
@band.route('/band/score', methods=['GET'])
def get_band_score():
    return None

'''Obtener bandas'''
@band.route('/bands', methods=['GET'])
def get_bands():
    return None

'''Obtener bandas por score'''
@band.route('/bands/score', methods=['GET'])
def get_bands_by_score():
    return None

'''Obtener bandas por estado'''
@band.route('/bands/state', methods=['GET'])
def get_bands_by_state():
    return None

'''Obtener bandas por nombre'''
@band.route('/bands/name', methods=['GET'])
def get_bands_by_name():
    return None


'''Actualizar banda'''
@band.route('/band', methods=['PUT'])
def update_band():
    return None

'''Borrar banda'''
@band.route('/band', methods=['DELETE'])
def delete_band():
    return None
