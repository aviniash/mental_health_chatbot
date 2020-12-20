# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:30:46 2020

@author: Aznida
"""
from chatbot_function import *
from flask import Flask, render_template, request

global emotion_array
emotion_array = []

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot_response(userText))

@app.route("/getsentiment")
def get_bot_sentiment():
    userText = request.args.get('msg')
    sent_msg = [userText]
    return str('Based on my sentiment calculation you are currently feeling "'+sentiment_response(sent_msg)+'"')

if __name__ == "__main__":
    app.run()