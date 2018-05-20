from Cube import Cube
from Pyramid import Pyramid

class Map:

    def __init__(self):
        self.objects = []

        for i in range(3):
            for j in range(3):
                for k in range(2):
                    self.objects.append(Pyramid(i, j , k, 1))
        self.results = []

    def render(self):

        if len(self.results) > 0:
            return self.results

        faces = []
        for i in self.objects:
            faces += i.render()

        # little hack to remove duplicate faces (~20% performance improvement)
        faces = [tuple(face) for face in faces]
        faces = list(set(faces))
        faces = [list(face) for face in faces]

        self.results = faces
        return faces
