#!flask/bin/python
from app.models.db import db
from app.models.user import *
from app.models.profile import *
from app.models.category import *
from app.models.service import *
from app.models.quotation import *
from app.models.contract import *
from app.models.reputation import *
from app.models.suscription import *
db.create_all()
