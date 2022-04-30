from flask import render_template
from app import app

#views
@app.route('/')#localhost:5000/
def FrontPage():
    '''
    View root page function that returns the front page and its data
    '''
    return render_template('source.html')
