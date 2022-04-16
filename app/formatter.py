import string

puncuationToRemove = "".join(string.punctuation.split("'"))
table = str.maketrans('', '', puncuationToRemove)

def r_artFormatting(item_dict):
    item_dict['name'] = item_dict['title'].split(",")[0]
    filetype = item_dict['link'].split(".")[-1]
    item_dict['name'] = "".join(w.translate(table) for w in item_dict['name'])
    filename = (item_dict['name'])
    outfile = r"C:\Users\jdeek\PycharmProjects\Datascience\sudoArt\Redditors Art\""[:-1] + filename + "." + filetype
    return ((item_dict, filetype, outfile))

def generalFormatting(item_dict):
    filetype = item_dict['link'].split(".")[-1]
    item_dict['title'] = "".join(w.translate(table) for w in item_dict['title'])
    filename = (item_dict['title'])
    outfile = r"C:\Users\jdeek\PycharmProjects\Datascience\sudoArt\Redditors Art\""[:-1] + filename + "." + filetype
    return ((item_dict, filetype, outfile))