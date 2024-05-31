import bpy

def reset():
#    bpy.context.view_layer.objects.active = None
#    bpy.ops.object.select_all(action='DESELECT')
    for collection in bpy.context.scene.collection.children:
        if collection != bpy.data.collections.get('Solved_State'):
            bpy.data.collections.remove(collection)
reset()