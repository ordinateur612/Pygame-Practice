from PIL import Image

img1 = Image.open('image1.jpg')
img2 = Image.open('image2.jpg')

r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()

new_image = Image.merge("RGB", (r2, g1, b2))

new_image.show()
new_image.save('new_image.jpg')