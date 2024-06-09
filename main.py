import bpy
import math
import sys
import pathlib

#Lets us import from our files (not sure what it does, or if needed?)
path = pathlib.Path(bpy.data.filepath)
myProjects_dir = path.parent.resolve() 
myProjects_dir = str(myProjects_dir) 
if not myProjects_dir in sys.path:
    sys.path.append(myProjects_dir)

__package__ = "Rubiks-Cube"
import algs_CFOP

# Group the cubes to be rotated 
def find_cubes(face):
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            if face == 'Right' and obj.location.x >= .5:
                obj.select_set(True) #Right
            if face == 'Left' and obj.location.x <= -.5:
                obj.select_set(True) #Left
            if face == 'Back' and obj.location.y >= .5:
                obj.select_set(True) #Back
            if face == 'Front' and obj.location.y <= -.5:
                obj.select_set(True) #Front
            if face == 'Up' and obj.location.z >= .5:
                obj.select_set(True) #Up
            if face == 'Down' and obj.location.z <= -.5:
                obj.select_set(True) #Down
                
            if face == 'Middle' and obj.location.x < .1 and obj.location.x > -.1:
                obj.select_set(True) #Middle
            if face == 'Side' and obj.location.y < .1 and obj.location.y > -.1:
                obj.select_set(True) #Side
            if face == 'Equator' and  obj.location.z < .1 and obj.location.z > -.1:
                obj.select_set(True) #Equator

angle = math.pi / 2
def get_rotation_params(face):
    match face:
        case 'R':
            return ('Right', 'X', 1)
        case 'R2':
            return ('Right', 'X', 2)
        case "R'":
            return ('Right', 'X', -1)
        case 'L':
            return ('Left', 'X', -1)
        case 'L2':
            return ('Left', 'X', -2)
        case "L'":
            return ('Left', 'X', 1)
        case 'F':
            return ('Front', 'Y', -1)
        case 'F2':
            return ('Front', 'Y', -2)
        case "F'":
            return ('Front', 'Y', 1)
        case 'B':
            return ('Back', 'Y', 1)
        case 'B2':
            return ('Back', 'Y', 2)
        case "B'":
            return ('Back', 'Y', -1)
        case 'U':
            return ('Up', 'Z', 1)
        case 'U2':
            return ('Up', 'Z', 2)
        case "U'":
            return ('Up', 'Z', -1)
        case 'D':
            return ('Down', 'Z', -1)
        case 'D2':
            return ('Down', 'Z', -2)
        case "D'":
            return ('Down', 'Z', 1)
        case 'M':
            return ('Left', 'X', -1)
        case 'M2':
            return ('Left', 'X', -2)
        case "M'":
            return ('Left', 'X', 1)
        case 'S':
            return ('Front', 'Y', -1)
        case 'S2':
            return ('Front', 'Y', -2)
        case "S'":
            return ('Front', 'Y', 1)
        case 'E':
            return ('Down', 'Z', -1)
        case 'E2':
            return ('Down', 'Z', -2)
        case "E'":
            return ('Down', 'Z', 1)
    return None

# Function to rotate a face
def rotate_face(face):
    rotation_params = get_rotation_params(face)
    if rotation_params:
        group_name, axis, dir = rotation_params
        find_cubes(group_name)
        bpy.ops.transform.rotate(value=angle * dir, orient_axis=axis)
        bpy.context.view_layer.objects.active = None

moves = ["F", "B", "L", "R", "U", "D", "f", "r", "d", "M"]
def do_algorithm(alg):
    alg = alg.replace(" ", '')
    length = len(alg)
    for i in range(0, length):
        if alg[i] in moves:
            if i+1 < length and alg[i+1] not in moves:
                rotate_face(alg[i] + alg[i+1])
            else: rotate_face(alg[i])

def scramble():
    bpy.context.scene.frame_current = 0
    do_algorithm("L D2 L U' L' B' R'")
    #do_algorithm("R B L U L' D2 L'") #unscramble
scramble()
