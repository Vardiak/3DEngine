from Cube import Cube
from Pyramid import Pyramid
from Floor imoprt Floor 
from Slope import Slope
from Stairs import Stairs

class Map:

    def __init__(self):
        self.objects = []

        # for i in range(3):
        #     for j in range(3):
        #         for k in range(2):
        #             self.objects.append(Pyramid(i, j , k, 1))
        for i in range(-5, 5):
            for j in range(-5, 5):
                self.objects.append(Floor(i, 0, j, 1))
        # self.objects.append(Pyramid(0, 0, 0, 20))²
        self.objects.append(Cube(0, 0, 0, 1))
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
