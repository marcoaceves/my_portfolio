from flask import flash, request, redirect, session, url_for, render_template, json
import requests
from flask_app import app


import flask_app.controllers.creds as creds
token=creds.brawl_token
@app.route('/brawlstars')
def brawlers():
    url= f'https://api.brawlapi.com/v1/brawlers'

    response = requests.get(url) 

    brawlers_data = response.json()
    # print(brawlers_data, "random data")
    print(brawlers_data["list"][1], "random data")


    return render_template('brawl.html', brawlers_data=brawlers_data)


@app.route('/brawler/<int:brawler_id>')
def display_brawler(brawler_id):
    url= f'https://api.brawlapi.com/v1/brawlers/{brawler_id}'

    response = requests.get(url) 

    brawlers_data = response.json()
    # print(brawlers_data, "random data")
    print(brawlers_data, "brawler_data")


    return render_template('brawler.html', brawlers_data=brawlers_data )