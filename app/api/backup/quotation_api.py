from flask import Blueprint, json, request

from app.models.quotation import Quotation

quotation = Blueprint('quotation', __name__,)


@quotation.route('/quotation/create', methods=['POST'])
def create_quotation():
    service = request.args.get('service')
    client = request.args.get('client')
    operator = int(request.args.get('operator'))
    price = int(request.args.get('price'))
    if request.args.get('service') is None \
            or len(request.args.get('service')) == 0:
        res = {'error': 'You must provide a valid service name.'}
    if request.args.get('client') is None \
            or len(request.args.get('client')) == 0:
        res = {'error': 'You must provide a valid client id.'}
    if request.args.get('operator') is None \
            or len(request.args.get('operator')) == 0:
        res = {'error': 'You must provide a valid operator.'}
    if request.args.get('price') is None \
            or len(request.args.get('price')) == 0:
        res = {'error': 'You must provide a price operator.'}
    else:
        QuotationInstance = Quotation()
        result = QuotationInstance.createQuotation(
            service, client, operator, price)
        res = result

    return json.dumps(res)


@quotation.route('/quotation/delete', methods=['POST'])
def delete_quotation():
    id = int(request.args.get('id'))
    if request.args.get('id') is None \
            or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid quotation id.'}
    else:
        QuotationInstance = Quotation()
        result = QuotationInstance.deleteQuotation(id)
        res = result

    return json.dumps(res)


@quotation.route('/quotation/update', methods=['POST'])
def update_quotation():
    id = int(request.args.get('id'))
    service = request.args.get('service') or None
    client = request.args.get('client') or None
    operator = request.args.get('operator') or None
    price = request.args.get('price') or None
    if price is not None:
        price = int(price)
    if request.args.get('id') is None \
            or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid quotation id.'}
    else:
        QuotationInstance = Quotation()
        result = QuotationInstance.updateQuotation(
            id, service, client, operator, price)
        res = result

    return json.dumps(res)


@quotation.route('/quotations', methods=['GET'])
def get_quotations():
    QuotationInstance = Quotation()
    quotations = QuotationInstance.getQuotations()
    rescat = []
    for quotation in quotations:
        rescat.append({'id': quotation.quotationId,
                       'service': quotation.service,
                       'client': quotation.client,
                       'operator': quotation.operator,
                       'price': quotation.price})

    return json.dumps(rescat)


@quotation.route('/quotation', methods=['GET'])
def get_quotation():
    id = int(request.args.get('id'))
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid quotation id.'}
    else:
        QuotationInstance = Quotation()
        quotation = QuotationInstance.getQuotationById(id)
        res = {'id': quotation.quotationId,
               'service': quotation.service,
               'client': quotation.client,
               'operator': quotation.operator,
               'price': quotation.price}

    return json.dumps(res)


@quotation.route('/quotation/check', methods=['POST'])
def check_quotation():
    service = request.args.get('service')
    client = request.args.get('client')
    operator = request.args.get('operator')
    QuotationInstance = Quotation()
    quotation = QuotationInstance.checkQuotation(
        service, client, operator)
    res = {'id': quotation.quotationId,
           'service': quotation.service,
           'client': quotation.client,
           'operator': quotation.operator,
           'price': quotation.price}

    return json.dumps(res)
