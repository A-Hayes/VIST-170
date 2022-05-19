# Asa Hayes
# VIST-170
# 5 March, 2021

import maya.cmds as cmds
import random


for i in range(2000):     
    print("Constructing Tree ", i+1)  
    
    # set random scale factor for y value
    # decided to have range as 1 +/- 0.7, since the lower limit was 0.3  
    yScale = random.random()  
    if yScale < 0.3:
        yScale = 0.3

    # same as provided code, except the trunk height can be changed by default since its only 1 dimension
    leavesRadius = random.randint(3, 5)
    trunkRadius = random.randint(1, 2)    
    trunkHeight = random.randint(7, 11) * yScale  

    # create leaves AND THEN scale y to generated value, otherwise woudl just create a different size sphere   
    # then moves leaves to top of trunk
    leaves = cmds.polySphere(r = leavesRadius, n='leaves'+str(i+1))  
    cmds.scale(1, yScale, 1, leaves)  
    cmds.move(0, trunkHeight/2 , 0, 'leaves'+str(i+1))  

    # this section same as given code
    trunk  = cmds.polyCylinder(r = trunkRadius, h=trunkHeight, n='trunk'+str(i+1))    
    tree = cmds.group( 'leaves'+str(i+1), 'trunk'+str(i+1), n='tree'+str(i+1)) 

    # move tree to random point on grid
    # to make grid of size grdiSize, use (-gridSize/2,gridSize/2) for x and z pos
    cmds.move(random.randint(-250,250), trunkHeight/2, random.randint(-200, 200), tree)  

     

# scale leaves in x and z as directed, can do in bulk due to similar names and *wildcard
cmds.select('leaves*')
cmds.scale(1.5,1,1.5)