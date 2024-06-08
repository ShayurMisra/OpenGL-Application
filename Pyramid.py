from OpenGL.GL import *

class Pyramid:
    def __init__(self):
        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (0, 0, 1)
        )

        self.edges = (
            (0, 1), (0, 2), (0, 3),
            (1, 2), (1, 3), (2, 3),
            (4, 0), (4, 1), (4, 2), (4, 3)
        )

    def draw(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()