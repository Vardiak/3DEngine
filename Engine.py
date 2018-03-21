#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter
import msvcrt
import time
import threading
import math

class Camera:
    x = 0
    y = 0
    z = -5

class Engine:

    def __init__(self, width, height, FPS):
        self.width = width
        self.height = height
        self.targetFPS = FPS
        self.cam = Camera()

        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=width, height=height, background='white')

        self.lastFrame = time.clock()


        # temporary
        self.points = [
            (-1, -1, -1),
            (-1, 1, -1),
            (1, -1, -1),
            (1, 1, -1),
            (-1, -1, 1),
            (-1, 1, 1),
            (1, -1, 1),
            (1, 1, 1)
        ]

        self.faces = [
            [0, 1, 2],
            [1, 2, 3],
            [4, 5, 6],
            [5, 6, 7]
        ]
        
        self.mainloop()

    def mainloop(self):

        cycleStart = time.clock()
        fps = self.targetFPS
        frameCount = 0

        while True:
            
            start = time.clock()

            # Display frame
            self.root.update()

            # Render next frame
            self.render()
            self.canvas.create_text(10, 10, anchor=tkinter.NW, font="Roboto\ Mono 20", text=str(fps) + " FPS")
            self.canvas.pack()

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

        for face in self.faces:

            coords = [];

            for pointId in face:

                (x, y, z) = self.points[pointId]

                # Camera position
                x -= self.cam.x
                y -= self.cam.y
                z -= self.cam.z


                # Projection
                f = (self.height / 2) / z

                x = x * f + (self.width / 2)
                y = y * f + (self.height / 2)
                coords.append((x, y))

            # print(coords)

            for i in range(len(coords)):

                if i + 1 < len(coords):
                    self.canvas.create_line(coords[i] + coords[i + 1])
                else:
                    self.canvas.create_line(coords[i] + coords[0])