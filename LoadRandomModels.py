import bpy
import os
import random
from mathutils import Vector
from math import sqrt

# Specify your directory containing DAE files
directory = "../Models/DAE format"

# Function to list all DAE files in the specified directory
def list_dae_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.dae')]

# Function to import a DAE file
def import_dae(filepath):
    bpy.ops.wm.collada_import(filepath=filepath)

# Function to check if new location is valid (simple distance check for this example)
def is_valid_location(new_object, existing_objects, min_distance=5):
    new_location = new_object.location
    for obj in existing_objects:
        existing_location = obj.location
        distance = sqrt((new_location.x - existing_location.x) ** 2 + (new_location.y - existing_location.y) ** 2)
        if distance < min_distance:  # Adjust min_distance as needed
            return False
    return True

# Main function to import models and place them randomly
def place_models_randomly(directory, total_models=500):
    dae_files = list_dae_files(directory)
    placed_objects = []
    
    for _ in range(total_models):
        # Select a random DAE file to import
        filepath = random.choice(dae_files)
        import_dae(filepath)
        
        # Get the most recently imported object
        new_object = bpy.context.selected_objects[0]  # Assuming the imported object is selected
        
        # Try placing the object, ensuring no overlap
        for _ in range(100):  # Attempt 100 times to find a non-colliding position
            new_object.location = (random.uniform(-5, 5), random.uniform(0, 1000), 0)
            if is_valid_location(new_object, placed_objects):
                placed_objects.append(new_object)
                break

# Run the script
place_models_randomly(directory)
