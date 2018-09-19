import numpy as np


def filter1(height=3, width=9):
    size = height * width
    k = np.zeros((width, height))
    for h in range(height):
        for w in range(width):
            if w == width // 2 and h == height // 2:
                v = size - 1
            else:
                v = -1
            k[w, h] = v
    print(k)
    return k


def filter2(height=9, width=3):
    size = height * width
    k = np.zeros((width, height))
    for h in range(height):
        for w in range(width):
            if w == width // 2 and h == height // 2:
                v = size
            else:
                v = -1
            k[w, h] = v
    print(k)
    return k
