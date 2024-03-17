from flask import Flask
from .models import db
from .views import main_bp
from .auth import auth_bp
from flask_login import LoginManager

# Import your User model here
from .models import User

# Initialize Flask-Login
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AfroPhoenix'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///StudentAidHub.db'

    db.init_app(app)
    login_manager.init_app(app)  # Initialize Flask-Login

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app

# Tell Flask-Login how to load a user from a user ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
