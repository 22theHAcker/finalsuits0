from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
from .models import User, Note, Suit


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'this is the best website 100/100'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views, suits
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(suits, url_prefix='/')

    from .models import User, Note, Suit

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            sample_suit = Suit(name='Sample Suit', price= 199.99, color='Black', size='M')
            db.session.add(sample_suit)
            db.session.commit()
        print('Created Database!')
