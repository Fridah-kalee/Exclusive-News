# from app import app
import urllib.request,json
from .models import Article,Source

api_key =None
base_url =None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url= app.config['NEWS_API_BASE_URL']
    

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url= base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list =get_articles_response['articles']
            article_results = process_results(article_results_list)

    return article_results

def get_article(name):
    get_article_url = base_url.format(name,api_key)
    with urllib.request.urlopen(get_article_outcome_url) as url:
        article_outcome_data = url.read()
        article_outcome_response = json.loads(article_output_data)

        article_object = None

        if article_outcome_response:
            source = article_outcome_response("source")
            author = article_outcome_response("author")
            description = article_outcome_response("description")
            title = article_outcome_response("title")
            url = article_outcome_response("url")
            urlToImage = article_outcome_response("urlToImage")
            publishedAt = article_outcome_response("publishedAt")
            content = article_outcome_response("content")

            article_object =Article(source, author, description, title, url, urlToImage, publishedAt,content)

    return article_object

#processing results
def process_results(article_list):
    article_result = []
    for article_item in article_list:
        source = article_item.get("source")
        author = article_item.get("author")
        description = article_item.get("description")
        title = article_item.get("title")
        url = article_item.get("url")
        urlToImage = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")
        content = article_item.get("content")

        if content:
            articles_object = Article(source, author, description, title, url, urlToImage, publishedAt,content)
            article_result.append(articles_object)

    return article_result

def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_results(search_article_list)


    return search_article_results                