from flask import render_template,request,redirect,url_for
from app import app
from .request import get_articles,get_article,search_article
 

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

    search_article= request.args.get('article_query')
    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
        return render_template('index.html',entertainment = entertainment_articles, business =business_articles, health = health_articles)

@app.route('/article/<name>')
def article(name):
    article = get_article(name)
    return render_template(article.html,article=article)

@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',articles = searched_articles)    

