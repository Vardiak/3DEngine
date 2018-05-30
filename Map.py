from Cube import Cube
from Pyramid import Pyramid
from FallingPyramid import FallingPyramid
from Floor import Floor 
from Slope import Slope
from Stairs import Stairs

class Map:

    def __init__(self):
        self.objects = []

        self.faces = []
        self.colors = []

        for i in range(-5, 6):
            for j in range(-5, 5):
                self.objects.append(Floor(i, 0, j, 1, 'black'))

        self.objects.append(Cube(-3, 0, 0, 1, 'pink'))
        self.objects.append(Slope(-1, 0, 0, 1, 'purple'))
        self.objects.append(Stairs(1, 0, 0, 1, 'green'))
        self.objects.append(FallingPyramid(3, 20, 0, 1, 'red'))

    def render(self):

        # Need to be disabled if using falling objects
        # if len(self.faces) > 0:
        #     return (self.faces, self.colors)

        faces = []
        colors = []
        for obj in self.objects:
            (f, c) = obj.render()
            faces += f
            colors += c

        # # little hack to remove duplicate faces (~20% performance improvement)
        # faces = [tuple(face) for face in faces]
        # faces = list(set(faces))
        # faces = [list(face) for face in faces]

        self.faces = faces
        self.colors = colors
        return (faces, colors)
