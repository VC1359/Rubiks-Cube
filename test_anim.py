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

def test_animate():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.frame_current = 0
    current_frame = bpy.context.scene.frame_current
    cubes = []
    
    for obj in bpy.data.objects:
        if obj.location.x >= .5:
            if obj.type == 'MESH':
                cubes.append(obj)
                for obj_con in obj.constraints:
                    if obj_con.name == "R":
                        obj_con.influence = 1
                        obj_con.keyframe_insert(data_path="influence", frame=current_frame)
            else: 
                obj.select_set(True)
                bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")
        
    bpy.context.scene.frame_current += 15
    bpy.ops.transform.rotate(value=math.radians(90), orient_axis='X')
    bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")
    print(cubes)
test_animate()