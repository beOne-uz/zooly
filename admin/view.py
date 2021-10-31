from .blueprint import admin
from flask import render_template
from flask_login import login_required 

@admin.route('/')
def admin_panel():
    return render_template('/admin/index.html')




