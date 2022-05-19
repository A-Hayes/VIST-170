##### MAYA
import maya.cmds as cmds
import random

# create a sphere
def createTorus(torRadius, torSecRadius):    
    print('Creating A Sphere')    
    tor = cmds.polyTorus(r = torRadius, sr = torSecRadius)    
    return tor

def scaleTor(theObject, scaleX, scaleY, scaleZ):    
    cmds.select(clear = True)    
    cmds.select(theObject)    
    cmds.scale(scaleX, scaleY, scaleZ, theObject)


def shadeObj(anObject, rVal, gVal, bVal):
    objShader = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(objShader + '.color', rVal,gVal,bVal, type='double3')
    cmds.select(anObject)
    cmds.hyperShade(assign=objShader)

def lotsOfObjects(numObjects): 
    for i in range(numObjects):    
        torRad = random.randint(1, 5)
        torSecRad = torRad * 0.5    
        torus = createTorus(torRad,  torSecRad)   

        shadeObj(torus, 0,0,random.random()) 
    
        xTranslate = random.randint(0, numObjects)    
        yTranslate = random.randint(0, numObjects/10)    
        zTranslate = random.randint(0, numObjects)    
    
        cmds.move(xTranslate, yTranslate, zTranslate, torus)

lotsOfObjects(100)