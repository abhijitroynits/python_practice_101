# Image processing demonstration -
# For this illustration, we will be using the following images :
# * afro.jpg
# * lady.jpg
# * 216.jpg
# * camera.jpg

from PIL import Image, ImageFilter


img = Image.open("afro.jpg")

print("Image dimensions: ", img.size)
print("Image file format: ", img.format)

# To open the image using your default OS app(for example: Photos.exe)
# PIL creates a temporary image file which would have
# a rather different file name and/or format(for example, .bmp)
img.show()


# Cropping an image
img2 = Image.open("camera.jpg")
print("img2.size=", img2.size)
area_to_crop = (300, 300, 600, 675)
cropped_image = img2.crop(area_to_crop)
cropped_image.show()


# Combining images together ;
# inserting the smaller image into the bigger image
img3 = Image.open("afro.jpg")
print('img3.size=', img3.size)
img4 = Image.open("216.jpg")
print('img4.size=', img4.size)
area_to_cover = (100, 100, 3877, 3877)

# syntax :>>>  bigger_image.paste(smaller_image, area_to_cover)
collated_image = Image.new('RGB', (img4.size[0], img4.size[1]), 0)
collated_image.paste(img4)
collated_image.paste(img3, area_to_cover)
collated_image.show()
img3.close()
img4.close()

# Getting individual channels ;
# Each pixel is composed of R, G, and B channels
img5 = Image.open("camera.jpg")
print('Image mode: ', img5.mode)
r, g, b = img5.split()

# Show all channels
r.show()
g.show()
b.show()

# Awesome merge effect
recreated_image = Image.merge("RGB", (r, g, b))
recreated_image.show()

# Another awesome effect
rec_image2 = Image.merge("RGB", (b, g, r))
rec_image2.show()

# Note : We can take two images of equal size
# Split their rgb, and swap their channels to get a different(often awesome) effect


# Basic Transformations
# Image to be used for this session :
# * couple.jpg

couple = Image.open("couple.jpg")
square_couple = couple.resize((250, 250))
flip_couple = couple.transpose(Image.FLIP_LEFT_RIGHT)
spin_couple = couple.transpose(Image.ROTATE_90)

couple.show()
square_couple.show()
flip_couple.show()
spin_couple.show()


# Modes and Filters
black_and_white_couple = couple.convert("L")
black_and_white_couple.show()

blurred_couple = couple.filter(ImageFilter.BLUR)
blurred_couple.show()

detail_couple = couple.filter(ImageFilter.DETAIL)
detail_couple.show()

edges_couple = couple.filter(ImageFilter.FIND_EDGES)
edges_couple.show()