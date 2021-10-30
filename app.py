from flask import Flask, render_template
from auth.blueprint import auth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(auth)
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    #snip
    return render_template('404.html'), 404

if '__main__' == __name__:
    app.run('127.0.0.1',5000, debug=True)