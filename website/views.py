from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home_page.html')

@main_bp.route('/admin/dashboard')
# @login_required
def admin_dashboard():
    # Makes sure only the admin can access this page
    # if not current_user.is_admin:
    #     return redirect(url_for('main.home'))
    return render_template('admin_dashboard.html')

@main_bp.route('/admin/dashboard/admin_bursaries')
def admin_bursaries():
    return render_template('admin_bursaries.html')

@main_bp.route('/admin/dashboard/admin_profile')
def admin_profile():
    return render_template('admin_profile.html')

@main_bp.route('/admin/dashboard/admin_users_list')
def admin_users_list():
    return render_template('admin_users_list.html')

@main_bp.route('/student/dashboard')
# @login_required
def student_dashboard():
    # Makes sure only the student can access this page
    # if current_user.is_admin:
    #     return redirect(url_for('main.home'))
    return render_template('student_dashboard.html')

@main_bp.route('/student/dashboard/student_notifications')
def student_notifications():
    return render_template('student_notifications.html')

@main_bp.route('/student/dashboard/student_profile')
def student_profile():
    return render_template('student_profile.html')

@main_bp.route('/more_bursary_info')
def more_bursary_info():
    return render_template('more_info_students_btn.html')