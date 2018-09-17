import numpy as np
from skimage import img_as_float


def procImageUsingKernel(image, kernel, const=0):
    image = img_as_float(image)
    const = const / 255.

    i_height, i_width = image.shape[0], image.shape[1]
    k_width, k_height = kernel.shape[0], kernel.shape[1]

    filtered = np.zeros_like(image)

    for y in range(i_height):
        for x in range(i_width):
            weighted_pixel_sum = 0

            for ky in range(-k_height // 2 + 1, k_height // 2 + 1):
                for kx in range(-k_width // 2 + 1, k_width // 2 + 1):
                    pixel = 0
                    pixel_y = y - ky
                    pixel_x = x - kx

                    if (pixel_y >= 0) and (pixel_y < i_height) and (pixel_x >= 0) and (pixel_x < i_width):
                        pixel = image[pixel_y, pixel_x]

                    pos = (ky + k_height // 2, kx + k_width // 2)
                    weight = kernel[pos[1], pos[0]]

                    weighted_pixel_sum += pixel * weight

            weighted_pixel_sum += const

            filtered[y, x] = np.clip(weighted_pixel_sum, 0, 1)

    # dtype must unsigned int
    return (filtered * 255).astype('uint8')
