import maya.cmds as cmds

def change_override_color(color):
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("Please select at least one object.")
        return
    
    for obj in selected_objects:
        shape_nodes = cmds.listRelatives(obj, shapes=True) #or []
        print(shape_nodes)

        for shape_node in shape_nodes:
            cmds.setAttr(f"{shape_node}.overrideEnabled", True)
            cmds.setAttr(f"{shape_node}.overrideRGBColors", True)
            cmds.setAttr(f"{shape_node}.overrideColorRGB", *color)

change_override_color((1.0, 0.0, 0.0))