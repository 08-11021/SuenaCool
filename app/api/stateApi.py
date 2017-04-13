from flask import Blueprint, json, request, session
from articleApi import *
from bandApi import *
from discApi import *
from newApi import *
from userApi import *

state = Blueprint('state', __name__,)

'''Obtener estado'''
@state.route('/state', methods=['GET'])
def get_state():
    return None

'''Obtener estados'''
@state.route('/states', methods=['GET'])
def get_states():
    return None
