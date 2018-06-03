#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

'''
Function that rotate a 2D point around (0, 0) 
'''
def rotate2D(x, y, rad):
    s = math.sin(rad)
    c = math.cos(rad)

    return (
        (x * c) - (y * s),
        (y * c) + (x * s)
    )


'''
Function that returns the average distance of a face from (0, 0, 0)
'''
def calculateDepth(face):

    if len(face) == 0:
        return 0

    total = 0

    for (x, y, z) in face:
        total += math.sqrt(x**2+y**2+z**2)
    
    return - total / len(face)


'''
Function clip all points with z < 0
'''
def clip(face):

    out = -1
    enter = -1

    #Find the enter and the exit point
    for i in range(len(face)):
        (x, y, z) = face[i]
        (xa, ya, za) = face[(i - 1) % len(face)]
        (xb, yb, zb) = face[(i + 1) % len(face)]

        if z < 0.01:
            if za >= 0.01:
                out = i

            if zb >= 0.01:
                enter = i
    
    if out > -1 and enter > -1:
        
        #Calculate intersections points before and after.
        (xa, ya, za) = face[(out - 1) % len(face)]
        (xb, yb, zb) = face[out]

        za += 0.01
        zb += 0.01

        a = (
            xa - ((za * (xb - xa)) / (zb - za)),
            ya - ((za * (yb - ya)) / (zb - za)),
            0.01
        )

        (xa, ya, za) = face[(enter + 1) % len(face)]
        (xb, yb, zb) = face[enter]

        za += 0.01
        zb += 0.01

        b = (
            xa - ((za * (xb - xa)) / (zb - za)),
            ya - ((za * (yb - ya)) / (zb - za)),
            0.01
        )

        #Reconstruct face with order
        new = [a, b]
        i = enter
        while (True):
            i = (i + 1) % len(face)
            if i == out:
                break
            else:
                new.append(face[i])

        return new
    else:
        if face[0][2] > 0.01:
            return face
        else:
            return []
                

