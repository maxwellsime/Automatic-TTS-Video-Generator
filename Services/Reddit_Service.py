import sys
sys.path.append('.')
from Routes.Reddit_API import reddit_api

def get_top_greentext_posts():
    api = reddit_api()
    posts = api.get_top_posts('greentext')
    print(posts.text)
    