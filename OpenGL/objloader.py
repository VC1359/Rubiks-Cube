from OpenGL.GL import *
import os

class OBJ:
    def __init__(self, filename):
        self.vertices = []
        self.faces = []
        self.colors = []
        self.materials = {}

        self.load(filename)

    def load(self, filename):
        path = os.path.dirname(filename)
        with open(filename, 'r') as file:
            material = None
            for line in file:
                if line.startswith('v '):
                    parts = line.strip().split()
                    vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                    self.vertices.append(vertex)
                elif line.startswith('f '):
                    parts = line.strip().split()
                    face = [int(parts[1].split('/')[0]), int(parts[2].split('/')[0]), int(parts[3].split('/')[0])]
                    self.faces.append((face, material))
                elif line.startswith('usemtl '):
                    material = line.split()[1]
                elif line.startswith('mtllib '):
                    self.load_mtl(os.path.join(path, line.split()[1]))

    def load_mtl(self, filename):
        with open(filename, 'r') as file:
            material = None
            for line in file:
                if line.startswith('newmtl '):
                    material = line.split()[1]
                    self.materials[material] = {'Kd': [1, 1, 1]}  # Default to white
                elif line.startswith('Kd ') and material:
                    parts = line.strip().split()
                    self.materials[material]['Kd'] = [float(parts[1]), float(parts[2]), float(parts[3])]

    def draw(self):
        for face, material in self.faces:
            if material and material in self.materials:
                glColor3fv(self.materials[material]['Kd'])
            else:
                glColor3f(0, 0, 0)  # Default to white if no material
            glBegin(GL_TRIANGLES)
            for vertex in face:
                glVertex3fv(self.vertices[vertex - 1])
            glEnd()
