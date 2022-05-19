import maya.cmds as cmds
import random


def randAnim(shapeList, startAnim, endAnim):
    for shape in shapeList:
        cmds.setKeyframe(shape, time=startAnim, attribute = 'translateY', value=random.randint(1,25))
        cmds.setKeyframe(shape, time=(endAnim/2) + startAnim, attribute = 'translateY', value=random.randint(30,50))
        cmds.setKeyframe(shape, time=endAnim, attribute = 'translateY', value=2)

class Egg: 
    def __init__(self, size, scaleY ): 
        self.size   = size
        self.scaleY = scaleY
        self.name   = []
        self.x = 0
        self.y = 0
        self.z = 0 

    def create(self):
        self.name = cmds.polySphere(radius = self.size)
        cmds.scale(1.2, self.scaleY, 1.2, self.name[0])
        # we want it on the ground
        cmds.move(0, self.scaleY*self.size, 0, self.name[0])

    def randomPosition(self):
        self.x = random.randint(-20, 20)
        self.y = self.scaleY*self.size
        self.z = random.randint(-20, 20)
        cmds.move(self.x, self.y, self.z, self.name[0])

    def randomRotation(self):
        cmds.rotate(random.randint(0,360), random.randint(0,360), random.randint(0,360), self.name[0])

    def setColor(self):
        rv = random.random()
        bv = random.random()
        gv = random.random()
        shadingNode = cmds.shadingNode( 'blinn', asShader=True ) 
        cmds.setAttr( shadingNode+".color", rv, gv, bv, type='double3' ) 
        shadingGroup = cmds.sets(name=self.name[0]+'SG', empty=True, renderable=True, noSurfaceShader = True)

        cmds.connectAttr(shadingNode+'.outColor', shadingGroup+'.surfaceShader')
        cmds.select(self.name[0])
        cmds.sets(e=True, forceElement=shadingGroup)

cmds.file(force = True, new = True)

#start actual code here
for egg in range(50):
    eggSize = random.randint(1, 2)
    eggHeight = random.randint(1, 2)
    oneEgg = Egg(eggSize, eggHeight)
    oneEgg.create()
    oneEgg.setColor()
    oneEgg.randomPosition() 
    oneEgg.randomRotation()

eggList = cmds.ls('pSphere*', transforms=True)

startTime = 55 
endTime = 200

cmds.cutKey( time=(startTime,endTime) )

randAnim(eggList, startTime,endTime)








'''

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


'''

