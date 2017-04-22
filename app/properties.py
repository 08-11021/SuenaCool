# -*- coding: utf-8 -*-

maxUsers = 16
maxFullName = 50
maxPassword = 200
maxEmail = 30
maxStateName = 30
maxBandName = 30
maxDiscName = 60
maxGenreName = 60
articleTypes = ['Chronic','Interview','Opinion']
newTypes = ['Event','Newspaper','Release']

#User Model responses
responseUserAlreadyExist = {'status': 'failure', 'msg': 'El usuario ya existe'}
responseUserInvalidAttributes = {'status': 'failure', 'msg': 'Los campos exceden el limite de caracteres'}
responseUserUpdated = {'status': 'success', 'msg': 'La informacion de usuario ha sido actualizada'}
responseUserNotUpdated = {'status': 'failure', 'msg': 'La informacion de usuario no ha podido ser actualizada'}
responseUserCreated = {'status': 'success', 'msg': 'El usuario fue creado exitosamente'}
responseUserNotCreated = {'status': 'failure', 'msg': 'El usuario no pudo ser creado'}
responseUserDeleted = {'status': 'success', 'msg': 'El usuario ha sido eliminado'}
responseUserNotDeleted = {'status': 'failure', 'msg': 'El usuario no pudo ser eliminado'}

#Band Model responses
responseBandCreated = {'status': 'success', 'msg': 'La banda fue creada'}
responseBandNotCreated = {'status': 'failure', 'msg': 'La banda no pudo ser creada'}
responseBandUpdated = {'status': 'success', 'msg': 'La banda fue actualizada'}
responseBandNotUpdated = {'status': 'failure', 'msg': 'La banda no pudo ser actualizada'}
responseBandDeleted = {'status': 'success', 'msg': 'La banda fue eliminada'}
responseBandNotDeleted = {'status': 'failure', 'msg': 'La banda no pudo ser eliminada'}

#Disc Model responses
responseDiscCreated = {'status': 'success', 'msg': 'El disco fue creado'}
responseDiscNotCreated = {'status': 'failure', 'msg': 'El disco no pudo ser creado'}
responseDiscUpdated = {'status': 'success', 'msg': 'El disco fue actualizado'}
responseDiscNotUpdated = {'status': 'failure', 'msg': 'El disco no pudo ser actualizado'}
responseDiscDeleted = {'status': 'success', 'msg': 'El disco fue eliminado'}
responseDiscNotDeleted = {'status': 'failure', 'msg': 'El disco no pudo ser eliminado'}

#New Model responses
responseNewInvalidType = {'status': 'false', 'msg': 'El tipo de la noticia no es valido'}
responseNewCreated = {'status': 'success', 'msg': 'Noticia creada exitosamente'}
responseNewNotCreated = {'status': 'failure', 'msg': 'La noticia no pudo ser creada'}
responseNewUpdated = {'status': 'success', 'msg': 'La noticia ha sido actualizada'}
responseNewNotUpdated = {'status': 'failure', 'msg': 'La noticia no ha podido ser actualizada'}
responseNewDeleted = {'status': 'success', 'msg': 'La noticia ha sido eliminada'}
responseNewNotDeleted = {'status': 'failure', 'msg': 'La noticia no ha podido ser eliminada'}

#Article Model responses
responseArticleInvalidType = {'status': 'failure', 'msg': 'El articulo no pudo ser creado'}
responseArticleCreated = {'status': 'success', 'msg': 'Articulo creado exitosamente'}
responseArticleNotCreated = {'status': 'failure', 'msg': 'El articulo no pudo ser creado'}
responseArticleUpdated = {'status': 'success', 'msg': 'El articulo ha sido actualizado'}
responseArticleNotUpdated = {'status': 'failure', 'msg': 'El articulo no ha podido ser actualizado'}
responseArticleDeleted = {'status': 'success', 'msg': 'El articulo ha sido eliminado'}
responseArticleNotDeleted = {'status': 'failure', 'msg': 'El articulo no ha podido ser eliminado'}

states =[u'Amazonas',
         u'Anzoátegui',
         u'Apure',
         u'Aragua',
         u'Barinas',
         u'Bolívar',
         u'Carabobo',
         u'Cojedes',
         u'Delta Amacuro',
         u'Distrito Capital',
         u'Falcón',
         u'Guárico',
         u'Lara',
         u'Mérida',
         u'Miranda',
         u'Monagas',
         u'Nueva Esparta',
         u'Portuguesa',
         u'Sucre',
         u'Táchira',
         u'Trujillo',
         u'Vargas',
         u'Yaracuy',
         u'Zulia']





