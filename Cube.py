#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Cube model
'''

class Cube:

    def __init__(self, x, y, z, size, color):
        self.pos = (x, y, z)
        self.size = size
        self.color = color

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

        faces = [
            [points[2], points[3], points[7], points[6]],
            [points[0], points[1], points[5], points[4]],
            [points[0], points[1], points[3], points[2]],
            [points[4], points[5], points[7], points[6]],
            [points[3], points[7], points[5], points[1]],
            [points[0], points[2], points[6], points[4]]
        ]

        colors = [self.color for i in range(6)]

        return (faces, colors)