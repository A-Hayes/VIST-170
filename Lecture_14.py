import maya.cmds as cmds

'''

# LETS DO SOME ANIMATION
# I am going to create a sphere
# and simply make it rotate

mySphere = cmds.polySphere()
cmds.setKeyframe(mySphere[0], time = 1, attribute = 'rotateY', value = 0)

#LETS run that much 
#notice there is a little red line in the timeline to show a keyframe has been set
# NOT V Exciting though
# Lets give ourselves 200 Frames

cmds.setKeyframe(mySphere[0], time = 200, attribute = 'rotateY', value = 180)
cmds.setKeyframe(mySphere[0], time = 1,   attribute = 'translateX', value = -10)
cmds.setKeyframe(mySphere[0], time = 200, attribute = 'translateX', value = 20)

cmds.file( force=True, new=True )


cmds.playbackOptions(animationStartTime=1)
cmds.playbackOptions(animationEndTime=500)

cmds.playbackOptions(minTime=0)
cmds.playbackOptions(maxTime=300)

cmds.play(forward=True)
cmds.play( state=False )

shape = cmds.cube()
#cmds.setKeyframe('mCube',attribute = 'ty',value = 0,time=1)
cmds.setKeyframe(shape[0],attribute = 'translateX',value = 2.5,time=1)
cmds.setKeyframe(shape[0],attribute = 'translateX',value = 10,time=100)
cmds.setKeyframe(shape[0],attribute = 'translateY',value = 0,time=101)
cmds.setKeyframe(shape[0],attribute = 'translateY',value = 10,time=200)
cmds.setKeyframe(shape[0],attribute = 'translateX',value = 10,time=201)
cmds.setKeyframe(shape[0],attribute = 'translateX',value = 0,time=300)
cmds.setKeyframe(sphere[0],attribute = 'translateY',value = 10,time=301)
cmds.setKeyframe(shape[0],attribute = 'translateY',value = 0,time=400)




cmds.file( force=True, new=True )

shape=cmds.polyCube()
cmds.setKeyframe(shape[0],attribute = 'scaleX',value = 2,time = 1)
cmds.setKeyframe(shape[0],attribute = 'scaleX',value = 6,time = 25)
cmds.setKeyframe(shape[0],attribute = 'scaleY',value = 2,time = 31)
cmds.setKeyframe(shape[0],attribute = 'scaleY',value = 6,time = 50)
cmds.setKeyframe(shape[0],attribute = 'scaleZ',value = 2,time = 70)
cmds.setKeyframe(shape[0],attribute = 'scaleZ',value = 6,time = 100)
cmds.setKeyframe(shape[0],attribute = 'scaleX',value = 6,time = 101)
cmds.setKeyframe(shape[0],attribute = 'scaleY',value = 6,time = 101)
cmds.setKeyframe(shape[0],attribute = 'scaleZ',value = 6,time = 101)
cmds.setKeyframe(shape[0],attribute = 'scaleX',value = 1,time = 125)
cmds.setKeyframe(shape[0],attribute = 'scaleY',value = 1,time = 125)
cmds.setKeyframe(shape[0],attribute = 'scaleZ',value=1,time = 125)


# Lets try a ball bounce 
cmds.file( force=True, new=True )

ball = cmds.polySphere(radius = 2)
# we need to move it up
# set posiition one up 10 units 
cmds.setKeyframe(mySphere[0], time = 1, attribute = 'translateY', value = 10)

# now lets move to frame 10 and put the ball on the ground
cmds.setKeyframe(mySphere[0], time = 10, attribute = 'translateY', value = 2)


# as the ball bounces it looses momentum
# so its not going to reach as high as 10 again  
# and its going to slow down
# so its taken 10 frames to hit the ground 
# so lets go about 6 more frames and move it up to 6 units
cmds.setKeyframe(mySphere[0], time = 16, attribute = 'translateY', value = 6)

# A Convinicing ball bounce takes thes same amount of time to come down as it did to go up
# so it took 6 frames to go up - lets give it 6 to come down
cmds.setKeyframe(mySphere[0], time = 22, attribute = 'translateY', value = 2)

# Okay lets reduce the frames and the height
# Lets try 4 frames and 4 units up
cmds.setKeyframe(mySphere[0], time = 26, attribute = 'translateY', value = 4)

cmds.setKeyframe(mySphere[0], time = 30, attribute = 'translateY', value = 2)


cmds.setKeyframe(mySphere[0], time = 33, attribute = 'translateY', value = 3)
cmds.setKeyframe(mySphere[0], time = 36, attribute = 'translateY', value = 2)

cmds.setKeyframe(mySphere[0], time = 38, attribute = 'translateY', value = 2.5)
cmds.setKeyframe(mySphere[0], time = 40, attribute = 'translateY', value = 2)

# we can do one frame at a time just to get the tiny settling bounces
cmds.setKeyframe(mySphere[0], time = 41, attribute = 'translateY', value = 2.5)
cmds.setKeyframe(mySphere[0], time = 42, attribute = 'translateY', value = 2)
cmds.setKeyframe(mySphere[0], time = 43, attribute = 'translateY', value = 2.25)
cmds.setKeyframe(mySphere[0], time = 44, attribute = 'translateY', value = 2)

cmds.keyTangent (inTangentType='linear', outTangentType='linear')

# Lets add some squash and stretch
# perfectly round on key 1
# stretch before it hits ground 
cmds.setKeyframe(mySphere[0], time = 1, attribute = 'scaleY', value = 1)
cmds.setKeyframe(mySphere[0], time = 9, attribute = 'scaleY', value = 1.2)
cmds.setKeyframe(mySphere[0], time = 10, attribute = 'scaleY', value = .8)

cmds.setKeyframe(mySphere[0], time = 16, attribute = 'scaleY', value = 1)
cmds.setKeyframe(mySphere[0], time = 21, attribute = 'scaleY', value = 1.1)
cmds.setKeyframe(mySphere[0], time = 22, attribute = 'scaleY', value = 0.6)

cmds.setKeyframe(mySphere[0], time = 26, attribute = 'scaleY', value = 1)

cmds.cutKey( time=(0,1000) )

cmds.file( force=True, new=True )
shape = cmds.polySphere()
keyFrame = 1
scaleValue = 1
scaleFactor = 1.1
xTranslate = 1
xTranslateFactor = 2 
for frame in range(1, 50):
    print frame
    cmds.setKeyframe(shape[0], time = keyFrame, attribute = 'scaleX', value = scaleValue)
    cmds.setKeyframe(shape[0], time = keyFrame, attribute = 'scaleY', value = scaleValue)
    cmds.setKeyframe(shape[0], time = keyFrame, attribute = 'scaleZ', value = scaleValue)
    cmds.setKeyframe(shape[0], time = keyFrame, attribute = 'translateX', value = xTranslate)
    keyFrame += 20
    print keyFrame
    scaleValue *= scaleFactor
    xTranslate *= xTranslateFactor


'''

import random
import maya.cmds as cmds
cmds.cutKey( time=(0,500) )

cmds.file( force=True, new=True )

for i in range(100):
    cmds.polySphere(radius = random.randint(1, 2))
    cmds.move(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))


spheres = cmds.ls('pSphere*', transforms=True)

print spheres

for sphere in spheres:
    print sphere 
    cmds.setKeyframe(sphere, time = 1,   attribute = 'rotateY', value = 0)
    cmds.setKeyframe(sphere, time = 350, attribute = 'rotateY', value = 360)
    cmds.setKeyframe(sphere, time = 1,   attribute = 'translateY', value = random.randint(1, 10))
    cmds.setKeyframe(sphere, time = 175, attribute = 'translateY', value = random.randint(1, 5))
    cmds.setKeyframe(sphere, time = 350, attribute = 'translateY', value = 0)












