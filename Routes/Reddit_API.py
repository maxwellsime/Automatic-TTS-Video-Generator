import requests

reddit_url = 'https://www.reddit.com'

def get_top_posts(subreddit):
    return requests.get('%s/r/%s/top/.json'%reddit_url%subreddit)
