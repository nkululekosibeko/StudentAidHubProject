from flask import Flask
from .models import db
from .views import main_bp
from .auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AfroPhoenix'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///StudentAidHub.db'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
