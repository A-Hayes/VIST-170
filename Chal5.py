import maya.cmds as cmds

# Asa Hayes
# VIST-170
# 22 Feb 2021

# Challenge 5: If Statements
""" 
# Slide 3
print("Slide 3\n")
bodySize = 5
headSize = 5
neckSize = 4
legSize = 3
earSize = 4
tailSize = 4

# Slide 4-6
print("Slide 4-6\n")

character = raw_input('Do you want to build a Dog? (Choosing no will create default dog): [y/n]')

if character=='y':
    print("\nLet's build a Dog.\n")
    body = input('Enter Body Size: 1(Short) / 2(Medium) / 3(Long)')
    if body == 1:
        bodySize = 5
    elif body == 2: 
        bodySize = 3
    else: 
        bodySize = 4

    head = input('\nEnter Head Size: 1(Short) / 2(Long)')
    if head == 1:
        headSize = 5
    else: 
        headSize = 4

    legs = input('\nEnter Leg Size: 1(Short) / 2(Medium) / 3(Long)')
    if legs == 1:
        legSize = 2
    elif legs == 2: 
        legSize = 2.5
    else: 
        bodySize = 3

    tail = input('\nEnter Tail Size: 1(Short) / 2(Long)')
    if tail == 1:
        tailSize = 4
    else: 
        tailSize = 3

    neck = input('\nEnter Neck Size: 1(Short) / 2(Long)\n')
    if neck == 1:
        neckSize = 3
    else: 
        neckSize = 4

# Slide 7
print("Slide 7\n")

cmds.select(all=True)
cmds.delete()

# Slide 8
print("Slide 8\n")

bodyShape = cmds.polySphere(r = bodySize)
print(bodyShape)
cmds.setAttr(bodyShape[0]+'.scaleY', bodySize/2)
cmds.setAttr(bodyShape[0]+'.rotateX', 90)

# Slide 9
print("Slide 9\n")

neckShape = cmds.polySphere(r = neckSize, n="neck")
print(neckShape)
cmds.setAttr(neckShape[0]+'.scaleY', neckSize/2.0)
cmds.setAttr(neckShape[0]+'.rotateX', 50)
cmds.setAttr(neckShape[0]+'.translateZ', bodySize*2)
cmds.setAttr(neckShape[0]+'.translateY', neckSize+bodySize)

# Slide 10
print("Slide 10\n")

headShape = cmds.polySphere(r = headSize, n="head")
print(headShape)
cmds.setAttr(headShape[0]+'.scaleY', headSize/2.0)
cmds.setAttr(headShape[0]+'.rotateX', 65)
if headSize == 4:
    cmds.setAttr(headShape[0]+'.translateZ', (bodySize+neckSize)*2)
else:
    cmds.setAttr(headShape[0]+'.translateZ', (bodySize+neckSize)*3)

cmds.setAttr(headShape[0]+'.translateY', (headSize*2)+neckSize+bodySize)

# Slide 11
print("\nSlide 11\n")

tailShape = cmds.polySphere(r = tailSize, n="tail")
print(tailShape)
cmds.setAttr(tailShape[0]+'.rotateX', -50)
cmds.setAttr(tailShape[0]+'.translateZ', -bodySize*2.5)
cmds.setAttr(tailShape[0]+'.translateY', tailSize*2)
cmds.select(tailShape)
cmds.scale(0.75, tailSize/2.0, 0.75)

# Slide 12
print("\nSlide 12\n")

leftLegF = cmds.polySphere(r = legSize, n="leftFLeg")
rightLegF = cmds.polySphere(r = legSize, n="rightFLeg")
leftLegB = cmds.polySphere(r = legSize, n="leftBLeg")
rightLegB = cmds.polySphere(r = legSize, n="rightBLeg")

# Slide 13
print("Slide 13\n")

legsAll = cmds.ls('*Leg', sl=False)
print(legsAll)

cmds.select(legsAll)
cmds.scale(0.75, legSize, 0.75)

cmds.select(legsAll[0])
cmds.move(legSize*2, -legSize*2, bodySize*1.5)

cmds.select(legsAll[1])
cmds.move(-legSize*2, -legSize*2, bodySize*1.5)

cmds.select(legsAll[2])
cmds.move(legSize*2, -legSize*2, -bodySize*1.5)

cmds.select(legsAll[3])
cmds.move(-legSize*2, -legSize*2, -bodySize*1.5)

# Slide 14
print("\nSlide 14\n")

headX = cmds.objectCenter('headShape', x=True)
print(headX)
headY = cmds.objectCenter('headShape', y=True)
print(headY)
headZ = cmds.objectCenter('headShape', z=True)
print(headZ)

# Slide 15
print("\nSlide 15\n")

leftEar = cmds.polySphere(r = 3)
cmds.select(leftEar)
cmds.rotate(-50, 0, 0)
cmds.scale(1, earSize, 1)
cmds.move(-2, headY+8, headZ-(headSize*3))

rightEar = cmds.polySphere(r = 3)
cmds.select(rightEar)
cmds.rotate(-50, 0, 0)
cmds.scale(1, earSize, 1)
cmds.move(2, headY+8, headZ-(headSize*3)) """

