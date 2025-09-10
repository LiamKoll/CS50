# system commands
import sys

# loading library
from PIL import Image

# list to save images in creating process
images = []

#opening pictures in file
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# saving gif in right format and with all pictures
images[0].save(
    "gif1.gif", save_all=True, append_images=[images[1],images[2],images[3],images[4],images[5],images[6]], duration=200, loop =0
)

#source Harvard CS50 David Malan (changed)