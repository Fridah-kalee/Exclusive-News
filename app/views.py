from flask import render_template
from app import app
from .request import get_articles
 

#views
@app.route('/')#localhost:5000/
def index():
    '''
    View root page function that returns the front page and its data
    '''
    #Getting Trending article
    trending_articles = get_articles('trending')
    print(trending_articles)
    
    return render_template('index.html',trending = trending_articles)
