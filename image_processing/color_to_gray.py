from skimage import img_as_float
from skimage.color import rgb2gray
from skimage.io import imread, imshow, show

img = imread('images/pathtoimage')
# img.setflags(write=1)

img_float = img_as_float(img)

red = img_float[:, :, 0]
green = img_float[:, :, 1]
blue = img_float[:, :, 2]

# rgb2gray result
imshow(rgb2gray(img))
show()

# average rgb result
imshow((red + green + blue) / 3)
show()

# close to real light and shadow
imshow((0.2126 * red + 0.7152 * green + 0.0722 * blue))
show()
