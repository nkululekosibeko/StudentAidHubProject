from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class FieldOfStudy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class Bursaries(db.Model):
    bursary_id = db.Column(db.String(12), primary_key=True)
    field_of_study_id = db.Column(db.Integer, db.ForeignKey('field_of_study.id'), nullable=False)
    field_of_study = db.relationship('FieldOfStudy', backref=db.backref('bursaries', lazy=True))
    bursary_name = db.Column(db.String(250), nullable=False)
    closing_date = db.Column(db.Date, nullable=False)
    application_link = db.Column(db.String(250), nullable=False)
    about_sponsor = db.Column(db.String(100000), nullable=False)
    about_bursary = db.Column(db.String(100000), nullable=False)
    eligibility_criteria = db.Column(db.String(100000), nullable=False)
    to_be_covered = db.Column(db.String(100000), nullable=False)
    documents_required = db.Column(db.String(100000), nullable=False)



    # Implement required methods for Flask-Login
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


