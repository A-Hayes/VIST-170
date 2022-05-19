import MASH.api as mapi
import maya.cmds as cmds
import random

#new file
cmds.file(force=True, new=True)

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
    

#don't set position or dynamics with Egg's functions, MASH will do that for us
originalEgg = Egg(1,  1)
originalEgg.create()
originalEgg.setColor()

# create a new MASH network
mashNetwork = mapi.Network()
mashNetwork.createNetwork(name="Eggs")

# When you create a MASH network it creates 
# some default nodes
# print out the default node names
print(mashNetwork.waiter)
print(mashNetwork.distribute)
print(mashNetwork.instancer)

cmds.setAttr(mashNetwork.distribute+'.arrangement', 3)
cmds.setAttr(mashNetwork.distribute+'.pointCount', 75)

# We can change the distribution
# each is represeneted by a number
# 1 = linear, 2 = radial, 3 = spherical, 4 = mesh, 5 = inPositionPP, 6 = Grid, 
# 7 = Initial State 8 = Paint Effects 9 = volume
print(mashNetwork.distribute+'arrangement')
cmds.setAttr(mashNetwork.distribute+'.arrangement', 6)
cmds.setAttr(mashNetwork.distribute+'.gridx', 5)
cmds.setAttr(mashNetwork.distribute+'.gridy', 5)
cmds.setAttr(mashNetwork.distribute+'.gridz', 5)

node = mashNetwork.addNode("MASH_Dynamics")

cmds.setAttr(mashNetwork.waiter+'_BulletSolverShape.groundPlanePositionY', -10)


cmds.setAttr(node.name+'.bounce', 1)



randomNode = mashNetwork.addNode("MASH_Random")
print(randomNode)
cmds.setAttr(mashNetwork.waiter+'_Random.scaleX', 1)
cmds.setAttr(mashNetwork.waiter+'_Random.scaleY', 10)
cmds.setAttr(mashNetwork.waiter+'_Random.scaleZ', .5)


