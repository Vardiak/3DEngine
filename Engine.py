#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter
import time
import math
import utils

from Map import Map
from Camera import cam

'''
Main class, used to instanciate a window.
'''

class Engine:

    def __init__(self, width, height, FPS):
        self.width = width
        self.height = height
        self.targetFPS = FPS

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

        while True:
            
            start = time.clock()

            # Display frames
            self.root.update()

            #Calculate movement
            self.updatePosition()

            # Render next frame
            self.render()
            self.canvas.create_text(10, 10, anchor=tkinter.NW, font="Roboto\ Mono 20", text=str(fps) + " FPS")

            # Next frame planification for stable refresh rate
            renderingTime = time.clock() - start
            nextFrame = (1 / self.targetFPS) - renderingTime
            if (nextFrame > 0): time.sleep(nextFrame)

            # Update refresh counter
            cam.frameCount += 1
            if (cam.frameCount % self.targetFPS == 0):
                fps = round(self.targetFPS / (time.clock() - cycleStart), 2)
                cycleStart = time.clock()


    def render(self):
        self.canvas.delete('all')

        (faces, colors) = self.map.render()
        faces, colors = list(faces), list(colors)

        for i in range(len(faces)):

            face = []

            for (x, y, z) in faces[i]:

                # Camera position
                x -= cam.x
                y -= cam.y
                z -= cam.z

                # Camera rotation
                (x, z) = utils.rotate2D(x, z, cam.yaw)
                (y, z) = utils.rotate2D(y, z, cam.pitch)

                face.append((x, y, z))

            faces[i] = face

        #Face clipping
        faces = [utils.clip(face) for face in faces]

        #Face sorting
        order = sorted(range(len(faces)), key=lambda i: utils.calculateDepth(faces[i]))

        #Face display
        for i in order:
            face = faces[i]

            if len(face) > 0:
                polygon = []

                for (x, y, z) in face:
                    # Projection
                    f = (self.width / 2) / z

                    x = x * f + (self.width / 2)
                    y = - y * f + (self.height / 2)
                    polygon += [x, y]
                    

                # de = ("%02x"%random.randint(0,255))
                # re = ("%02x"%random.randint(0,255))
                # we = ("%02x"%random.randint(0,255))
                # color= "#" + de + re + we
                self.canvas.create_polygon(polygon, outline='white', fill=colors[i])

    def onKeyPress(self, e):

        if (e.keycode == 90):
            cam.zPressed = True
        elif (e.keycode == 81):
            cam.qPressed = True
        elif (e.keycode == 83):
            cam.sPressed = True
        elif (e.keycode == 68):
            cam.dPressed = True
        elif (e.keycode == 38):
            cam.upPressed = True
        elif (e.keycode == 40):
            cam.downPressed = True
        elif (e.keycode == 37):
            cam.leftPressed = True
        elif (e.keycode == 39):
            cam.rightPressed = True

        elif (e.keycode == 32):
            cam.y += .3
        elif (e.keycode == 16):
            cam.y -= .3

    def onKeyRelease(self, e):

        if (e.keycode == 90):
            cam.zPressed = False
        elif (e.keycode == 81):
            cam.qPressed = False
        elif (e.keycode == 83):
            cam.sPressed = False
        elif (e.keycode == 68):
            cam.dPressed = False
        elif (e.keycode == 38):
            cam.upPressed = False
        elif (e.keycode == 40):
            cam.downPressed = False
        elif (e.keycode == 37):
            cam.leftPressed = False
        elif (e.keycode == 39):
            cam.rightPressed = False

    def updatePosition(self):
        # Handle keyboard input
        if (cam.zPressed):
            cam.z += 0.05 * math.cos(cam.yaw)
            cam.x += 0.05 * math.sin(cam.yaw)
            # Uncomment for 3D orientation
            # cam.z += 0.05 * math.cos(cam.yaw) * math.cos(cam.pitch)
            # cam.x += 0.05 * math.sin(cam.yaw) * math.cos(cam.pitch)
            # cam.y += 0.05 * math.sin(cam.pitch)

        if (cam.qPressed):
            cam.x -= 0.05 * math.cos(cam.yaw)
            cam.z += 0.05 * math.sin(cam.yaw)

        if (cam.sPressed):
            cam.z -= 0.05 * math.cos(cam.yaw)
            cam.x -= 0.05 * math.sin(cam.yaw)
            # Uncomment for 3D orientation
            # cam.z -= 0.05 * math.cos(cam.yaw) * math.cos(cam.pitch)
            # cam.x -= 0.05 * math.sin(cam.yaw) * math.cos(cam.pitch)
            # cam.y -= 0.05 * math.sin(cam.pitch)

        if (cam.dPressed):
            cam.x += 0.05 * math.cos(cam.yaw)
            cam.z -= 0.05 * math.sin(cam.yaw)

        if (cam.upPressed):
            cam.pitch += 0.015
        if (cam.downPressed):
            cam.pitch -= 0.015
        if (cam.leftPressed):
            cam.yaw -= 0.015
        if (cam.rightPressed):
            cam.yaw += 0.015