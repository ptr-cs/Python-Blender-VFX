import bpy

# Create the chrome material
chrome_material = bpy.data.materials.new(name="ChromeMaterial")
chrome_material.use_nodes = True
nodes = chrome_material.node_tree.nodes

# Clear default nodes
for node in nodes:
    nodes.remove(node)

# Create necessary nodes
bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
bsdf_node.location = (0, 0)
bsdf_node.inputs['Metallic'].default_value = 1.0  # Max metallic
bsdf_node.inputs['Roughness'].default_value = 0.0  # Min roughness for chrome effect
bsdf_node.inputs['Base Color'].default_value = (0.8, 0.8, 0.8, 1)  # Slightly off-white color

output_node = nodes.new(type='ShaderNodeOutputMaterial')
output_node.location = (200, 0)

# Link nodes
links = chrome_material.node_tree.links
link = links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])

# Assign the chrome material to all objects that can have materials
for obj in bpy.data.objects:
    if obj.type in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT']:
        # Clear existing materials
        obj.data.materials.clear()
        # Assign the new chrome material
        obj.data.materials.append(chrome_material)

print("All applicable objects have been set to a chrome-like material.")
