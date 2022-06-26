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