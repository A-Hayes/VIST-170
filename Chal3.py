# Asa Hayes
# VIST-170 
# 5 Feb 2021

# Slide 1
print("Slide 1: ")
numberList = [0,1,2,3,4,5]
print(numberList)

# Slide 2
print("\nSlide 2: ")
rainbowColors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(rainbowColors)
print(type(rainbowColors))

# Slide 3
print("\nSlide 3: ")
longList = list(range(0, 501, 1))
print(longList)

shortList = list(range(0, 4, 1))
print(shortList)

print(len(longList))
print(len(shortList))

# Slide 4
print("\nSlide 4: ")
reallyLongList = shortList + longList
print(len(reallyLongList))

# Slide 5
print("\nSlide 5: ")
print(1 in numberList)

# Slide 7
print("\nSlide 7: ")
print(rainbowColors[0])
print(rainbowColors[6])

print(reallyLongList[-1])
print(reallyLongList[-2])

# Slide 8
print("\nSlide 8: ")
print(rainbowColors[:3])

# Slide 9
print("\nSlide 9: ")
print(rainbowColors.index("blue"))

rainbowColors[rainbowColors.index("yellow")] = "lemon"
print(rainbowColors)

rainbowColors[rainbowColors.index("blue")] = "azul"
print(rainbowColors)

# Slide 10
print("\nSlide 10: ")
import maya.cmds as cmds

# Slide 11
print("\nSlide 11: ")
cmds.select(all=True)
cmds.delete()

# Slide 12
print("\nSlide 12: ")
tall = cmds.polyPyramid(n="tall")
taller = cmds.polyPyramid(n="taller")
tallest = cmds.polyPyramid(n="tallest")

# Slide 13
print("\nSlide 13: ")
listOfPyramids = cmds.ls( 'tall*', sl=False, geometry=True)
print(listOfPyramids)
print(type(listOfPyramids))

print(listOfPyramids[0])
print(listOfPyramids[1])
print(listOfPyramids[2])


# Slide 14
print("\nSlide 14: ")
cmds.scale(1, 2, 1, listOfPyramids[0])
cmds.move(2.75, 0.75, 0, listOfPyramids[0])

cmds.scale(1, 0.5, 1, listOfPyramids[2])
cmds.move(-2.75, 0.75, 0, listOfPyramids[2])