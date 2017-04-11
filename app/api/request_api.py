from flask import Blueprint, json, request, session

from app.models.service import Service
from app.models.category import Category
from app.models.suscription import Suscription

requesta = Blueprint('request', __name__,)

@requesta.route('/requests', methods=['GET'])
def get_requests():
    user = session['email']
    newSuscription = Suscription()
    suscriptions = newSuscription.getSuscriptionsByUser(user)
    categories = {}
    for suscription in suscriptions:
        categories[suscription.category] = suscription.category
        children = get_children(suscription.category)
        for child in children:
            categories[child] = child
    res = []
    categoriesx= categories.keys()
    newService = Service()
    for category in categoriesx:
        services= newService.getServicesByCategory(category)
        for service in services:
            res.append({'id': service.serviceId,
                       'name': service.name,
                       'category': service.category,
                       'user': service.user})
    rescat = {'result': res}
    return json.dumps({'result': res})


def get_children(parentCategory):
    CategoryInstance = Category()
    cat = CategoryInstance.getCategoryByName(parentCategory)
    categories = CategoryInstance.getSubCategories(cat.categoryId)
    res = []
    for category in categories:
        res.append(category.name)
        children = get_children(category.name)
        for child in children:
            res.append(child)

    return res

