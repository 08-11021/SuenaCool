from flask import Blueprint, json, request, session

from app.models.suscription import Suscription

suscription = Blueprint('suscription', __name__,)


@suscription.route('/suscriptions/create', methods=['POST'])
def create_suscription():
    category = request.args.get('category') or None
    user = session['email']
    if request.args.get('category') is None or len(request.args.get('category')) == 0:
        res = {'error': 'You must provide a valid category.'}
    else:
        SuscriptionInstance = Suscription()
        result = SuscriptionInstance.createSuscription(
            category, user)
        res = result

    return json.dumps(res)


@suscription.route('/suscriptions', methods=['GET'])
def get_suscriptions():
    SuscriptionInstance = Suscription()
    suscriptions = SuscriptionInstance.getSuscriptions()
    rescat = []
    for suscription in suscriptions:
        rescat.append({'id': suscription.suscriptionId,
                       'category': suscription.category,
                       'user': suscription.user})

    return json.dumps(rescat)

@suscription.route('/userSuscriptions', methods=['GET'])
def get_user_suscriptions():
    user = session['email']
    SuscriptionInstance = Suscription()
    suscriptions = SuscriptionInstance.getSuscriptionsByUser(user)
    rescat = []
    for suscription in suscriptions:
        rescat.append({'id': suscription.suscriptionId,
                       'category': suscription.category,
                       'user': suscription.user})
    res = {'result':rescat}
    return json.dumps(res)


@suscription.route('/suscriptions/delete', methods=['POST'])
def delete_suscription():
    id = int(request.args.get('id'))
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid suscription id.'}
    else:
        SuscriptionInstance = Suscription()
        result = SuscriptionInstance.deleteSuscription(id)
        res = result

    return json.dumps(res)

@suscription.route('/suscriptions/update', methods=['POST'])
def update_suscription():
    id = int(request.args.get('id'))
    category = request.args.get('category') or None
    user = request.args.get('user') or None
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid category id.'}
    else:
        SuscriptionInstance = Suscription()
        result = SuscriptionInstance.updateSuscription(
            id, category, user)
        res = result

    return json.dumps(res)
