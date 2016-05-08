from flask import Flask, url_for
from db import db
from ma import ma
from endpoints import blueprint as endpoints
import os

def create_app(app):
    #config
    app.config.from_object(os.environ['APP_SETTINGS'])

    #models
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        from models.book import Book
        from models.author import Author
        from models.rating import Rating
        from models.category import Category
        from models.user import User
        from models.log import ReadingLog
        db.create_all()
        db.session.commit()

        #create endpoints
        app.register_blueprint(endpoints)

app = Flask(__name__)
create_app(app)

if __name__ == '__main__':
    app.run()
