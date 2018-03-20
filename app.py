#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter

width = 1280
height = 720

class Camera:
    x = 0
    y = 0
    z = -5

camera = Camera()
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=width, height=height, background='white')

points = [
    (-1, -1, -1),
    (-1, 1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, -1, 1),
    (1, 1, 1)
]

faces = [
    [0, 1, 2],
    [1, 2, 3],
    [4, 5, 6],
    [5, 6, 7]
]

def render():
    canvas.delete('all')

    for face in faces:

        coords = [];

        for pointId in face:

            (x, y, z) = points[pointId]

            x -= camera.x
            y -= camera.y
            z -= camera.z

            f = (height / 2) / z

            x = x * f + (width / 2)
            y = y * f + (height / 2)
            coords.append((x, y))

        print(coords)

        for i in range(len(coords)):

            if i + 1 < len(coords):
                canvas.create_line(coords[i] + coords[i + 1])
            else:
                canvas.create_line(coords[i] + coords[0])


render();


canvas.pack()

window.mainloop()