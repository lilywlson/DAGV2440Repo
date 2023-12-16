import maya.cmds as cmds
import random

class windowUI:
    def __init__(self):
        self.selected_objects = None

    def create_ui(self):
        window_name = "windowUI"
        if cmds.window(window_name, exists=True):
            cmds.deleteUI(window_name, window=True)

        cmds.window(window_name, title="Window UI", widthHeight=(300, 150))
        cmds.columnLayout(adjustableColumn=True)
        cmds.button(label="Duplicate and Disperse", command=self.duplicate_and_disperse)
        cmds.text(label="Number of Duplicates:")
        duplicateCountField = cmds.intFieldGrp(numberOfFields=1, label=" ")

        cmds.text(label="X Range:")
        xRangeField = cmds.floatFieldGrp(numberOfFields=2, label="Min Max")

        cmds.text(label="Y Range:")
        yRangeField = cmds.floatFieldGrp(numberOfFields=2, label="Min Max")

        cmds.text(label="Z Range:")
        zRangeField = cmds.floatFieldGrp(numberOfFields=2, label="Min Max")
        
        cmds.showWindow(window_name)

    

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

if __name__ == "__main__":
    ui = windowUI()
    ui.create_ui()

# Example usage:
# duplicate_and_disperse(5, -10, 10, 0, 20, -5, 5)
