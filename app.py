import os
import datetime
import hashlib
import sys
from friend import Friend
from database import addFriend
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/friend_info")
def friend_info():
    return render_template('friend_info.html')

@app.route("/add_friend", methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST': #When the add friend button is pressed
        r = request.form
        #print("!!!!!!!!!!!!!!!!!", file=sys.stderr)
        ##print(r.get('first_name') + r.get('last_name'), file=sys.stderr)
        
        birthday = r.get('date')
        birthday_s = birthday.split('/') ##[mm,dd,yyyy]


        friend = Friend(
            name= str(r.get('first_name')) + " " + str(r.get('last_name')), 
            pronouns = str(r.get('pronouns')),
            birthdate=datetime.date(int(birthday_s[2]),int(birthday_s[0]),int(birthday_s[1])), #datetime.date takes (yyyy,mm,dd)  
            phone=str(r.get('phone_number')),
            allergies=str(r.get('allergies')),
            optional1={str(r.get('optional1-name')):str(r.get('optional1-text'))},
            optional2={str(r.get('optional2-name')):str(r.get('optional2-text'))},
            optional3={str(r.get('optional3-name')):str(r.get('optional3-text'))},
            optional4={str(r.get('optional4-name')):str(r.get('optional4-text'))}
        )
        f = addFriend()
        f.add(friend)
        return str(r.get('date'))

    if request.method == 'GET':
        #load page that has the form to add friend
        return render_template('add_friend.html')

@app.route("/dashboard")
def load_dashboard():
    current_user = app.config['USER']
    # friends_list = db.get_friends(limit=100) #scrollable?
    # upcoming_events = db.get_upcoming_events(limit=4)
    # return render_template('index.html', user, friends_list, upcoming_events)
    return "Hello " + current_user

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)