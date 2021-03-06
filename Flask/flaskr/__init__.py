import os
from flask import Flask , render_template, request
from flask_bootstrap import Bootstrap
from flaskr.db import DBHelper
from flaskr.Database.UserDB import UserDB


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    #Database
    dbHelper = DBHelper()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    Bootstrap(app)

    # Landing page
    @app.route('/')
    def Landing():
        return render_template("landing.html")

    #Login page 
    @app.route('/login', methods=['GET', 'POST'])
    def Login():
        #POST
        if request.method == "POST":
            print("Post Login")
            result = dbHelper.Login(str(request.form['email']),str(request.form['password']))
            if result == DBHelper.LOGIN_SUCCESS:
                return render_template("events.html")
            else:
                return render_template("login.html",loginCheck =result)

        return render_template("login.html")

    #Registration page 
    @app.route('/register', methods=['GET', 'POST'])
    def Register():
        if request.method == "POST":
            newUser = UserDB(str(request.form['email']),str(request.form['password']),str(request.form['userType']))
            result = dbHelper.AddUser(newUser)
            print(result)
            if result == dbHelper.REGISTRATION_SUCCESS:
                #called when registration is a success.
                return render_template("register.html",registrationCheck = result)
            else:
                #called when registration was a failure.
                return render_template("register.html",registrationCheck = result)

        #called when first get on the page
        return render_template("register.html")

    #Profile for creator 
    @app.route('/creator')
    def Creator():
        return render_template("auth/creator.html")

    #Profile for user
    @app.route('/user')
    def User():
        return render_template("user/user.html")

    #Events page
    @app.route('/events')
    def Events():
        return render_template("events.html")

    return app