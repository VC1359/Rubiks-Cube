import bpy
import math

# Creates a collection (for faces)
def create_collection(name):
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)    
    return collection

# Adds a cube to a collection
def add_to_collection(obj, collection_name):
    collection = bpy.data.collections.get(collection_name)
    if collection:
        collection.objects.link(obj)
#        bpy.context.scene.collection.objects.unlink(obj)

# Groups faces and create collections
def define_collections():
    create_collection('Right')
    create_collection('Left')
    create_collection('Front')
    create_collection('Back')
    create_collection('Up')
    create_collection('Down')
    create_collection('Middle')
    create_collection('Side')
    create_collection('Equator')


# Manual Init
def start():
    define_collections()
    # Group the cubes into collections
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            if obj.location.x >= .5:
                add_to_collection(obj, 'Right')
            elif obj.location.x <= -.5:
                add_to_collection(obj, 'Left')
            if obj.location.y >= .5:
                add_to_collection(obj, 'Back')
            elif obj.location.y <= -.5:
                add_to_collection(obj, 'Front')
            if obj.location.z >= .5:
                add_to_collection(obj, 'Up')
            elif obj.location.z <= -.5:
                add_to_collection(obj, 'Down')

# Function needs to be finished           
def scramble(scramble): # Input should look like "D2 R' F" 
    pass
#    for move in range(0,len(scramble)-1):
#        if scramble[move+1] == ' ':
#            rotate_face(scramble[move])
#        else if scramble[move+1] == '2' or scramble[move+1] == "'":
#            rotate_face(scramble[move])
#            
#        else if s

def reset_collections():
    for collection in bpy.context.scene.collection.children:
        if collection != bpy.data.collections.get('Solved_State'):
            bpy.data.collections.remove(collection)

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
        collection_name, axis, dir = rotation_params
        collection = bpy.data.collections.get(collection_name)
        if collection:
            bpy.context.view_layer.objects.active = None
            for obj in collection.objects:
                obj.select_set(True)
            bpy.ops.transform.rotate(value=angle * dir, orient_axis=axis)
    reset_collections()

start()
