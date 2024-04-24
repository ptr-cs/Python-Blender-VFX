import bpy
import os
import math
import random  # Ensure the random module is imported

# Specify your directory containing DAE files
directory = "/Users/.../Downloads/kenney_space-kit/Models/DAE format"

# Function to list all DAE files in the specified directory
def list_dae_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.dae')]

# Function to import a DAE file
def import_dae(filepath):
    bpy.ops.wm.collada_import(filepath=filepath)

# Function to place and rotate models along a circular path
def place_and_rotate_models_in_circle(directory, total_models=135, circle_radius=95):
    dae_files = list_dae_files(directory)
    
    if len(dae_files) == 0:
        print("No DAE files found in the specified directory.")
        return
    
    for i in range(total_models):
        # Select a random DAE file to import
        filepath = random.choice(dae_files)
        import_dae(filepath)
        
        # Calculate the angle for the current object
        angle = (math.pi * 2) / total_models * i
        
        # Calculate the position for the current object
        x = math.cos(angle) * circle_radius
        y = math.sin(angle) * circle_radius
        
        # Get the most recently imported object
        new_object = bpy.context.selected_objects[0]  # Assuming the imported object is selected
        
        # Update the object's location
        new_object.location = (x, y, 0)
        
        # Rotate the object to face the direction of the circle's tangent
        # The tangent direction at any point on the circle is perpendicular to the radius
        # So, we can use the angle plus 90 degrees (or pi/2 radians) to set the correct rotation
        tangent_angle = angle + math.pi / 2
        new_object.rotation_euler = (0, 0, tangent_angle)

# Run the script
place_and_rotate_models_in_circle(directory)
