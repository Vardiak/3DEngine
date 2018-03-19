#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 

width = 500
height = 500

class Camera:
    x = 0
    y = 0
    z = -5

camera = Camera()
window = Tk()
canvas = Canvas(window, width=width, height=height, background='white')

points = [
    [-1, -1, -1],
    [-1, 1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, -1, 1],
    [1, 1, 1]
]

faces = [
    [0, 1, 2],
    [1, 2, 3],
    [4, 5, 6],
    [5, 6, 7]
]

for face in faces:

    coords = [];

    for pointId in face:

        point = points[pointId]

        x = point[0] - camera.x
        y = point[1] - camera.y
        z = point[2] - camera.z

        f = (width / 2) / z

        x = x * f + (width / 2)
        y = y * f + (width / 2)
        coords.append((x, y))

    print(coords)
    
    canvas.create_line(coords[0] + coords[1])
    canvas.create_line(coords[1] + coords[2])
    canvas.create_line(coords[2] + coords[0])


canvas.pack()

window.mainloop()