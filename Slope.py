class Slope:

    def __init__(self, x, y, z, size):
        self.pos = (x, y, z)
        self.size = size

    def render(self):
        (x, y, z) = self.pos
        points = [
            (x, y, z),
            (x, y, z + self.size),
            (x, y + self.size/2, z),
            (x, y + self.size, z + self.size),
            (x + self.size, y, z),
            (x + self.size, y, z + self.size),
            (x + self.size, y + self.size/2, z),
            (x + self.size, y + self.size, z + self.size),
        ]

        return [
            [points[2], points[3], points[7], points[6]],
            [points[0], points[1], points[5], points[4]],
            [points[0], points[1], points[3], points[2]],
            [points[4], points[5], points[7], points[6]],
            [points[3], points[7], points[5], points[1]],
            [points[0], points[2], points[6], points[4]]
        ]
