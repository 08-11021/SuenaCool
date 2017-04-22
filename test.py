import unittest
import datetime
from app.models.user import *
from app.models.state import *
from app.models.band import *
from app.models.disc import *
from app.utility.encoder import *

class TestModel(unittest.TestCase):

    def testUserCRUD(self):
        email = 'globerusso@gmail.com'
        fullname = 'Gabriel Russo'
        editedFullName = 'Gabriel A Russo'
        password = toMd5('17744256')
        rol = 1

        user = User(email, fullname, password, rol)
        self.assertEqual(user.createUser(email, fullname, password, rol), properties.responseUserCreated, 'Usuario Creado')
        self.assertNotEqual(user.getUsers(), [], 'Usuario insertado en la base de datos')
        self.assertEqual(user.createUser(email, fullname, password, rol), properties.responseUserAlreadyExist, 'Usuario duplicado no admitido')
        user = user.getUserByEmail(email)
        self.assertEqual(user.fullname, fullname, 'Usuario obtenido por email')
        user.fullname = editedFullName
        user.update()
        self.assertEqual(user.getUserByEmail(email).fullname, editedFullName, 'Informacion de usuario modificada')
        self.assertEqual(user.delete(), properties.responseUserDeleted)
        self.assertEqual(user.delete(), properties.responseUserNotDeleted)

    def testStateCRUD(self):
        stateObject = State('')
        if stateObject.getStates() == []:
            for state in properties.states:
                stateObject.createState(state)
        self.assertNotEqual(stateObject.getStates(), [], 'Estados insertados en la base de datos')
        self.assertEqual(len(stateObject.getStates()), 24, 'Estados completos en base de datos')
        self.assertEqual(len(stateObject.getStatesByName("A")), 20 , 'Estados filtrados correctamente')

    def testBandCRUD(self):
        bandName = 'Test Band Name'
        bandState = 1
        bandName2 = 'Name Test Band'

        band = Band(bandName, bandState)
        self.assertEqual(band.createBand(bandName,bandState), properties.responseBandCreated, 'Estado insertado correctamente')
        self.assertEqual(band.createBand(bandName2,bandState), properties.responseBandCreated, 'Estado insertado correctamente')
        self.assertNotEqual(band.getBands(),[], 'Lista de bandas no es vacia')
        self.assertNotEqual(band.getBandsByName('Test'),[],'Bandas consultadas correctamente')
        self.assertNotEqual(band.getBandsByStateId(1), [], 'Bandas consultadas correctamente')
        bands = band.getBandsByStateId(1)
        bands[0].setBandPic('http://www.picture.com/12345')
        bands[0].setBandReview('Esto es un review de una banda para probar la actualizacion de la misma. No posee ningun sentido')
        self.assertEqual(bands[0].update(),properties.responseBandUpdated,'banda actualizada correctamente')
        for band in bands:
            band.delete()
        self.assertEqual(band.getBandsByName('Test'), [], 'Bandas eliminadas correctamente')
        self.assertEqual(band.getBandsByStateId(1), [], 'Bandas eliminadas correctamente')

    def testDiscCRUD(self):
        bandName = 'Test Band Name'
        bandState = 1
        name = 'Disc number 1'
        date = datetime.date(2017,02,06)
        genre = 'Rock'
        disc = Disc('', date, '', '0')
        band = Band(bandName, bandState)
        band.createBand(bandName, bandState)
        self.assertEqual(disc.createDisc(name, date, genre, band.ig), properties.responseDiscCreated, 'Disco creado exitosamente')

if __name__ == '__main__':
    unittest.main()
