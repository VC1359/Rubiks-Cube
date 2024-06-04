import bpy

def reset():
#    bpy.context.view_layer.objects.active = None
#    bpy.ops.object.select_all(action='DESELECT')
    for collection in bpy.context.scene.collection.children:
        if collection != bpy.data.collections.get('Solved_State'):
            bpy.data.collections.remove(collection)
reset()

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