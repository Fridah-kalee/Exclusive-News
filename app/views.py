from flask import render_template
from app import app
from .request import get_articles
 

#views
@app.route('/')#localhost:5000/
def index():
    '''
    View root page function that returns the front page and its data
    '''
    #Getting entertainment article
    entertainment_articles = get_articles('entertainment')
    business_articles =get_articles('business')
    health_articles =get_articles('health')

    
    
    return render_template('index.html',entertainment = entertainment_articles, business =business_articles, health = health_articles)
