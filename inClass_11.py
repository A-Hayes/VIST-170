#### MAYA #####
import maya.cmds as cmds
import random

def newScene():
    cmds.file( force=True, new=True )

#Class to encapulate the data and behaviors needed for an EGG

# What Properties would an egg have 
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
        cmds.scale(1.5, self.scaleY, 1.5, self.name[0])
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

    def setDynamics(self):    
        cmds.connectDynamic(self.name[0], fields='gravityField')        
        cmds.setAttr(self.name[0]+'.centerOfMassY',-1)        
        cmds.setAttr(self.name[0]+'.mass',3)        
        cmds.setAttr(self.name[0]+'.staticFriction',1)        
        cmds.setAttr(self.name[0]+'.dynamicFriction',.5)        
        cmds.setAttr(self.name[0]+'.bounciness', 1)

newScene()
# create a variable to store the number of eggs to draw
numOfEggs = 5

cmds.gravity(position=(0, 0, 0), magnitude=9.8, directionX=0, directionY=-1, directionZ=0, name='gravityField')

cmds.polyPlane()    
cmds.scale(50,1,50)    
cmds.select("pPlane1")    
cmds.rigidBody(passive=True)


for egg in range(numOfEggs):
    # create an instance of class Egg - which is called an object
    eggSize = random.randint(2, 3)
    eggHeight = random.randint(2, 3)
    oneEgg = Egg(eggSize, eggHeight)
    # draw it 
    oneEgg.create()
    #set the color 
    oneEgg.setColor()
    # random position
    oneEgg.randomPosition() 
    oneEgg.randomRotation()
    oneEgg.setDynamics()


