from app import app




#Getting api key
api_key = app.config[NEWS_API_KEY]

#Getting news base url
base_url= app.config[NEWS_API_BASE_URL]
articles_api_url= app.config[NEWS_ARTICLES_API_URL]
source_articles_url= app.config[NEWS_SOURCE_ARTICLES_URL]