from flask import Flask, render_template
from auth.blueprint import auth
from admin.blueprint import admin

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(admin)
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example')
def example():
    return render_template('example.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    #snip
    return render_template('404.html'), 404


db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
    from models import User
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
if '__main__' == __name__:
    app.run('0.0.0.0',5000, debug=True)