#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter
import msvcrt
import time
import threading
import math
import utils
from Map import Map
from Camera import Camera


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

            # Update refresh counter
            frameCount += 1
            if (frameCount == self.targetFPS):
                frameCount = 0
                fps = round(self.targetFPS / (time.clock() - cycleStart), 2)
                cycleStart = time.clock()


    def render(self):
        self.canvas.delete('all')
        # self.canvas.

        # Handle keyboard input
        if (self.cam.zPressed):
            self.cam.z += 0.05 * math.cos(self.cam.yaw)
            self.cam.x += 0.05 * math.sin(self.cam.yaw)
            # Uncomment for 3D orientation
            # self.cam.z += 0.05 * math.cos(self.cam.yaw) * math.cos(self.cam.pitch)
            # self.cam.x += 0.05 * math.sin(self.cam.yaw) * math.cos(self.cam.pitch)
            # self.cam.y += 0.05 * math.sin(self.cam.pitch)

        if (self.cam.qPressed):
            self.cam.x -= 0.05 * math.cos(self.cam.yaw)
            self.cam.z += 0.05 * math.sin(self.cam.yaw)

        if (self.cam.sPressed):
            self.cam.z -= 0.05 * math.cos(self.cam.yaw)
            self.cam.x -= 0.05 * math.sin(self.cam.yaw)

        if (self.cam.dPressed):
            self.cam.x += 0.05 * math.cos(self.cam.yaw)
            self.cam.z -= 0.05 * math.sin(self.cam.yaw)

        if (self.cam.upPressed):
            self.cam.pitch += 0.015
        if (self.cam.downPressed):
            self.cam.pitch -= 0.015
        if (self.cam.leftPressed):
            self.cam.yaw -= 0.015
        if (self.cam.rightPressed):
            self.cam.yaw += 0.015


        faces = self.map.render()

        for i in range(len(faces)):

            face = []

            for (x, y, z) in faces[i]:

                # (x, y, z) = self.points[pointId]

                # Camera position
                x -= self.cam.x
                y -= self.cam.y
                z -= self.cam.z

                # Camera rotation
                (x, z) = utils.rotate2D(x, z, self.cam.yaw)
                (y, z) = utils.rotate2D(y, z, self.cam.pitch)

                if z > 0:
                    face.append((x, y, z))

            faces[i] = face

        order = sorted(range(len(faces)), key=lambda i: utils.calculateDepth(faces[i]))

        for i in order:
            polygon = []

            for (x, y, z) in faces[i]:
                # Projection
                f = (self.width / 2) / z

                x = x * f + (self.width / 2)
                y = - y * f + (self.height / 2)
                polygon += [x, y]

            if len(polygon) > 0:
                self.canvas.create_polygon(polygon, outline='white', fill='black')

    def onKeyPress(self, e):

        if (e.keycode == 90):
            self.cam.zPressed = True
        elif (e.keycode == 81):
            self.cam.qPressed = True
        elif (e.keycode == 83):
            self.cam.sPressed = True
        elif (e.keycode == 68):
            self.cam.dPressed = True
        elif (e.keycode == 38):
            self.cam.upPressed = True
        elif (e.keycode == 40):
            self.cam.downPressed = True
        elif (e.keycode == 37):
            self.cam.leftPressed = True
        elif (e.keycode == 39):
            self.cam.rightPressed = True

        elif (e.keycode == 32):
            self.cam.y += .3
        elif (e.keycode == 16):
            self.cam.y -= .3

    def onKeyRelease(self, e):

        if (e.keycode == 90):
            self.cam.zPressed = False
        elif (e.keycode == 81):
            self.cam.qPressed = False
        elif (e.keycode == 83):
            self.cam.sPressed = False
        elif (e.keycode == 68):
            self.cam.dPressed = False
        elif (e.keycode == 38):
            self.cam.upPressed = False
        elif (e.keycode == 40):
            self.cam.downPressed = False
        elif (e.keycode == 37):
            self.cam.leftPressed = False
        elif (e.keycode == 39):
            self.cam.rightPressed = False