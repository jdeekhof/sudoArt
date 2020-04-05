from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageSequence
from io import BytesIO


def watermarkPhoto(item_dict, fileName):
    img = Image.open(fileName)
    size = int(img.height / 44)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r'C:\Users\jdeek\PycharmProjects\Datascience\sudoArt\Assets\constan', size)
    draw.rectangle([(0, 0), (int(len(item_dict['artist']) * .7 * size), size)], fill=(0, 0, 0))
    draw.text((0, 0), "u/" + item_dict["artist"], (255, 255, 255), font=font)
    img.save(fileName)


def watermarkGIF(item_dict, fileName):
    img = Image.open(fileName)
    frames = []
    for frame in ImageSequence.Iterator(img):
        frame = frame.convert('RGB')
        draw = ImageDraw.Draw(frame)
        size = int(img.height / 44)
        font = ImageFont.truetype(r'C:\Users\jdeek\PycharmProjects\Datascience\sudoArt\Assets\constan', size)
        draw.rectangle([(0, 0), (int(len(item_dict['artist']) * .7 * size), size)], fill=(0, 0, 0))
        draw.text((0, 0), "u/" + item_dict["artist"], (255, 255, 255), font=font)
        del draw
        b = BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)
    frames[0].save(fileName, save_all=True, append_images=frames[0:])
