from .blueprint import auth 
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        from models import User

        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        return redirect(url_for('admin.admin_panel'))
    

@auth.route('/profile')
def profile():
    return 'Profile'

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST': 

            from models import User
            from app import db 

            email = request.form.get('email')
            name = request.form.get('first_name')
            surname = request.form.get('surname')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

            if user:
                flash('Email address already exists') # if a user is found, we want to redirect back to signup page so user can try again
                return redirect(url_for('auth.signup'))

            fullname = str(name) + ' '+ str(surname)
            # create a new user with the form data. Hash the password so the plaintext version isn't saved.
            new_user = User(email=email, name=fullname, password=generate_password_hash(password, method='sha256'))

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit() 

            return redirect(url_for('auth.login'))