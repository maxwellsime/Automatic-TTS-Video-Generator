import requests
import json

class reddit_api:
    
    reddit_url = 'https://www.reddit.com'

    def __init__(self):
        file = open('reddit_client_details.json')
        client_details = json.load(file)
        client_details['refresh_token'] = self.refresh_token(client_details['client_id'], client_details['client_secrets'])
        file.seek(0)
        json.dump(client_details, file, indent=4)
        file.close()

    def refresh_token(self, client_id, client_secret):
        client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        post_data = {'grant_type': 'password', 'username': 'reddit_bot', 'password': 'snoo'}
        headers = {'User-Agent': 'ChangeMeClient/0.1 by YourUsername'}
        response = requests.post('%s/api/v1/access_token'%self.reddit_url, auth=client_auth, data=post_data, headers=headers)
        response.json()

    def get_top_posts(self, subreddit):
        response = requests.get('%s/r/%s/top/.json'%(self.reddit_url, subreddit))

        if response.status_code != 200:
            raise Exception('Invalid response from API')
        else:
            return response
        
    def get_post_comments(self, subreddit, post_id):
        response = requests.get('%s/r/%s/comments/%s.json'%(self.reddit_url, subreddit, post_id))

        if response.status_code != 200:
            raise Exception('Invalid response from API')
        else:
            return response
        