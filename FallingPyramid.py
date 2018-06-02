
'''
Pyramid model with some gravity stuff
'''

class FallingPyramid:

    def __init__(self, x, y, z, size, color):
        self.pos = (x, y, z)
        self.size = size
        self.color = color
        self.frameCount = 0

    def render(self):
        (x, y, z) = self.pos
        if y > 0 and self.frameCount > 600:
            y -= 30 * (self.frameCount - 600) / 60**2
        elif y < 0:
            y = 0
        self.frameCount += 1
        self.pos = (x, y, z)

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
