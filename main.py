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
#    create_collection('Middle')
#    create_collection('Side')
#    create_collection('Equator')


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
start()

angle = math.pi / 2
def get_rotation_params(face):
    match face:
        case 'R':
            return ('Right', 'X', 1)
        case "R'":
            return ('Right', 'X', -1)
        case 'L':
            return ('Left', 'X', -1)
        case "L'":
            return ('Left', 'X', 1)
        case 'F':
            return ('Front', 'Y', -1)
        case "F'":
            return ('Front', 'Y', 1)
        case 'B':
            return ('Back', 'Y', 1)
        case "B'":
            return ('Back', 'Y', -1)
        case 'U':
            return ('Up', 'Z', 1)
        case "U'":
            return ('Up', 'Z', -1)
        case 'D':
            return ('Down', 'Z', -1)
        case "D'":
            return ('Down', 'Z', 1)
#        case 'M':
#            return ('Left', 'X', -1)
#        case "M'":
#            return ('Left', 'X', 1)
#        case 'S':
#            return ('Front', 'Y', -1)
#        case "S'":
#            return ('Front', 'Y', 1)
#        case 'E':
#            return ('Down', 'Z', -1)
#        case "E'":
#            return ('Down', 'Z', 1)
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

# Example rotations (accepts R', L', etc)
#rotate_face("R")  # R
#rotate_face("L")  # L
#rotate_face("F")  # F
#rotate_face("B")  # B
#rotate_face("U")  # U
#rotate_face("D")  # D