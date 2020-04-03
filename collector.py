import praw
import reddit_creds
import urllib.request
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

reddit = praw.Reddit(client_id=reddit_creds.client_id,
                     client_secret=reddit_creds.client_secret,
                     password=reddit_creds.password,
                     user_agent=reddit_creds.user_agent,
                     username=reddit_creds.username)

subreddit = reddit.subreddit('art').top('month')

def watermarkPhoto(fileName):
    img = Image.open(outfile)
    size = int(img.height / 44)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r'C:\Users\jdeek\PycharmProjects\Datascience\sudoArt\Assets\constan', size)
    draw.rectangle([(0, 0), (int(len(item_dict['artist']) * .7 * size), size)], fill=(0, 0, 0))
    draw.text((0, 0), "u/" + item_dict["artist"], (255, 255, 255), font=font)
    img.save(outfile)

for item in subreddit:
    item_dict = {'artist':item.author.name,
        'original':item.is_self,
        'title':item.title,
        'link': item.url,
        'score': item.score
        }

    item_dict['name'] = item_dict['title'].split(",")[0]
    item_dict['year'] = item_dict['title'].split(",")[-1]
    filetype = item_dict['link'].split(".")[-1]

    if int(item_dict['score']) >= 10000:
        filename= "".join("".join((item_dict['name']+","+item_dict['year']).split('.')).split('"'))
        outfile = r"C:\Users\jdeek\PycharmProjects\Datascience\sudoArt\Redditors Art\""[:-1]+filename+"."+filetype
        print(outfile)
        try:
            file = urllib.request.urlretrieve(item_dict['link'],outfile)
            if filetype == "gif":
                watermarkGIF()
            else:
                watermarkPhoto(outfile)

        except FileNotFoundError:
            print("invalid URL")