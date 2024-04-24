import bpy

def setup_hdri_lighting(hdri_path):
    # Load the HDRI image
    bpy.ops.image.open(filepath=hdri_path)
    hdri_img = bpy.data.images.load(hdri_path)

    # Set up environment texture
    if not bpy.data.worlds['World'].node_tree:
        bpy.data.worlds['World'].use_nodes = True
    world_nodes = bpy.data.worlds['World'].node_tree.nodes
    world_nodes.clear()
    env_texture = world_nodes.new('ShaderNodeTexEnvironment')
    env_texture.image = hdri_img
    background = world_nodes.new('ShaderNodeBackground')
    world_output = world_nodes.new('ShaderNodeOutputWorld')

    # Connect the nodes
    bpy.data.worlds['World'].node_tree.links.new(env_texture.outputs['Color'], background.inputs['Color'])
    bpy.data.worlds['World'].node_tree.links.new(background.outputs['Background'], world_output.inputs['Surface'])

def add_light(name, type, location, rotation, energy):
    # Create a new light data object
    light_data = bpy.data.lights.new(name=name, type=type)
    light_data.energy = energy
    
    # Create a new object with the light data
    light_object = bpy.data.objects.new(name=name, object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    
    # Set light location and rotation
    light_object.location = location
    light_object.rotation_euler = rotation

def setup_three_point_lighting():
    # Key light
    add_light('Key Light', 'AREA', (10, -10, 10), (0.436332, 0.785398, 0.436332), 1000)
    # Fill light
    add_light('Fill Light', 'AREA', (-10, 10, 10), (0.436332, 0.785398, -0.436332), 500)
    # Back light
    add_light('Back Light', 'AREA', (0, -15, 10), (0.785398, 0, 0), 750)

# Path to your HDRI image
hdri_path = '/Users/.../Downloads/noon_grass_4k.exr'

# Set up the lighting
setup_hdri_lighting(hdri_path)
setup_three_point_lighting()
