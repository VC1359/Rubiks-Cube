## Running in Blender exports object data into the below files (need triangles)
import bpy
obj = bpy.context.objct
mesh = obj.data

file1 = open("Rubiks_Cube/Cube_Model/vertices.txt", "a")
file2 = open("Rubiks_Cube/Cube_Model/faces.txt", "a")

for vert in mesh.vertices:
    xyz = vert.co.xyz
    file1.write(f"({xyz[0]}, {xyz[1]}, {xyz[2]}),\n")

for face in mesh.faces:
    file2.write(f"({face.vertices[0]}, {face.vertices[1]}, {face.vertices[2]}),\n")
