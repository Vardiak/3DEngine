import math

def rotate2D(x, y, rad):
    s = math.sin(rad)
    c = math.cos(rad)

    return (
        (x * c) - (y * s),
        (y * c) + (x * s)
    )

def calculateDepth(face):

    if len(face) == 0:
        return 0

    total = 0

    for (x, y, z) in face:
        total += math.sqrt(x**2+y**2+z**2)
    
    return - total / len(face)