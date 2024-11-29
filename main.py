#!/bin/python3
from flask import Flask, render_template,request, send_from_directory
from flask import make_response

import os
from os.path import join, dirname

app = Flask(__name__, template_folder=".")

@app.route("/rss")
def rss():
    rss_xml = render_template('rss.xml')
    response = make_response(rss_xml)
    response.headers['Content-Type'] = 'application/rss+xml'
    return response
    
@app.route("/atom")
def atom():
    atom_xml = render_template('atom.xml')
    response = make_response(atom_xml)
    response.headers['Content-Type'] = 'application/atom+xml'
    return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template("index.html")

