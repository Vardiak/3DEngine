import math

def rotate2D(x, y, rad):
    s = math.sin(rad)
    c = math.cos(rad)

    return (
        (x * c) - (y * s),
        (y * c) + (x * s)
    )