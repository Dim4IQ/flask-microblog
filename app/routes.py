from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = { 'username': 'Dim4IQ'}
    posts = [
        {
            'author': { 'username': 'Ruslan'},
            'body': 'Beautiful day in Voronezh!'
        },
        {
            'author': { 'username': 'Ayka'},
            'body': 'The Holop2 film was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)