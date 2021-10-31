from flask import Blueprint

admin = Blueprint('admin', __name__, static_folder='static', 
                                    static_url_path='/static/admin', 
                                    template_folder='/templates/admin',
                                    url_prefix='/admin')


from .view import *