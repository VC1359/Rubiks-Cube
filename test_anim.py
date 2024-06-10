import bpy
import math
import mathutils

# Group the cubes to be rotated 
def find_and_select_cubes(face):
    selected_cubes = []
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            
            # Gives the cube global coordinates
            obj.select_set(True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            
            if face == 'Right' and obj.location.x >= .5:
                selected_cubes.append(obj) #Right
            if face == 'Left' and obj.location.x <= -.5:
                selected_cubes.append(obj) #Left
            if face == 'Back' and obj.location.y >= .5:
                selected_cubes.append(obj) #Back
            if face == 'Front' and obj.location.y <= -.5:
                selected_cubes.append(obj) #Front
            if face == 'Up' and obj.location.z >= .5:
                selected_cubes.append(obj) #Up
            if face == 'Down' and obj.location.z <= -.5:
                selected_cubes.append(obj) #Down
                
            if face == 'Middle' and obj.location.x < .1 and obj.location.x > -.1:
                selected_cubes.append(obj) #Middle
            if face == 'Side' and obj.location.y < .1 and obj.location.y > -.1:
                selected_cubes.append(obj) #Side
            if face == 'Equator' and obj.location.z < .1 and obj.location.z > -.1:
                selected_cubes.append(obj) #Equator

    # Restores cube center to origin
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    bpy.ops.object.select_all(action='DESELECT')
    for cube in selected_cubes:
        cube.select_set(True)

# Returns [where to find the cubes, axis of rotation, direction of rotation]
def get_rotation_params(notation):
    match notation:
        case 'R':
            return ('Right', 'X', -1)
        case 'R2':
            return ('Right', 'X', 2)
        case "R'":
            return ('Right', 'X', 1)
        case 'L':
            return ('Left', 'X', 1)
        case 'L2':
            return ('Left', 'X', -2)
        case "L'":
            return ('Left', 'X', -1)
        case 'F':
            return ('Front', 'Y', 1)
        case 'F2':
            return ('Front', 'Y', -2)
        case "F'":
            return ('Front', 'Y', -1)
        case 'B':
            return ('Back', 'Y', -1)
        case 'B2':
            return ('Back', 'Y', 2)
        case "B'":
            return ('Back', 'Y', 1)
        case 'U':
            return ('Up', 'Z', -1)
        case 'U2':
            return ('Up', 'Z', 2)
        case "U'":
            return ('Up', 'Z', 1)
        case 'D':
            return ('Down', 'Z', 1)
        case 'D2':
            return ('Down', 'Z', 2)
        case "D'":
            return ('Down', 'Z', -1)
        case 'M':
            return ('Middle', 'X', 1)
        case 'M2':
            return ('Middle', 'X', 2)
        case "M'":
            return ('Middle', 'X', -1)
        case 'S':
            return ('Side', 'Y', 1)
        case 'S2':
            return ('Side', 'Y', 2)
        case "S'":
            return ('Side', 'Y', -1)
        case 'E':
            return ('Equator', 'Z', 1)
        case 'E2':
            return ('Equator', 'Z', 2)
        case "E'":
            return ('Equator', 'Z', -1)
    return None

# Function to rotate a face
def anim_rot(notation):
    face, axis, dir = get_rotation_params(notation)
    find_and_select_cubes(face)
    
    for obj in bpy.context.selected_objects:
        obj.keyframe_insert(data_path="rotation_quaternion")

    bpy.context.scene.frame_current += 15
    angle = math.radians(90) * dir
    quat = mathutils.Quaternion()
    
    if axis == 'X':
        quat = mathutils.Quaternion((1, 0, 0), angle)
    elif axis == 'Y':
        quat = mathutils.Quaternion((0, 1, 0), angle)
    elif axis == 'Z':
        quat = mathutils.Quaternion((0, 0, 1), angle)
    
    for obj in bpy.context.selected_objects:
        obj.rotation_quaternion = quat @ obj.rotation_quaternion
        obj.keyframe_insert(data_path="rotation_quaternion")
    bpy.context.scene.frame_current += 1

moves = ["F", "B", "L", "R", "U", "D", "f", "r", "d", "M"]
def anim_alg(alg):
    alg = alg.replace(" ", '')
    length = len(alg)
    for i in range(length):
        if alg[i] in moves:
            if i + 1 < length and alg[i + 1] not in moves:
                anim_rot(alg[i] + alg[i + 1])
            else:
                anim_rot(alg[i])

def anim_scramble():
    bpy.context.scene.frame_current = 0
    anim_alg("L D2 L U' L' B' R'") #scramble
    anim_alg("R B L U L' D2 L'") #unscramble
anim_scramble()
