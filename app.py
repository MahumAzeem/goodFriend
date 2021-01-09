import os
import datetime
import hashlib
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def root():
    return "hello WOrd"
