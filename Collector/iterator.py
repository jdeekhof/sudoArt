import urllib.request
from Collector import formatter
from Collector import watermarks

def iterateSubmissions(subreddit):
    for item in subreddit:
        item_dict = {'artist': item.author.name,
                     'original': item.is_self,
                     'title': item.title,
                     'link': item.url,
                     'score': item.score
                     }

        if int(item_dict['score']) >= 5000:
            if item.subreddit == 'art':
                (item_dict, filetype, outfile) = formatter.r_artFormatting(item_dict)
            else:
                (item_dict, filetype, outfile) = formatter.generalFormatting(item_dict)

            print(outfile)
            try:
                if filetype == "gif":
                    file = urllib.request.urlretrieve(item_dict['link'], outfile)
                    watermarks.watermarkGIF(item_dict, outfile)
                elif filetype == "jpg":
                    file = urllib.request.urlretrieve(item_dict['link'], outfile)
                    watermarks.watermarkPhoto(item_dict, outfile)
                elif filetype == "png":
                    file = urllib.request.urlretrieve(item_dict['link'], outfile)
                    watermarks.watermarkPhoto(item_dict, outfile)
                else:
                    print("invalid file type: " + filetype)

            except(FileNotFoundError, SystemError):
                print("Invalid URL")

