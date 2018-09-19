from skimage import img_as_float
from skimage.io import imread, imshow, show
import plot_img_and_hist
import numpy as np

img = imread('/home/avelts/Desktop/krsu/images/image_1.png')
# img.setflags(write=1)

img_float = img_as_float(img)

red = img_float[:, :, 0]
green = img_float[:, :, 1]
blue = img_float[:, :, 2]

# brightness
Y = 0.2126 * red + 0.7152 * green + 0.7222 * blue
# blue
U = -0.0999 * red - 0.3360 * green + 0.4360 * blue
# red
V = 0.6150 * red - 0.5586 * green - 0.0563 * blue

# will throw out 5% pixels - get 5% of pixels
tPix = round(Y.size * 0.05)
print tPix
cnt = 0
hist = Y.ravel()
for i in range(256):
    # print hist[i]
    if cnt > tPix:
        x_min = i
        break
# print x_min
# print Y.ravel()
R = Y + 1.2803 * V
G = Y - 0.2148 * U - 0.3805 * V
B = Y + 2.1279 * U
plot_img_and_hist(Y)
# imshow(np.clip(Y * 2, 0, 1))
imshow(img)
show()
