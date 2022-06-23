import re
from unittest.mock import DEFAULT
from flask import flash, jsonify, request, redirect, session, url_for, render_template

from flask_app import app

from email.message import EmailMessage

from flask_mail import Mail, Message
import smtplib

import json



@app.route('/')
def index():
    return render_template('index.html')




@app.route("/a", methods=['POST'])
def massage():

    name = request.form['name']
    contact = request.form['email']
    message = request.form['message']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('ahf.task.manager@gmail.com', 'xrhkeiruhpcazfws')
    email = EmailMessage()
    email['From'] = 'ahf.task.manager@gmail.com'
    email['To'] = 'mr.aceves@gmail.com'
    email['Subject'] = 'Marco Portfolio Contact'
    email.set_content(f"{name} has a message {message} Please reply at {contact}")
    server.send_message(email)
    return jsonify ({'flash': "Thank you for contacting me, I have received your message and will respond soon."})