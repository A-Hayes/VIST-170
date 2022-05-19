# Asa Hayes
# VIST-170
# 12 Feb 2021

# Challenge 4: More Lists
# Slide 1-2
print("Slide 1-2: ")
import maya.cmds as cmds

# Slide 3
print("Slide 3: ")
print(cmds.ls())

print(cmds.ls(transforms=True))
print(cmds.ls(shapes=True))
print(cmds.ls(cameras=True))
print(cmds.ls(lights=True))
print(cmds.ls(geometry=True))

print(cmds.ls(sl=True))

selection = cmds.ls(sl=True, showType=True)
print(selection)

# Slide 4
print("Slide 4: ")
cmds.select(all=True)
cmds.delete()

sphereObj1 = cmds.polySphere(n='mySphere1')
sphereObj2 = cmds.polySphere(n='mySphere2')
sphereObj3 = cmds.polySphere(n='mySphere3')

cubeObj1 = cmds.polyCube(n='myCube1')
cubeObj2 = cmds.polyCube(n='myCube2')
cubeObj3 = cmds.polyCube(n='myCube3')
cubeObj4 = cmds.polyCube(n='myCube4')

# Slide 5
print("Slide 5: ")
torusObj1 = cmds.polyTorus(n='myTorus1')
torusObj2 = cmds.polyTorus(n='myTorus2')
torusObj3 = cmds.polyTorus(n='myTorus3')

# Slide 6
print("Slide 6: ")
cmds.select(clear=True)
sphereList = cmds.ls('*Sp*', sl=False)

# Slide 7
print("Slide 7: ")
print(type(sphereList))

print(sphereList)

sphereList = cmds.ls( '*Sp*', sl=False, type='transform')
print(sphereList)

# Slide 8-9
print("Slide 8-9: ")
cubeList = cmds.ls('*Cu*', sl=False, type='transform')
print(cubeList)
torusList = cmds.ls('*To*', sl=False, type='transform')
print(torusList)

# Slide 10
print("Slide 10: ")
cmds.scale(5, 5, 5, sphereList[0])
cmds.move(5, 5, 0, sphereList[0])

cmds.scale(0.5, 0.5, 0.5, sphereList[1])
cmds.move(-2, 7, 0, sphereList[1])

cmds.scale(2, 2, 2, sphereList[2])
cmds.move(0, 12, 0, sphereList[2])

# Slide 11
print("Slide 11: ")
cmds.scale(5, 5, 5, cubeList[0])
cmds.move(15, 0, 0, cubeList[0])

cmds.scale(0.5, 0.5, 0.5, cubeList[1])
cmds.move(0, 0, 0, cubeList[1])

cmds.scale(2, 2, 2, cubeList[2])
cmds.move(-5, 5, 0, cubeList[2])

cmds.scale(2, 2, 2, cubeList[3])
cmds.move(-15, 5, 0, cubeList[3])

# Slide 12
print("Slide 12: ")
cmds.scale(4,4,4, cubeList)

# Slide 13
print("Slide 13: ")
cmds.scale(5, 5, 5, torusList[0])
cmds.move(0, 5, 5, torusList[0])

cmds.scale(0.5, 0.5, 0.5, torusList[1])
cmds.move(0, 7, -2, torusList[1])

cmds.scale(2, 2, 2, torusList[2])
cmds.move(12, 0, 12, torusList[2])

# Slide 14
print("Slide 14: ")
shinyRed = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr(shinyRed + '.color', 1,0,0, type='double3')
cmds.select(sphereList)
cmds.hyperShade(assign=shinyRed)

# Slide 15-16
print("Slide 15-16: ")
flatBlue = cmds.shadingNode('lambert', asShader=True)
cmds.setAttr(flatBlue + '.color', 0,0,1, type='double3')
cmds.select(cubeList)
cmds.hyperShade(assign=flatBlue)

# Slide 17
print("Slide 17: ")
aniPurple = cmds.shadingNode('anisotropic', asShader=True)
cmds.setAttr(aniPurple + '.color', 1,0,1, type='double3')
cmds.select(torusList)
cmds.hyperShade(assign=aniPurple)

# Slide 18
print("Slide 18: ")
sphereObj4 = cmds.polySphere(n='mySphere4')
cmds.move(-10,0,0, sphereObj4)
print(sphereObj4)

sphereList.append(sphereObj4[0])
print(sphereList)

cmds.select(sphereList)
cmds.hyperShade(assign=shinyRed)

# Slide 19
print("Slide 19: ")
torusObj4 = cmds.polyTorus(n='myTorus4')
cmds.move(0,0,-10, torusObj4)
print(torusObj4)

torusList.append(torusObj4[0])
print(torusList)

cmds.select(torusList)
cmds.hyperShade(assign=aniPurple)

# Slide 20 / Advanced Challenge
print("Advanced Challenge: ")
#clear all prev objects
cmds.select(all=True)
cmds.delete()

#create new obj list of different obj types
otherObj1 = cmds.polyCone(n='otherCone')
otherObj2 = cmds.polyPyramid(n='otherPyr')
otherObj3 = cmds.polyCylinder(n='otherCyl')
otherList = cmds.ls( '*ot*', sl=False, type='transform')
 
#scale & move
cmds.scale(10,10,10, otherList)

cmds.move(0, 5, 5, otherList[0])
cmds.move(10, 5, 0, otherList[1])
cmds.move(-10, 0, -5, otherList[2])

#apply green blinn shader to list
otherGreen = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr(otherGreen + '.color', 0,1,0, type='double3')
cmds.select(otherList)
cmds.hyperShade(assign=otherGreen) 