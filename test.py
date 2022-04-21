from PIL import Image

import urllib.request


imgurl = 'https://i.scdn.co/image/ab67616d0000b273428d2255141c2119409a31b2'

imgname = imgurl.split('/')[-1] + ".png"

urllib.request.urlretrieve(imgurl, imgname)

image = Image.open(imgname)
