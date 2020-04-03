import praw
import reddit_creds
from PIL import Image

reddit = praw.Reddit(client_id=reddit_creds.client_id,
                     client_secret=reddit_creds.client_secret,
                     password=reddit_creds.password,
                     user_agent=reddit_creds.user_agent,
                     username=reddit_creds.username)

subreddit = reddit.subreddit('art').top('month')
for item in subreddit:
    item_dict = {'artist':item.author.name,
        'original':item.is_self,
        'title':item.title,
         'link': item.url,
          'score': item.score
        }
    if int(item_dict['score']) >= 10000:
        Image.save(item_dict['link'])


