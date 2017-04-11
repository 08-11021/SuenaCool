from flask import Blueprint, json, request

from app.models.category import Category

category = Blueprint('category', __name__,)


@category.route('/categories/create', methods=['POST'])
def create_category():
    name = request.args.get('name')
    isSubcategory = bool(request.args.get('isSubCategory')) or None
    parentCategory = request.args.get('parentCategory') or None
    if request.args.get('name') is None or len(request.args.get('name')) == 0:
        res = {'error': 'You must provide a valid category name.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.createCategory(
            name, isSubcategory, parentCategory)
        res = result

    return json.dumps(res)


@category.route('/categories', methods=['GET'])
def get_categories():
    CategoryInstance = Category()
    categories = CategoryInstance.getCategories()
    rescat = []
    for category in categories:
        rescat.append({'name': category.name,
                       'id': category.categoryId,
                       'parent': category.parentCategory,
                       'isSubCategory': category.isSubCategory})
    res = {'result': rescat}

    return json.dumps(res)


@category.route('/categories/children', methods=['GET'])
def get_children():
    parentCategory = int(request.args.get('parentCategory'))
    CategoryInstance = Category()
    categories = CategoryInstance.getSubCategories(parentCategory)
    rescat = []
    if categories != []:
        for category in categories:
            rescat.append({'name': category.name,
                           'id': category.categoryId,
                           'parent': category.parentCategory,
                           'isSubCategory': category.isSubCategory})
    res = {'result': rescat}

    return json.dumps(res)


@category.route('/category', methods=['GET'])
def get_category():
    name = request.args.get('name')
    if request.args.get('name') is None or len(request.args.get('name')) == 0:
        res = {'error': 'You must provide a valid category name.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.getCategoryByName(name)
        res = result

    return json.dumps(res)


@category.route('/categories/delete', methods=['POST'])
def delete_category():
    id = request.args.get('id')
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid category id.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.deleteCategory(id)
        res = result

    return json.dumps(res)


@category.route('/categories/update', methods=['POST'])
def update_category():
    id = int(request.args.get('id'))
    name = request.args.get('name') or None
    isSubcategory = bool(request.args.get('isSubcategory')) or None
    parentCategory = int(request.args.get('parentCategory')) or None
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'You must provide a valid category id.'}
    else:
        CategoryInstance = Category()
        result = CategoryInstance.updateCategory(
            id, name, isSubcategory, parentCategory)
        res = result

    return json.dumps(res)


@category.route('/categories/breadcrumbs', methods=['GET'])
def get_breadcrumbs():
    category = int(request.args.get('id'))
    CategoryInstance = Category()
    rescat = []
    while category != 0 and category is not None:
        parent = CategoryInstance.getCategoryById(category)
        rescat.append({'name': parent.name,
                       'id': parent.categoryId,
                       'parent': parent.parentCategory,
                       'isSubCategory': parent.isSubCategory})
        category = parent.parentCategory
    parent = CategoryInstance.getCategoryById(category)
    rescat.append(parent)
    rescat.reverse()
    res = {'result': rescat}

    return json.dumps(res)

@category.route('/categories/tree', methods=['GET'])
def get_tree():
    CategoryInstance = Category()
    categories = CategoryInstance.getCategories()
    rescat = []
    for category in categories:
        rescat.append({'categoryName': category.name,
                       'categoryId': category.categoryId,
                       'children': get_subtree(category.categoryId)})
    res = {'result': rescat}

    return json.dumps(res)

def get_subtree(id):
    CategoryInstance = Category()
    categories = CategoryInstance.getSubCategories(id)
    rescat = []
    for category in categories:
        rescat.append({'categoryName': category.name,
                       'categoryId': category.categoryId,
                       'children': get_subtree(category.categoryId)})
    return rescat
