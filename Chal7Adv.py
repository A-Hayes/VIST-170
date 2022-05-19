# Asa Hayes
# VIST-170
# 5 March, 2021


import maya.cmds as cmds
import random

numberOfPyr = 500
pyrs         = 0
while pyrs < numberOfPyr:     
    print("Constructing Pyramid ", pyrs)  
    
    # generate random salcing values from 0.0 to 1.0
    xScale = random.random()
    yScale = random.random()
    zScale = random.random()
    
    # with a coinflip, decide if scaling up or down since scaling would always be down otherwise (downscale is < 1.0)
    if random.random() >= 0.5:
        xScale = xScale + 1
    if random.random() >= 0.5:
        yScale = yScale + 1
    if random.random() >= 0.5:
        zScale = zScale + 1
    
    # create pyramid
    aPyr = cmds.polyPyramid(w=5)  

    # scale and rotate as directed by exercise
    cmds.scale(xScale, yScale, zScale, aPyr) 
    cmds.rotate(random.randint(0,360), 0, 0, aPyr)

    # move to random location on grid. Grid limits are numberOfPyr/4 in pos/neg, for total of numberOfPyr/2 total per side
    cmds.move(random.randint(-(numberOfPyr/4),(numberOfPyr/4)), 5*yScale, random.randint(-(numberOfPyr/4),(numberOfPyr/4)), aPyr)  
       
    pyrs = pyrs + 1 
