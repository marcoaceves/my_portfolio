import re
from flask import flash, jsonify, request, redirect, session, url_for, render_template

from flask_app import app

from email.message import EmailMessage
import smtplib

import json
import os



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marco')
def new_index():
    return render_template("marco.html") 


@app.route("/project-1")
# AHF APP
def project1():
    project_img="static/img/projects/project-1.png"
    project_title='Work Management <span>Web Application</span>'
    project_frontend='HTML, CSS, Javascript, Bootstrap'
    project_backend='Python, Flask'
    project_database=' MySQL, AWS Ubuntu Server(Deployment)' 

    project_description='Custom Built for AHF Pharmacy, A work Management Web Application that allows a Manager to assign tasks to employees. Employees can update their tasks throughout the day.'
    return render_template('project.html', project_title=project_title, project_description=project_description, project_img=project_img, project_frontend=project_frontend, project_backend=project_backend, project_database=project_database)

@app.route("/project-2")
# ubiquity
def project2():
    return render_template('project.html')

@app.route("/project-3")
# Project Collab
def project3():
    return render_template('project.html')

@app.route("/project-4")
def project4():
    return render_template('project.html')




@app.route("/a", methods=['POST'])
def massage():
    data = request.form
    print(data)
    name = request.form['name']
    contact = request.form['email']
    message = request.form['message']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('cosmicmarcobrahma@gmail.com', "pazsmajysencrhcj")
    email = EmailMessage()
    email['From'] = 'cosmicmarcobrahma@gmail.com'
    email['To'] = 'mr.aceves@gmail.com'
    email['Subject'] = 'Marco Portfolio Contact'
    email.set_content(f"{name} has a message {message} Please reply at {contact}")
    server.send_message(email)
    return jsonify ({'flash': "Thank you for contacting me, I have received your message and will respond soon."})