from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/multiplayer')
def multiplayer():
    return render_template('multiplayer.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/daily')
def daily():
    return render_template('daily.html')


@app.route('/practise')
def practise():
    return render_template('practise.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/countdown_prc')
def countdown_prc():
    return render_template('countdown_game.html')

@app.route('/timer')
def timer():
    return render_template('timer.html')

if __name__ == "__main__":
    app.run(debug=True)
