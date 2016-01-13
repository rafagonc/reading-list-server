from flask import Flask
from db import db
from api import api
from ma import ma
import os

def create_app(app):
    #config
    app.config.from_object(os.environ['APP_SETTINGS'])

    #models
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)

    with app.app_context():

        import models
        db.drop_all()
        db.create_all()


app = Flask(__name__)
create_app(app)

if __name__ == '__main__':
    app.run()
