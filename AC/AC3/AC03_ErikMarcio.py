import bpy
import math

# 1. Cria um Cilindro (Objeto 3D)
bpy.ops.mesh.primitive_cylinder_add(location=(4, 0, 1.5))
cilindro = bpy.context.active_object
cilindro.name = "obj3d_cilindro_script"

# Aplica transformações no Cilindro (Rotação em X e Y, Escala em Z)
cilindro.rotation_euler = (math.radians(45), math.radians(15), 0)
cilindro.scale = (1.0, 1.0, 2.5)

# 2. Cria um Triângulo (Objeto 2D - Círculo com 3 vértices com face preenchida)
bpy.ops.mesh.primitive_circle_add(vertices=3, fill_type='NGON', location=(4, 0, 4))
triangulo = bpy.context.active_object
triangulo.name = "obj2d_triangulo_script"

# Aplica transformações no Triângulo (Rotação no eixo Z para manter-se 2D, e Escala global)
triangulo.rotation_euler = (0, 0, math.radians(90))
triangulo.scale = (1.5, 1.5, 1.5)


triangulo.parent = cilindro