# Slide 17-Challenge
print("Slide 17-Challenge\n")
 
# Uncomment to show challenge results
# Will create a snowman, all elements scaled to body size

cmds.select(all=True)
cmds.delete()

#set defaults
bodySize = 3
isHat = False
isScarf = False

buildSnow = raw_input('Do you want to build a Snowman? (Choosing no will create default snowman): [y/n]')
# Please don't copyright-strike my code Disney, no affiliation to Frozen

if buildSnow=='y':
    print("\nLet's build a Snowman.\n")

    # legs/bottom segment and head will be directly scaled from body size
    body = input('Enter Body Size: 1(Small) / 2(Medium) / 3(Large)')
    if body == 1:
        bodySize = 2
    elif body == 3: 
        bodySize = 4
    else: 
        bodySize = 3
    
    hatCheck = input('Do you want a hat for your snowman?: 1(Yes) / 2(No)')
    if hatCheck == 1:
        isHat = True

    scarfCheck = input('Do you want a scarf for your snowman?: 1(Yes) / 2(No)')
    if scarfCheck == 1:
        isScarf = True

snowBottom = cmds.polySphere(r = bodySize*1.25)
snowBody = cmds.polySphere(r = bodySize)
snowHead = cmds.polySphere(r = bodySize * 0.75)

cmds.select(snowBody)
cmds.move(0, bodySize*1.4, 0)
cmds.select(snowHead)
cmds.move(0, (bodySize*1.4)*2, 0)

# handle hat
if isHat==True:
    hatTop = cmds.polyCylinder(r = bodySize * 0.6, h=3)
    hatBrim = cmds.polyCylinder(r = bodySize*0.8, h=0.1)

    cmds.select(hatBrim)
    cmds.move(0, (bodySize*1.4)*2.4, 0)
    cmds.select(hatTop)
    cmds.move(0, (bodySize*1.4)*2.8, 0)

# handle scarf
if isScarf==True: 
    scarfBand = cmds.polyCylinder(r = bodySize * 0.8, h=1)
    scarfDrape = cmds.polyCube(d=0.1, w=1, h=bodySize+1)

    cmds.select(scarfBand)
    cmds.move(0, (bodySize*1.4)*1.5, 0)
    cmds.select(scarfDrape)
    cmds.move(1.25, (bodySize*1.4)*1.2, bodySize-0.4)
    cmds.rotate(-15, 30, 0)

# Adv Challenge
# Note: Default setting is no mood, i.e. no Shader

""" mood = "n"
mood = input('Enter Mood: 1(Light) / 2(Dark)')
if mood == 1:
    color = "Light"
elif mood == 2:
    color = "Dark" """ 