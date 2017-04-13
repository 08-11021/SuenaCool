from flask import Blueprint, json
from app.models.state import *

state = Blueprint('state', __name__,)

'''Obtener estado'''
@state.route('/state/<int:id_state>', methods=['GET'])
def getState(id_state):
    id = id_state
    state = State.getStateById(id)
    res = {'id': state.id,
           'name': state.name,
           }
    return json.dumps(res)

'''Obtener estados'''
@state.route('/states', methods=['GET'])
def getStates():
    states = State.getStates()
    result = []
    for state in states:
        result.append(
            {'id': state.id,
             'name': state.name,
             })
    res = {'status': 'success', 'result': result}

    return json.dumps(res)
