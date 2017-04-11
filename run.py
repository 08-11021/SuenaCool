from app import app
from random import SystemRandom
app.config.update(
    SECRET_KEY=repr(SystemRandom().random())
)
app.run(debug = True)
