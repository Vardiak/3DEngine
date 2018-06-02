'''
Simple floor model
'''

class Floor:

    def __init__(self, x, y, z, size, color):
        self.pos = (x, y, z)
        self.size = size
        self.color = color

    def render(self):
        (x, y, z) = self.pos

        points = [
            (x, y, z),
            (x + self.size, y, z),
            (x + self.size, y, z + self.size),
            (x, y, z + self.size)
        ]

        faces = [
            [points[0], points[1], points[2], points[3]],
        ]

        return (faces, [self.color])
