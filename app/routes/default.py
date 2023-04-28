from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

# This is for rendering the home page
@app.route('/home')
def home():
    return render_template('home.html')

# I think this is for rendering the aboutUs page
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/controlroom')
def aboutus():
    return render_template('controlroom.html')
