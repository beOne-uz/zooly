from .blueprint import auth
from flask import render_template

@auth.route('/')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')