from flask import Flask, render_template, Blueprint, abort
from auth.blueprint import auth

app = Flask(__name__)
app.register_blueprint(auth)

@app.route('/')
def index():
    return render_template('index.html')

if '__main__' == __name__:
    app.run('127.0.0.1',5000, debug=True)