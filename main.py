import bpy
import math
import sys
import mathutils
import pathlib

#Lets us import from our files (not sure what it does, or if needed?)
path = pathlib.Path(bpy.data.filepath)
myProjects_dir = path.parent.resolve() 
myProjects_dir = str(myProjects_dir) 
if not myProjects_dir in sys.path:
    sys.path.append(myProjects_dir)

__package__ = "Rubiks-Cube"
import algs_CFOP
import stage_interpreter

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

# Rotates faces without animating it
def rotate(notation):
    face, axis, dir = get_rotation_params(notation)
    find_and_select_cubes(face)
    
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

# Animates the rotation
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
def do_algorithm(alg, animate):
    alg = alg.replace(" ", '')
    length = len(alg)
    for i in range(length):
        if alg[i] in moves:
            if i + 1 < length and alg[i + 1] not in moves:
                if animate: anim_rot(alg[i] + alg[i + 1])
                else: rotate(alg[i] + alg[i + 1])
            else:
                if animate: anim_rot(alg[i])
                else: rotate(alg[i])

# Define global face directions
face_directions = {
    'U': (0, 0, 1),
    'D': (0, 0, -1),
    'B': (0, 1, 0),
    'F': (0, -1, 0),
    'R': (1, 0, 0),
    'L': (-1, 0, 0)
}
# Rounds vector components and replace -0.0 with 0.0
def clean_vector(vector):
    return tuple(0.0 if round(comp, 2) == -0.0 else round(comp, 2) for comp in vector)

# Returns a list of the faces corresponding to the normals
def get_faces_from_normals(normals):
    faces = []
    for vector in normals:
        for face, direction in face_directions.items():
            if all(vector[i] == direction[i] for i in range(3)):
                faces.append(face)
                break
    return faces

# Returns a list of normals of the colored faces given the indexed list of materials
def get_piece_face_from_normals(obj, mat_id_list):
    normals = []
    if mat_id_list == 1:
        for poly in obj.data.polygons:
            if poly.material_index == mat_id_list:
                normals.append(clean_vector(poly.normal))
        return get_faces_from_normals(normals)
        
    for i in range(0, len(mat_id_list)):
        for poly in obj.data.polygons:
            if poly.material_index == mat_id_list[i]:
                normals.append(clean_vector(poly.normal))
                break
    return get_faces_from_normals(normals)
                
# Creates piece objects for each type of piece            
def get_data():
    current_state = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            if obj.name in ["2", "4", "6", "8", "10", "12", "15", "17", "19", "21", "23", "25"]:
                faces = get_piece_face_from_normals(obj, (1,2))
                piece = stage_interpreter.edge_p(obj.name, faces[0], (obj.material_slots[1].name[0], obj.material_slots[2].name[0]), faces)
                current_state.append(piece)
                continue
            elif obj.name in ["1", "3", "7", "9", "18", "20", "24", "26"]:
                faces = get_piece_face_from_normals(obj, (1,2,3))
                piece = stage_interpreter.corner_p(obj.name, faces[0], (obj.material_slots[1].name[0], obj.material_slots[2].name[0], obj.material_slots[3].name[0]), faces)
                current_state.append(piece)
                continue
            else: 
                faces = get_piece_face_from_normals(obj, (1))
                piece = stage_interpreter.center_p(obj.name, faces[0], (obj.material_slots[1].name[0]), faces)
                current_state.append(piece)
                continue
    return current_state


def start(alg, animate=False):
    bpy.context.scene.frame_current = 0
    state = get_data()
    for cube in state:
        print(cube.name, cube.faces)

    do_algorithm(alg, animate)
    print()

    state2 = get_data()
    for cube in state2:
        print(cube.name, cube.faces)

#start("L D2 L U' L' B' R'") #scramble
start("R B L U L' D2 L'") #unscramble