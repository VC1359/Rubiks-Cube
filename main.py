# import pygame
# import sys
# from pygame.locals import*
# from OpenGL.GLU import*
# from OpenGL.GL import*
#
# vertex_path = "/Users/cposada/Desktop/Terminal/Rubiks_Cube/Cube_Model/vertices.txt"
# face_path = "/Users/cposada/Desktop/Terminal/Rubiks_Cube/Cube_Model/faces.txt"
#
# paints = [
# (253,254,255), #white
# (206,221,48), #yellow
# (195,2,3), #red
# (255,97,14), #orange
# (43,198,0), #green
# (0,80,173), #blue
# ]
#
# def get_list(txtname):
#     listname = []
#     with open(txtname) as f:
#         for line in f:
#             line = line.rstrip(",\r\n").replace("(",'').replace(")","").replace(" ",'')
#             row = list(line.split(","))
#             listname.append(row)
#         listname = [[float(j) for j in i] for i in listname]
#         return listname
#
# modelVerts = get_list(vertex_path)
# modelFaces = get_list(face_path)
#
# def drawfaces():
#     glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT) #clears each frame
#     glClear(GL_TRIANGLES) #drawing method
#     for eachface in (modelFaces):
#         for eachvert in eachface:
#             glColor3fv(paints[0]) #?
#             glColor3fv(modelVerts[int(eachvert)])
#         glEnd()
#
# def main():
#     pygame.init()
#     display = (1000, 1000) #window
#     pygame.display.set_caption("Rubik's CFOP")
#     FPS = pygame.time.Clock() #fps sync
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     gluPerspective(45,1,.1,50)
#     glTranslate(0,-1,-5) #xyz
#     glRotate(0,1,0,0)
#
#     Left = False
#     Right = False
#
#     def moveOBJ():
#         if Left:
#             glRotate(-1,0,1,0)
#         if Right:
#             glRotate(1,0,1,0)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#                 if event.key == K_a:
#                     Left = True
#                 if event.key == K_d:
#                     Right = True
#             if event.type == KEYUP:
#                 if event.key == K_a:
#                     Left = False
#                 if event.key == K_d:
#                     Right = False
#         pygame.display.flip()
#         drawfaces()
#         moveOBJ()
#         FPS.tick(60)
# main()




### GPT CODE
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import OBJ

# Initialize Pygame and create a window
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Load the model
cube = OBJ("Cube_Model\Rubiks_Model.obj")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)  # Rotate the model for demonstration purposes
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the model
    cube.draw()

    pygame.display.flip()
    pygame.time.wait(10)