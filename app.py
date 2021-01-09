import os
import datetime
import hashlib
from friend import Friend
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')


@app.route("/")
def root():
    return "hello WOrd"

@app.route("/add_friend", methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST': #When the add friend button is pressed
        r = request.form
        friend = Friend(
            first_name=r.get('first_name'), 
            last_name=r.get('last_name'),
            birthdate=datetime.date(int(r.get('birthyear')),int(r.get('birthmonth')),int(r.get('birthday')))
            # birthdate=datetime.date(request.form.get('birthyear'), request.form.get('birthmonth'), request.form.get('birhtday'))
        )
        return "Friend Added page"

    if request.method == 'GET':
        #load page that has the form to add friend
        return "Add friend form"

@app.route("/dashboard")
def load_dashboard():
    current_user = app.config['USER']
    # friends_list = db.get_friends(limit=100) #scrollable?
    # upcoming_events = db.get_upcoming_events(limit=4)
    # return render_template('index.html', user, friends_list, upcoming_events)
    return "Hello " + current_user
