import praw
from prawcore import exceptions
from Collector import reddit_creds
from Collector import iterator
from urllib import error

def retrieve(sub):
    reddit = praw.Reddit(client_id=reddit_creds.client_id,
                         client_secret=reddit_creds.client_secret,
                         password=reddit_creds.password,
                         user_agent=reddit_creds.user_agent,
                         username=reddit_creds.username)

    print(sub)

    try:
        subreddit = reddit.subreddit(sub).top('week')
        iterator.iterateSubmissions(subreddit)
    except (exceptions.BadRequest,exceptions.Redirect, AttributeError, error.HTTPError):
        print('invalid reddit')






