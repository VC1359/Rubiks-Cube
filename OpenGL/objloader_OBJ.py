from OpenGL.GL import *

class OBJ:
    def __init__(self, filename):
        self.vertices = []
        self.faces = []

        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    parts = line.strip().split()
                    vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                    self.vertices.append(vertex)
                elif line.startswith('f '):
                    parts = line.strip().split()
                    face = [int(parts[1].split('/')[0]), int(parts[2].split('/')[0]), int(parts[3].split('/')[0])]
                    self.faces.append(face)

    def draw(self):
        glBegin(GL_TRIANGLES)
        for face in self.faces:
            for vertex in face:
                glVertex3fv(self.vertices[vertex - 1])
        glEnd()
