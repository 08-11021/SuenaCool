# -*- coding: utf-8 -*-.

from app.models.db import db
from app.models.user import User



class Profile(db.Model):
    '''Clase que define el modelo Usuario'''

    __tablename__ = 'profile'
    perfilId        = db.Column(db.Integer, primary_key=True, index=True)
    email           = db.Column(db.String(30), db.ForeignKey('user.email'))
    gender          = db.Column(db.String(20))
    age             = db.Column(db.Integer)
    vision          = db.Column(db.String(300))
    abilities       = db.Column(db.String(300))
    skills          = db.Column(db.String(300))
    formation       = db.Column(db.String(30))
    experience      = db.Column(db.String(300))
    courses          = db.Column(db.String(300))
    workshops       = db.Column(db.String(300))
    seminars        = db.Column(db.String(300))
    papers          = db.Column(db.String(300))
    publications    = db.Column(db.String(300))
    scholarships     = db.Column(db.String(300))


    def __init__(self, email=None, gender=None, age=None, vision=None,
                abilities=None, skills=None, formation=None,
                experience=None, courses=None, workshops=None,
                seminars=None, papers=None, publications=None,
                 scholarships=None):

        '''Constructor del modelo usuario'''
        self.email          = email
        self.gender         = gender
        self.age            = age
        self.vision         = vision
        self.abilities      = abilities
        self.skills         = skills
        self.formation      = formation
        self.experience     = experience
        self.courses         = courses
        self.workshops      = workshops
        self.seminars       = seminars
        self.papers         = papers
        self.publications   = publications
        self.scholarships    = scholarships


    def __repr__(self):
        '''Representacion en string del modelo Perfil'''
        return \
            '< email %r, gender %r, age %r (incompleto)>' % (
                self.email, self.gender, self.age)

    def getProfileById(self, id):
        '''Permite buscar un usuario por su id'''

        if (type(id) != int):
            return {'status': 'failure', 'reason': ' Id not integer'}
        else:
            profile = self.query.filter_by(perfilId=id).all()
            return profile

    def createProfile(self, email, gender, age, vision, abilities,
        skills, formation, experience, courses, workshops,
        seminars, papers, publications, scholarships):

        '''Permite crearle un perfil a un usuario'''

        # None checks
        email           = email or ""
        gender          = gender or ""
        age             = age or ""
        vision          = vision or ""
        abilities       = abilities or ""
        skills          = skills or ""
        formation       = formation or ""
        experience      = experience or ""
        courses          = courses or ""
        workshops       = workshops or ""
        seminars        = seminars or ""
        papers          = papers or ""
        publications    = publications or ""
        scholarships     = scholarships or ""

        u = User()
        findUser = u.getUserByEmail(email)

        findProfile = self.getProfileByEmail(email)

        if findProfile == None:

            if findUser != []:
                newProfile = Profile(email,gender,age,vision,abilities,skills,
                    formation,experience,courses,workshops,seminars,papers,
                    publications,scholarships)
                db.session.add(newProfile)
                db.session.commit()
                return {'status': 'success', 'reason': 'Profile created'}
        else:
            return {'status': 'failure', 'reason': 'Profile already created, Use modify instead'}

        return {'status': 'failure', 'reason': 'Couldnt find user  :( '}



    def getProfiles(self):
        '''Permite obtener todos los perfiles'''

        result = self.query.all()
        return result


    def getProfileByEmail(self, email):
        '''Permite buscar un perfil por su correo'''
        profiles = self.query.filter_by(email=email).all()

        if profiles:
            profile = profiles[0]
        else:
            profile = None

        return profile

    def updateProfile(self, email=None, gender=None, age=None, vision=None, abilities=None,
        skills=None, formation=None, experience=None, courses=None, workshops=None,
        seminars=None, papers=None, publications=None, scholarships=None):
        '''Permite actualizar el perfil de un usuario'''

        # None checks
        email           = email or ""
        gender          = gender or ""
        age             = age or ""
        vision          = vision or ""
        abilities       = abilities or ""
        skills          = skills or ""
        formation       = formation or ""
        experience      = experience or ""
        courses          = courses or ""
        workshops       = workshops or ""
        seminars        = seminars or ""
        papers          = papers or ""
        publications    = publications or ""
        scholarships     = scholarships or ""

        u = User()
        findUser = u.getUserByEmail(email)

        findProfile = self.getProfileByEmail(email)

        if findUser != []:

            if findProfile != None:

                if gender != "":
                    findProfile.gender = gender
                if age != "":
                    findProfile.age = age
                if vision != "":
                    findProfile.vision = vision
                if abilities != "":
                    findProfile.abilities = abilities
                if skills != "":
                    findProfile.skills = skills
                if formation != "":
                    findProfile.formation = formation
                if experience != "":
                    findProfile.experience = experience
                if courses != "":
                    findProfile.courses = courses
                if workshops != "":
                    findProfile.workshops = workshops
                if seminars != "":
                    findProfile.seminars = seminars
                if papers != "":
                    findProfile.papers = papers
                if publications !="":
                    findProfile.publications = publications
                if scholarships != "":
                    findProfile.scholarships = scholarships

                db.session.commit()

                return {'status': 'success', 'reason': 'Profile updated'}

            else:
                return {'status': 'failure', 'reason': 'Profile doesnt exists, Use create instead'}

        else:

            return {'status': 'failure', 'reason': 'Couldnt find user  :( '}




    def deleteProfile(self, id):
        ''' permite borrar un perfil de un usuario '''

        findProfile = self.getProfileById(id)

        if findProfile != {'status': 'failure', 'reason': ' Id not integer'}:
            self.query.filter_by(perfilId=id).delete()
            db.session.commit()
            return {'status': 'success', 'reason': 'Profile deleted'}
        else:
            return {'status': 'failure', 'reason': 'Couldnt find Profile :('}

