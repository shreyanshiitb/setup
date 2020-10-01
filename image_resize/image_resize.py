# Python script to resize an image
from PIL import Image

img = Image.open('gen-kenobi.jpg')
new_image = img.resize((100, 100))
new_image.save('new-kenobi.jpg')
