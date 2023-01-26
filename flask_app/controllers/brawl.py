from flask import flash, request, redirect, session, url_for, render_template, json
import requests
from flask_app import app


import flask_app.controllers.creds as creds
token=creds.brawl_token
@app.route('/brawlstars')
def brawlers():
    # random date generator
    tokens = token.strip()
    headers = {"Authorization": f"Bearer {tokens}"}

    

    url= f'https://api.brawlstars.com/v1/brawlers'

    response = requests.get(url, headers=headers) 


    
    brawlers_data = response.json()
    # print(brawlers_data, "random data")
    print(brawlers_data["items"][1], "random data")


    return render_template('marco.html', brawlers_data=brawlers_data)