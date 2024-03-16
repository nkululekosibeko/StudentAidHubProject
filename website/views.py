from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home_page.html')

@main_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Makes sure only the admin can access this page
    if not current_user.is_admin:
        return redirect(url_for('main.home'))
    return render_template('admin_dashboard.html')

@main_bp.route('/student/dashboard')
@login_required
def student_dashboard():
    # Makes sure only the student can access this page
    if current_user.is_admin:
        return redirect(url_for('main.home'))
    return render_template('student_dashboard.html')
