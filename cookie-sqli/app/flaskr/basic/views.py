import re
import datetime

from flask import render_template_string, request, render_template, current_app, flash, redirect, url_for, session, make_response
from . import app


def isLoggedIn(session):
    r = current_app.db.execute(f"select * from admins where session = {session}").first()
    return r != None

@app.route('/', methods=["GET","POST"])
def home():
    # check cookie via db
    if isLoggedIn(request.cookies.get("session","123")):
        return render_template("flag.html")
    
    if request.method == "POST":
        # you can't just login lol use some sqli fuckboi
        flash('Unknown Username/Password', 'danger')
    resp = make_response(render_template("home.html"))
    resp.set_cookie('session', '123')
    return resp


@app.route('/ping')
def ping():
    return "pong"


@app.route('/flag_debug', methods=["POST"])
def flag_debug():
    if request.form.get("flag_secret", "") == current_app.config['FLAG_SECRET']:
        return current_app.config['FLAG']
    return ":(", 401
