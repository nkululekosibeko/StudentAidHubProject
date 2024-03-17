from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Checks if it's admin that is signing in
        if email == 'admin@gmail.com' and password == 'admin':
            # Set session for admin
            session['admin_logged_in'] = True
            flash('Admin logged in successfully!', 'success')
            return redirect(url_for('admin.dashboard'))

        # Check if it's a student that is signing in
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # Set session for student
            session['student_logged_in'] = True
            flash('Student logged in successfully!', 'success')
            return redirect(url_for('student.dashboard'))

        flash('Invalid username or password', 'error')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    session.pop('student_logged_in', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if an email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('email already exists!', 'error')
            return redirect(url_for('auth.signup'))

        # Creating a new user
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')
