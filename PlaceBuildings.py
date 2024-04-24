import bpy
import os
import random
from mathutils import Vector
from math import sqrt

# Specify your directory containing DAE files
directory = "/Users/.../Downloads/kenney_city-kit-commercial/Models/DAE format"

# Modified function to list only DAE files containing "building" or "skyscraper" in the filename
def list_dae_files(directory):
    keywords = ['building', 'skyscraper']
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.dae') and any(keyword in f.lower() for keyword in keywords)]

# Function to import a DAE file and select the imported object(s)
def import_dae_and_select(filepath):
    # Deselect all objects to ensure a clean state
    bpy.ops.object.select_all(action='DESELECT')
    
    # Import the DAE file
    bpy.ops.wm.collada_import(filepath=filepath)
    
    # The imported objects are automatically selected after import
    # Here you can perform additional operations on the selected objects if needed
    # For example, to store the selected objects:
    imported_objects = [obj for obj in bpy.context.selected_objects]
    return imported_objects

# Function to check if new location is valid
def is_valid_location(new_object, existing_objects, min_distance=5):
    new_location = new_object.location
    for obj in existing_objects:
        existing_location = obj.location
        distance = sqrt((new_location.x - existing_location.x) ** 2 + (new_location.y - existing_location.y) ** 2)
        if distance < min_distance:  # Adjust min_distance as needed
            return False
    return True

# Main function to import models and place them randomly
def place_models_randomly(directory, total_models=250):
    dae_files = list_dae_files(directory)
    placed_objects = []
    
    if not dae_files:
        print("No matching DAE files found in the specified directory.")
        return
    
    for _ in range(250):
        filepath = random.choice(dae_files)
        imported_objects = import_dae_and_select(filepath)
        
        for new_object in imported_objects:
            # Try placing the object, ensuring no overlap
            for _ in range(100):
                new_object.location = (random.uniform(-5, 5), random.uniform(0, 250), 0)
                if is_valid_location(new_object, placed_objects):
                    placed_objects.append(new_object)
                    break

# Run the script
place_models_randomly(directory)
