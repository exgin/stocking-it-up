from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User
from forms import LoginForm, RegisterForm
from scrape import get_names_values, get_names, combine

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///stock_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def redirct_page():
    """Redirct to homepage"""

    return redirect('/home')

@app.route('/home')
def home_page():
    """Display home page"""

    return render_template('home.html')