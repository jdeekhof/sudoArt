import praw
import reddit_creds

reddit = praw.Reddit(client_id=reddit_creds.client_id,
                     client_secret=reddit_creds.client_secret,
                     password=reddit_creds.password,
                     user_agent=reddit_creds.user_agent,
                     username=reddit_creds.username)

print(reddit.user.me())


