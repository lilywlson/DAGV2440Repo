import maya.cmds as cmds
import random

def duplicate_and_disperse(num_duplicates, min_x, max_x, min_y, max_y, min_z, max_z):
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("Please select at least one object to duplicate.")
        return 0

    for _ in range(num_duplicates):
        duplicate_objects = cmds.duplicate(selected_objects)

        rand_x = random.uniform(min_x, max_x)
        rand_y = random.uniform(min_y, max_y)
        rand_z = random.uniform(min_z, max_z)

        cmds.move(rand_x, rand_y, rand_z, duplicate_objects)

    return 1

# Example usage:
duplicate_and_disperse(5, -10, 10, 0, 20, -5, 5)
