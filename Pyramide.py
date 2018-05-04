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
            (x + self.size, y, z),
            (x + self.size, y, z + self.size),
      
        ]

        return [
            [points[0], points[1], points[2]],
            [points[3], points[4], points[2]],
            [points[1], points[4], points[3], points[0]],
            [points[0], points[2], points[3]],
            [points[2], points[4], points[1]], 
        ]
