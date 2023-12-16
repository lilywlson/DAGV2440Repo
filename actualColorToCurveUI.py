import maya.cmds as cmds

class windowUI:
    def __init__(self):
        self.color = (1.0, 0.0, 0.0)

    def create_ui(self):
        window_name = "windowUI"
        if cmds.window(window_name, exists=True):
            cmds.deleteUI(window_name, window=True)

        cmds.window(window_name, title="Window UI", widthHeight=(300, 100))
        cmds.columnLayout(adjustableColumn=True)
        cmds.button(label="Change Override Color", command=self.change_override_color)
        cmds.showWindow(window_name)

    def change_override_color(x,y):
        color = (1.0, 0.0, 0.0)
        print("Yeehaw")
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

if __name__ == "__main__":
    ui = windowUI()
    ui.create_ui()

# change_override_color((1.0, 0.0, 0.0))