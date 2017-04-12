from flask import Blueprint, json, request, session

from app.models.service import Service

service = Blueprint('service', __name__,)


@service.route('/services/create', methods=['POST'])
def create_service():
    name = request.args.get('name')
    category = request.args.get('category') or None
    user = session['email']
    if request.args.get('name') is None or len(request.args.get('name')) == 0:
        res = {'error': 'You must provide a valid service name.'}
    if request.args.get('category') is None or len(request.args.get('category')) == 0:
        res = {'error': 'You must provide a valid category.'}
    else:
        ServiceInstance = Service()
        result = ServiceInstance.createService(
            name, category, user)
        res = result

    return json.dumps(res)


@service.route('/services', methods=['GET'])
def get_services():
    ServiceInstance = Service()
    services = ServiceInstance.getServices()
    rescat = []
    for service in services:
        rescat.append({'id': service.serviceId,
                       'name': service.name,
                       'category': service.category,
                       'user': service.user})

    return json.dumps(rescat)


@service.route('/userServices', methods=['GET'])
def get_user_services():
    user = session['email']
    ServiceInstance = Service()
    services = ServiceInstance.getServicesByUser(user)
    rescat = []
    for service in services:
        rescat.append({'id': service.serviceId,
                       'name': service.name,
                       'category': service.category,
                       'user': service.user})
    res = {'result': rescat}
    return json.dumps(res)


@service.route('/service', methods=['GET'])
def get_service():
    name = request.args.get('name')
    if request.args.get('name') is None or len(request.args.get('name')) == 0:
        res = {'error': 'You must provide a valid service name.'}
    else:
        ServiceInstance = Service()
        service = ServiceInstance.getServiceByName(name)
        res = {'id': service.serviceId,
               'name': service.name,
               'category': service.category,
               'user': service.user}

    return json.dumps(res)


@service.route('/services/delete', methods=['POST'])
def delete_service():
    id = int(request.args.get('id'))
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid service id.'}
    else:
        ServiceInstance = Service()
        result = ServiceInstance.deleteService(id)
        res = result

    return json.dumps(res)


@service.route('/services/update', methods=['POST'])
def update_service():
    id = int(request.args.get('id'))
    name = request.args.get('name') or None
    category = request.args.get('category') or None
    user = request.args.get('user') or None
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid category id.'}
    else:
        ServiceInstance = Service()
        result = ServiceInstance.updateService(
            id, name, category, user)
        res = result

    return json.dumps(res)
