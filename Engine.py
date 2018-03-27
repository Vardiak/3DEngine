#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter
import msvcrt
import time
import threading
import math

class Camera:
    x = 0
    y = 2
    z = -5
    zPressed = False
    qPressed = False
    sPressed = False
    dPressed = False

class Engine:

    def __init__(self, width, height, FPS):
        self.width = width
        self.height = height
        self.targetFPS = FPS
        self.cam = Camera()

        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=width, height=height, background='white')
        self.canvas.bind("<KeyPress>", self.onKeyPress)
        self.canvas.bind("<KeyRelease>", self.onKeyRelease)

        self.canvas.pack()
        self.canvas.focus_set()

        self.map = Map()
        
        self.mainloop()

    def mainloop(self):

        cycleStart = time.clock()
        fps = self.targetFPS
        frameCount = 0

        while True:
            
            start = time.clock()

            # Display frames
            self.root.update()

            # Render next frame
            self.render()
            self.canvas.create_text(10, 10, anchor=tkinter.NW, font="Roboto\ Mono 20", text=str(fps) + " FPS")

            # Next frame planification for stable refresh rate
            renderingTime = time.clock() - start
            nextFrame = (1 / self.targetFPS) - renderingTime
            if (nextFrame > 0): time.sleep(nextFrame)

            #Update refresh counter
            frameCount += 1
            if (frameCount == self.targetFPS):
                frameCount = 0
                fps = self.targetFPS / (time.clock() - cycleStart)
                cycleStart = time.clock()


    def render(self):
        self.canvas.delete('all')

        if (self.cam.zPressed):
            self.cam.z += 0.05

        if (self.cam.qPressed):
            self.cam.x -= 0.05

        if (self.cam.sPressed):
            self.cam.z -= 0.05

        if (self.cam.dPressed):
            self.cam.x += 0.05


        for face in self.map.render():

            coords = []

            for (x, y, z) in face:

                # (x, y, z) = self.points[pointId]

                # Camera position
                x -= self.cam.x
                y -= self.cam.y
                z -= self.cam.z


                # Projection
                f = (self.width / 2) / (z + 0.01)

                x = x * f + (self.width / 2)
                y = - y * f + (self.height / 2)
                coords.append((x, y))

            # print(coords)

            for i in range(len(coords)):

                if i + 1 < len(coords):
                    self.canvas.create_line(coords[i] + coords[i + 1])
                else:
                    self.canvas.create_line(coords[i] + coords[0])

    def onKeyPress(self, e):
        print('coucou', e.keycode)

        if (e.keycode == 90):
            self.cam.zPressed = True
        elif (e.keycode == 81):
            self.cam.qPressed = True
        elif (e.keycode == 83):
            self.cam.sPressed = True
        elif (e.keycode == 68):
            self.cam.dPressed = True
        elif (e.keycode == 32):
            self.cam.y += 1
        elif (e.keycode == 16):
            self.cam.y -= 1

    def onKeyRelease(self, e):
        print('release', e.keycode)

        if (e.keycode == 90):
            self.cam.zPressed = False
        elif (e.keycode == 81):
            self.cam.qPressed = False
        elif (e.keycode == 83):
            self.cam.sPressed = False
        elif (e.keycode == 68):
            self.cam.dPressed = False




class Map:

    def __init__(self):
        self.objects = []

        for i in range(10):
            for j in range(10):
                for k in range(1):
                    self.objects.append(Cube(i, j , k, 1))
        self.results = []

    def render(self):
        if self.results:
            return self.results

        faces = []
        for i in self.objects:
            faces += i.render()

        self.results = faces
        return faces


class Cube:

    def __init__(self, x, y, z, size):
        self.pos = (x, y, z)
        self.size = size

    def render(self):
        (x, y, z) = self.pos
        points = [
            (x, y, z),
            (x, y, z + self.size),
            (x, y + self.size, z),
            (x, y + self.size, z + self.size),
            (x + self.size, y, z),
            (x + self.size, y, z + self.size),
            (x + self.size, y + self.size, z),
            (x + self.size, y + self.size, z + self.size),
        ]

        return [
            [points[0], points[1], points[3], points[2]],
            [points[4], points[5], points[7], points[6]],
            [points[3], points[7], points[5], points[1]],
            [points[0], points[2], points[6], points[4]]
        ]