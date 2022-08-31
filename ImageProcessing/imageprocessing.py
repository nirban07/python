from PIL import Image
import PIL as pp

im = Image.open("/Users/nirbanroy/Documents/Python/ImageProcessing/Images/LordTengen.jpeg")
print(help(pp))

print(im.format, im.size, im.mode)
im.thumbnail((48,48))
im.save("thmbnl.ppm")
im2 = Image.open("/Users/nirbanroy/Documents/Python/thmbnl.jpg")
print(im2.show())
