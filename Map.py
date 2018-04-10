from Cube import Cube

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
