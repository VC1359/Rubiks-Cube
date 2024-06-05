import bpy
import math

def reset_cube():
    c = 1
    for i in range(1,27):
        if i == 14: c -= 1 # Cube 14 is 'real' center (shift over one)
        for obj in bpy.data.objects:
            if obj.name == str(i):
                obj.rotation_euler = (0,0,0)
                x = (i-c)%3 - 1
                y = -1 * math.floor(((i-c)%9)/3) + 1
                z = -1 * math.floor((i-c)/9) + 1
                obj.location = (x,y,z)
reset_cube()

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
        #bpy.context.scene.collection.objects.unlink(obj)

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