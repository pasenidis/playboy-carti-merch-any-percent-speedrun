from PIL import Image, ImageDraw, ImageFont
a=Image.open('a.jpg')
b=Image.open('b.jpg').resize((450, 500))

a.paste(b, (265, 200))
draw = ImageDraw.Draw(a)
draw.text((250, 150), 'RAF SIMONS x ASAP Mob', font=ImageFont.truetype("arial.ttf", 45))
draw.text((470, 250), 'X', font=ImageFont.truetype("arial.ttf", 65))

a.save('c.jpg')
