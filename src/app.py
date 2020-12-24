from PIL import Image

im1 = Image.open('ho.jpg')
im2 = Image.open('logo.jpg')
area = (50, 20, 20, 20)  
im1.paste(im2, area)