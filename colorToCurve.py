import maya.cmds as cmds

def change_override_color(color):
    # """
    # Change the override color of the shape node(s) for the selected object(s).

    # Parameters:
    #    color (tuple): RGB values for the desired color (0.0 to 1.0).
    # """
    # Get the selected objects
    selected_objects = cmds.ls(selection=True, dag=True)

    if not selected_objects:
        cmds.warning("Please select at least one object.")
        return
    
    # Iterate through selected objects
    for obj in selected_objects:
        print(obj)
        # Get the shape node(s) for the current object
        shape_nodes = cmds.listRelatives(obj, children=True) #or []
        print(shape_nodes)

        for shape_node in shape_nodes:
                # Check if the shape node has an override color attribute
            # if cmds.attributeQuery("baseColor", exists=True, node=shape_node):
            print("Yeehaw")
                # Set the override color for the shape node
            cmds.setAttr(f"{obj}.standardSurface1.baseColor", *color)

# Example usage:
# Change override color to red (1.0, 0.0, 0.0) for selected objects
change_override_color((1.0, 0.0, 0.0))
