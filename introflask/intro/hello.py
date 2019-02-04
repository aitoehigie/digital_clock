#!/usr/bin/env python

from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index():
    months = [pyth]
    return render_template("index.html")
