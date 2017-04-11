# -*- coding: utf-8 -*-.

from app.models.db import db


class Category(db.Model):
    '''Clase que define el modelo Categoria'''

    __tablename__ = 'category'
    categoryId = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(100), unique=True)
    isSubCategory = db.Column(db.Boolean, default=False)
    parentCategory = db.Column(db.Integer)

    def __init__(self, name=None, isSubCategory=None, parentCategory=None):
        '''Constructor del modelo usuario'''
        self.name = name
        self.isSubCategory = isSubCategory
        self.parentCategory = parentCategory

    def __repr__(self):
        '''Representacion en string del modelo Usuario'''
        return \
            '<name %r, isSubCategory %r, parentCategory %r >' % (
                self.name, self.isSubCategory, self.parentCategory)

    def getCategoryById(self, id):
        '''Permite buscar una categoria por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            category = self.query.filter_by(categoryId=id).all()
            if category == []:
                return []
            return category[0]

    def getAllCategories(self):
        '''Permite obtener todas las categorias y subcategorias'''

        result = self.query.all()

        if result != []:
            return result
        else:
            return {'status': 'failure', 'reason': 'There are not categories or subcateories'}

    def getCategories(self):
        '''Permite obtener todas las categorias PADRES'''

        category = self.query.filter_by(isSubCategory=False).all()

        return category

    def getSubCategories(self, id):
        ''' Permite obtener las subcategorias dado un categoryId PADRE'''

        findCategory = self.getCategoryById(id)

        if findCategory != []:

            category = self.query.filter_by(parentCategory=id).all()

            return category

        return {'status': 'failure', 'reason': 'Category parent does not exist'}

    def getCategoryByName(self, name):
        '''Permite buscar una categoria por nombre'''

        category = self.query.filter_by(name=name).all()

        if category:
            cat = category[0]
        else:
            cat = None

        return cat

    def createCategory(self, name, isSubCategory, parentCategory):
        '''Permite insertar una categoria'''

        # None checks
        name = name or ""
        isSubCategory = isSubCategory or False
        parentCategory = parentCategory or 0

        findCategory = self.getCategoryByName(name)

        findParent = self.getCategoryById(parentCategory)

        if findCategory is None:
            if findParent != [] or (parentCategory == 0):
                newCategory = Category(name, isSubCategory, parentCategory)
                db.session.add(newCategory)
                db.session.commit()
                return {'status': 'success', 'reason': 'Category Created'}

            else:
                return {'status': 'failure', 'reason': 'Parent category not found'}

        return {'status': 'failure', 'reason': 'The category is already created'}

    def deleteCategory(self, id):
        '''Permite eliminar una categoria'''

        findCategory = self.getCategoryById(id)

        if findCategory != []:
            self.query.filter_by(categoryId=id).delete()
            db.session.commit()

            return {'status': 'success', 'reason': 'Category deleted'}

        return {'status': 'failure', 'reason': 'Couldnt find Category :('}

    def updateCategory(self, categoryId, name=None, isSubCategory=None, parentCategory=None):
        '''Permite actualizar una categoria'''

        # None checks
        name = name or ""

        findCategory = self.getCategoryById(categoryId)

        if findCategory != []:

            # Si el name no es none
            if name != "":
                findCategory.name = name

            if isSubCategory != None:
                if parentCategory is None:
                    findParent = []
                else:
                    findParent = self.getCategoryById(parentCategory)
                if findParent != []:
                    findCategory.parentCategory = parentCategory
                    findCategory.isSubCategory = isSubCategory
                    db.session.commit()
                    return {'status': 'success', 'reason': 'Category updated'}

                else:
                    return {'status': 'failure', 'reason': 'Parent category not found'}

            else:
                findCategory.parentCategory = 0
                findCategory.isSubCategory = False
                db.session.commit()
                return {'status': 'success', 'reason': 'Category updated'}

        else:
            return {'status': 'failure', 'reason': 'Category does not exist, Use create instead'}
