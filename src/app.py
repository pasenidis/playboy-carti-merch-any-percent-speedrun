from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('hoodie.jpg')
im2 = Image.open('logo.jpg')
im2 = im2.resize((450, 500))

im1.paste(im2, (265, 200))
im1.save('res.jpg', quality=95)