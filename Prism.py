from OpenGL.GL import *

class Prism:
    def __init__(self):
        self.vertices = (
            (-1, -1, -1),  
            (1, -1, -1),   
            (0, 1, -1),    
            (-1, -1, 1),   
            (1, -1, 1),    
            (0, 1, 1)      
        )

        self.edges = (
            (0, 1), (1, 2), (2, 0), 
            (3, 4), (4, 5), (5, 3),  
            (0, 3), (1, 4), (2, 5)  
        )

    def draw(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()