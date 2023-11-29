import maya.cmds as cmds

cone = cmds.polyCone(ch=True, o=True, r=3.505138, h=10.062447, cuv=3)

cmds.select(cone)
cmds.rotate(0, 0, -180)

sphere1 = cmds.polySphere(ch=True, o=True, r=3.372323)
sphere2 = cmds.polySphere(ch=True, o=True, r=3.372323)
sphere3 = cmds.polySphere(ch=True, o=True, r=3.372323)

cmds.select(sphere1)
cmds.move(0, 6.481878, 0)

cmds.select(sphere2)
cmds.move(0, 10.513793, 0)

cmds.select(sphere3)
cmds.move(0, 14.510241, 0)