import sys
sys.path.append('.')
from Routes.Reddit_API import get_top_posts

def get_top_greentext_posts():
    posts = get_top_posts('greentext')
    print(posts.text)
    