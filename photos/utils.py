from PIL import Image, ImageDraw, ImageFont, ImageOps

def get_orientation(width, height):
    if width > height:
        return "landscape"
    else:
        return "portrait"

def reduce_size(path):
    """ reduce size image """
    src_photo = Image.open(path)  
    photo = ImageOps.exif_transpose(src_photo)
    width, height = photo.size
    orientation = get_orientation(width, height)
    if orientation == 'landscape':
        photo.thumbnail((1280,720), Image.ANTIALIAS)
    else:           
        photo.thumbnail((720, 1280), Image.ANTIALIAS)
    photo.save(path, quality=95, optimize=True)

def add_watermark(path):
    """ add watermark to an image"""   
    watermark_txt = "www.influ.com" 
    font = ImageFont.truetype('arial.ttf', 38)
    
    src_photo = Image.open(path) 
    photo = ImageOps.exif_transpose(src_photo)
    width, height = photo.size
    
    draw = ImageDraw.Draw(photo)
    txt_w, txt_h = draw.textsize(watermark_txt, font)
    position = ((width - txt_w)/2,(height - txt_h)/2)
    draw.text(position, watermark_txt, font=font)

    photo.save(path)
