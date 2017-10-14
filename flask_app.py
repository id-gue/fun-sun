
# A very simple Flask Hello World app for you to get started with...
# copied from pythonanywhere.com

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)