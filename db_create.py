#!flask/bin/python
from app.models.db import db

from app.models.user import *
from app.models.band import *
from app.models.disc import *
from app.models.state import *
from app.models.article import *
from app.models.new import *

db.create_all()
