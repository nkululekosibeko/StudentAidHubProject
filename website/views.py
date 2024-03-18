from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from website import db
from website.models import Bursaries

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
    # Creating a new bursary.

    if request.method == 'POST':

        bursary_id = request.form.get('bursary_id')
        field_of_study_id =request.form.get('field_of_study_id')
        field_of_study = request.form.get('field_of_study')
        bursary_name = request.form.get('bursary_name')
        closing_date = request.form.get('closing_date')
        application_link = request.form.get('application_link')
        about_sponsor = request.form.get('about_sponsor')
        about_bursary = request.form.get('about_bursary')
        eligibility_criteria = request.form.get('eligibility_criteria')
        to_be_covered = request.form.get('to_be_covered')
        documents_required = request.form.get('documents_required')

        # Creating a new bursary.
        new_bursary = Bursaries(bursary_id=bursary_id, field_of_study_id=field_of_study_id, field_of_study=field_of_study, bursary_name=bursary_name, closing_date=closing_date,
                              application_link=application_link, about_sponsor=about_sponsor, about_bursary=about_bursary, eligibility_criteria=eligibility_criteria,
                              to_be_covered=to_be_covered, documents_required=documents_required)
        db.session.add(new_bursary)
        db.session.commit()

        flash('New bursary created successfully!.', 'success')
        return redirect(url_for('main.admin_bursaries'))


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