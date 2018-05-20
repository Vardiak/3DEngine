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

def clip(face):
    
    new = []

    # Find start of exit
    out = -1
    for i in range(len(face)):
        (x, y, z) = face[i]

        if z < 0 and (i != 0 or face[len(face) - 1][2] >= 0):
            out = i
            break

    # If there is a point out, find the enter point
    if out != -1:
        enter = -1

        for i in list(range(out, len(face))) + list(range(0, out)):
            if (face[(i + 1) % len(face)][2] > 0):
                enter = i
                break

        # If there is no point in, start clipping
        if enter != -1:

            #Calculate intersections points before and after.
            (xa, ya, za) = face[(out - 1) % len(face)]
            (xb, yb, zb) = face[out]


            a = (
                xa - za * (xb - xa) / (zb - za),
                ya - za * (yb - ya) / (zb - za),
                0.01
            )

            (xa, ya, za) = face[(enter + 1) % len(face)]
            (xb, yb, zb) = face[enter]

            b = (
                xa - za * (xb - xa) / (zb - za),
                ya - za * (yb - ya) / (zb - za),
                0.01
            )

            #Reconstruct face with order
            i = (enter + 1) % len(face)
            while (True):
                new.append(face[i])
                i = (i + 1) % len(face)
                if i == out:
                    break
            new += [a, b]

            return new
        else:
            return []
    else:
        return face
                

