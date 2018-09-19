import numpy as np


def median(image, size=(5, 5)):

    i_height, i_width = image.shape[0], image.shape[1]
    k_width, k_height = size[0], size[1]

    filtered = np.zeros_like(image)

    for y in range(i_height):
        for x in range(i_width):
            weighted_pixel = []

            for ky in range(-(k_height / 2), k_height - 1):
                for kx in range(-(k_width / 2), k_width - 1):
                    pixel = 0
                    pixel_y = y - ky
                    pixel_x = x - kx

                    if (pixel_y >= 0) and (pixel_y < i_height) and (pixel_x >= 0) and (pixel_x < i_width):
                        pixel = image[pixel_y, pixel_x]

                    # weigh the pixel value and sum
                    weighted_pixel.append(pixel)

            # finally, the pixel at location (x,y) is the sum of the weighed neighborhood
            filtered[y, x] = np.median(weighted_pixel)
    return filtered
