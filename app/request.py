from app import app
import urllib.request,json
from .models import articles

Article=articles.Article

api_key =None
base_url =None

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting news base url
base_url= app.config['NEWS_API_BASE_URL']




def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            articles_results_list =get_articles_response['articles']
            article_results = process_results(article_results_list)

            return article_results

def get_article_everything(query):
    get_articles_url = 'https://newsapi.org/v2/everything?q={}&from=2022-04-30&language=en&sortBy=publishedAt&apiKey={}'.format(query,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results


#processing results
def process_results(article_list):
    articles_results = []
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
            article_object = Article(source, author, title, description, url, urlToImage, publishedAt,content)
            articles_results.append(article_object)

        return articles_results            