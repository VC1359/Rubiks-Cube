import os
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import OBJ

# Initialize Pygame and create a window
pygame.init()
display = (800, 600)
pygame.display.set_caption("Rubik's CFOP")
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, 1, .1, 50)
glTranslatef(0,0,-5) #Not sure why this needs to be here

# Load the model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "Cube_Model", "Rubiks_Model.obj")
cube = OBJ(model_path)

def init_opengl():
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for correct Z-ordering
    glEnable(GL_CULL_FACE)   # Enable face culling for performance
    glCullFace(GL_BACK)      # Cull back faces
init_opengl()


# Control variables
camera_rot = [0, 0]
dragging = False
last_mouse_pos = [0, 0]

def handle_camera_dragging(): #ugly motion
    global camera_rot, dragging, last_mouse_pos
    if dragging:
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - last_mouse_pos[0]
        dy = mouse_pos[1] - last_mouse_pos[1]
        camera_rot[0] += dy * .08
        camera_rot[1] += dx * .08
        last_mouse_pos = mouse_pos


Left = False
Right = False
Up = False
Down = False

def moveOBJ():
    if Left:
        glRotate(2,0,2,0)
    if Right:
        glRotate(-2,0,2,0)
    if Up:
        glRotate(2,2,0,0)
    if Down:
        glRotate(-2,2,0,0)


while True:

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_a:
                Left = True
            if event.key == K_d:
                Right = True
            if event.key == K_w:
                Up = True
            if event.key == K_s:
                Down = True
        if event.type == KEYUP:
            if event.key == K_a:
                Left = False
            if event.key == K_d:
                Right = False
            if event.key == K_w:
                Up = False
            if event.key == K_s:
                Down = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                dragging = True
                last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                dragging = False
                camera_rot = [0, 0]
        elif event.type == MOUSEMOTION:
            if dragging:
                handle_camera_dragging()

#dont know what these are doing here
    # glLoadIdentity()
    # glTranslatef(0.0, 0.0, -5)

    glRotatef(camera_rot[0], 1, 0, 0)
    glRotatef(camera_rot[1], 0, 1, 0)

    moveOBJ()
    cube.draw()
    pygame.display.flip()
    pygame.time.wait(10)
