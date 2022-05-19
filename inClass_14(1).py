import maya.cmds as cmds

'''


shape = cmds.polySphere()

# set key frames
cmds.setKeyframe(shape[0], time = 1, attribute = 'rotateY', value = 0)
cmds.setKeyframe(shape[0], time = 150, attribute = 'rotateY', value = 720)

cmds.setKeyframe(shape[0], time = 1, attribute = 'translateX', value = 0)
cmds.setKeyframe(shape[0], time = 150, attribute = 'translateX', value = 5)


cmds.setKeyframe(shape[0], time = 1, attribute = 'scaleY', value = 1)
cmds.setKeyframe(shape[0], time = 150, attribute = 'scaleY', value = 3)

#new file
cmds.file(force = True,  new = True)

cmds.playbackOptions(animationStartTime=1)
cmds.playbackOptions(animationEndTime = 500)

cmds.playbackOptions(minTime=1) 
cmds.playbackOptions(maxTime=200)

# Bouncing Ball

#new file
cmds.file(force = True,  new = True)

ball = cmds.polySphere(radius=2)

cmds.setKeyframe(ball[0], time=1,  attribute='translateY', value = 10)
cmds.setKeyframe(ball[0], time=10, attribute='translateY', value = 2)

cmds.setKeyframe(ball[0], time=16,  attribute='translateY', value = 8)
cmds.setKeyframe(ball[0], time=22, attribute='translateY',  value = 2)

cmds.setKeyframe(ball[0], time=26,  attribute='translateY', value = 6)
cmds.setKeyframe(ball[0], time=30, attribute='translateY',  value = 2)

cmds.setKeyframe(ball[0], time=32,  attribute='translateY', value = 4)
cmds.setKeyframe(ball[0], time=34, attribute='translateY',  value = 2)

#SQUASH AND STRETCH 
cmds.setKeyframe(ball[0], time=1,  attribute='scaleY', value = 1)
cmds.setKeyframe(ball[0], time=9,  attribute='scaleY',  value = 1.5)
cmds.setKeyframe(ball[0], time=10,  attribute='scaleY',  value = .5)

cmds.setKeyframe(ball[0], time=16,  attribute='scaleY', value = 1)
cmds.setKeyframe(ball[0], time=21,  attribute='scaleY',  value = 1.5)
cmds.setKeyframe(ball[0], time=22,  attribute='scaleY',  value = .5)

cmds.setKeyframe(ball[0], time=26,  attribute='scaleY', value = 1)
cmds.setKeyframe(ball[0], time=29,  attribute='scaleY',  value = 1.5)
cmds.setKeyframe(ball[0], time=30,  attribute='scaleY',  value = .5)

cmds.setKeyframe(ball[0], time=32,  attribute='scaleY', value = 1)
cmds.setKeyframe(ball[0], time=33,  attribute='scaleY',  value = 1.5)
cmds.setKeyframe(ball[0], time=34,  attribute='scaleY',  value = .5)

cmds.setKeyframe(ball[0], time=35,  attribute='scaleY',  value = 1)


# NEW SCENE - LOTS OF SHAPES!!!

shape = cmds.polyTorus()

# Variables
keyFrame = 1
scaleValue = 1
scaleFactor = 3

xTranslate = 1
xTranslateFactor = 2

for frame in range(1,10):
    cmds.setKeyframe(shape[0], time=keyFrame, attribute = 'scaleX', value=scaleValue)
    #MORE KEYFRAMES

    # Advance keyframe
    keyFrame += 20 # keyFrame = keyFrame + 1
    scaleValue *= scaleFactor

# RANDOM FUNCTIONS 

'''


import random

cmds.file(force = True, new = True)

for i in range(50):
    cmds.polyCube()
    cmds.move(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20))


cubes = cmds.ls('pCube*', transforms=True)
print cubes


for cube in cubes: 
    print cube
    #cmds.setKeyframe(cube, time=1, attribute = 'scaleX', value=10)
    cmds.setKeyframe(cube, time=1, attribute = 'rotateY', value=0)
    cmds.setKeyframe(cube, time=200, attribute = 'rotateY', value=random.randint(20, 360))

    # cmds.setKeyframe(cube, time = 1, attribute = 'rotateY', value = 0)
    # cmds.setKeyframe(cube, time =200, attribute = 'rotateY', value = 360)




