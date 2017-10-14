
# A very simple Flask Hello World app for you to get started with...
# copied from pythonanywhere.com

from flask import Flask
from flask import render_template
from .forms import LoginForm

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)