from Automatic_TTS_Video_Generator.Routes.Reddit_API import get_top_posts

def get_top_greentext_posts():
    posts = get_top_posts('greentext')
    