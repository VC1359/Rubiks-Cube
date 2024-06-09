import bpy
import math

#Set Inverse all Objects (preliminary step)
def set_null():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.select_set(True)
            bpy.ops.constraint.childof_set_inverse(constraint="B", owner='OBJECT')
            bpy.ops.constraint.childof_set_inverse(constraint="C", owner='OBJECT')
            bpy.ops.constraint.childof_set_inverse(constraint="F", owner='OBJECT')
            bpy.ops.constraint.childof_set_inverse(constraint="L", owner='OBJECT')
            bpy.ops.constraint.childof_set_inverse(constraint="R", owner='OBJECT')
            bpy.ops.constraint.childof_set_inverse(constraint="U", owner='OBJECT')
            bpy.ops.constraint.childof_set_inverse(constraint="D", owner='OBJECT')
                   
        bpy.context.active_object.select_set(False)
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj
#set_null()

# Empties define the way the cube rotates
def find_empties():
    empties = []
    for obj in bpy.data.objects:
        if obj.type != 'MESH': empties.append(obj)
    return empties
empties = find_empties()

# Returns Empty object
def locate_empty(empty_name):
    for obj in empties:
        if obj.name == empty_name:
            return obj

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

# Returns [empty, where to find the cubes, axis of rotation, direction of rotation]
def get_rotation_params(notation):
    match notation:
        case 'R':
            return ('R', 'Right', 'X', 1)
        case 'R2':
            return ('R', 'Right', 'X', 2)
        case "R'":
            return ('R', 'Right', 'X', -1)
        case 'L':
            return ('L', 'Left', 'X', -1)
        case 'L2':
            return ('L', 'Left', 'X', -2)
        case "L'":
            return ('L', 'Left', 'X', 1)
        case 'F':
            return ('F', 'Front', 'Y', -1)
        case 'F2':
            return ('F', 'Front', 'Y', -2)
        case "F'":
            return ('F', 'Front', 'Y', 1)
        case 'B':
            return ('B', 'Back', 'Y', 1)
        case 'B2':
            return ('B', 'Back', 'Y', 2)
        case "B'":
            return ('B', 'Back', 'Y', -1)
        case 'U':
            return ('U', 'Up', 'Z', 1)
        case 'U2':
            return ('U', 'Up', 'Z', 2)
        case "U'":
            return ('U', 'Up', 'Z', -1)
        case 'D':
            return ('D', 'Down', 'Z', -1)
        case 'D2':
            return ('D', 'Down', 'Z', -2)
        case "D'":
            return ('D', 'Down', 'Z', 1)
        case 'M':
            return ('C', 'Middle', 'X', -1)
        case 'M2':
            return ('C', 'Middle', 'X', -2)
        case "M'":
            return ('C', 'LeMiddlet', 'X', 1)
        case 'S':
            return ('C', 'Side', 'Y', -1)
        case 'S2':
            return ('C', 'Side', 'Y', -2)
        case "S'":
            return ('C', 'Side', 'Y', 1)
        case 'E':
            return ('C', 'Equator', 'Z', -1)
        case 'E2':
            return ('C', 'Equator', 'Z', -2)
        case "E'":
            return ('C', 'Equator', 'Z', 1)
    return None

# Function to rotate a face
def anim_rot(notation, cur_frame):
    bpy.context.scene.frame_current = cur_frame
    rotation_params = get_rotation_params(notation)
    cubes = []
    if rotation_params:
        empty_name, face, axis, dir = rotation_params
        empty = locate_empty(empty_name)
        find_cubes(face)
        for obj in bpy.context.selected_objects:
            cubes.append(obj)
            for obj_con in obj.constraints:
                if obj_con.name == empty_name:
                    obj_con.influence = 1
                    obj_con.keyframe_insert(data_path="influence")
                    
        bpy.ops.object.select_all(action='DESELECT')
        empty.select_set(True)
        bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")
        
        bpy.context.scene.frame_current += 15
        bpy.ops.transform.rotate(value=math.radians(90) * dir, orient_axis=axis)
        bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")
    
        for cube in cubes:
            for con in cube.constraints:
                if con.name == empty_name:
                    pass
                    #con.influence = 0
                    #con.keyframe_insert(data_path="influence")


moves = ["F", "B", "L", "R", "U", "D", "f", "r", "d", "M"]
def anim_alg(alg, cur_frame):
    alg = alg.replace(" ", '')
    length = len(alg)
    for i in range(0, length):
        if alg[i] in moves:
            if i+1 < length and alg[i+1] not in moves:
                anim_rot(alg[i] + alg[i+1], cur_frame)
            else: anim_rot(alg[i], cur_frame)
            cur_frame += 15

def anim_scramble():
    bpy.context.scene.frame_current = 0
    anim_alg("L", bpy.context.scene.frame_current)
anim_scramble()
