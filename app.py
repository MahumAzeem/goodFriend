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
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        
        friend = Friend(first_name=first_name, last_name=last_name)
        return "ok"
