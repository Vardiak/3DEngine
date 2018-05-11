from Cube import Cube
from Pyramid import Pyramid

class Map:

    def __init__(self):
        self.objects = []

        for i in range(5):
            for j in range(5):
                for k in range(2):
                    self.objects.append(Pyramid(i, j , k, 1))
        self.results = []

    def render(self):

        faces = []
        for i in self.objects:
            faces += i.render()

        self.results = faces
        return faces
