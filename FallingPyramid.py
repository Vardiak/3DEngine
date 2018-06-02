
from Camera import cam

'''
Pyramid model with some gravity stuff
'''

class FallingPyramid:

    def __init__(self, x, y, z, size, color):
        self.pos = (x, y, z)
        self.size = size
        self.color = color

    def render(self):
        (x, y, z) = self.pos

        g = 20
        t = cam.frameCount / 60 - 5

        if t > 0:
            y = - g * (t**2) / 2 + y

        if y < 0:
            y = 0

        points = [
            (x, y, z),
            (x, y, z + self.size),
            (x + (self.size / 2), y + self.size, z + (self.size / 2)),
            (x + self.size, y, z),
            (x + self.size, y, z + self.size)
        ]

        faces = [
            [points[0], points[1], points[2]],
            [points[3], points[4], points[2]],
            [points[1], points[4], points[3], points[0]],
            [points[0], points[2], points[3]],
            [points[2], points[4], points[1]], 
        ]

        colors = [self.color for i in range(5)]

        return (faces, colors)
