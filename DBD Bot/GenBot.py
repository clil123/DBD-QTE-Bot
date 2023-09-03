import pygetwindow as gw
import time
import pyautogui
import keyboard
from PIL import Image
import math
import numpy as np
import os


#(860,440,200,200) skill check area
#(825,830,75,30) wiggle text area (bottom)
#960,525,65 circle center x, center y, radius

time.sleep(2)


""" def skillCheckDetector(): #detects if there is a skill check
    space = pyautogui.locateCenterOnScreen("space.png",region=(860,440,200,200), confidence=0.5) #detects if the space image is on the screen (if resolution is different you may need to change the region)

    if(space != None):
        print("skill check")
        return True
    return False """


def findSkillCheckCoords():
    #space = pyautogui.locateCenterOnScreen("space.png", confidence=0.8)
    space = pyautogui.locateCenterOnScreen(os.path.join('resources',"space.png"), confidence=0.9)

    if (space != None):
        print(f"skill check at {space[0]} {space[1]}")
        return space[0]-1, space[1]
    
    return [0,0]


def whitchSkillCheck(): #detects whitch skill check it is (wiggle or non wiggle)
    #wiggleText = pyautogui.locateCenterOnScreen("wiggle text.png", confidence=0.8) #detects if the wiggle text at the bottom of the screen (if resolution is different you may need to change the region)
    wiggleText = pyautogui.locateCenterOnScreen(os.path.join('resources',"wiggle text.png"), confidence=0.8)

    if(wiggleText != None):
        print("wiggle skill check")
        return "wiggle"
    
    print("regular skill check")
    return "regular skill check"


def skillCheckDetector():
    if(findSkillCheckCoords() != [0,0]):
        skillCheckType = whitchSkillCheck()
        return skillCheckType



def findWhitePlaceOnCircle(centerX, centerY, radius,):
    edges = []
    for angle in range(0, 360, 7):  # Adjust the angle step as needed
        angleRad = math.radians(angle)
        edgeX = int(centerX + radius * math.cos(angleRad))
        edgeY = int(centerY + radius * math.sin(angleRad))
        print("not yet", edgeX,edgeY)
        if(pyautogui.pixelMatchesColor(edgeX,edgeY,(255,255,255))):
            print("white found")
            edges.append((edgeX, edgeY))
            return edges
    
    edges.append((0,0))
    return edges


def regularSkillCheck():
    count = 0
    hyperFocus = 0
    whitePlaces = findWhitePlaceOnCircle(960,525,65)
    whitePlaces = whitePlaces[0]
    print(whitePlaces)
    x = whitePlaces[0]
    y = whitePlaces[1]
    while(pyautogui.pixelMatchesColor(x,y,(255,255,255))):
        count = 1
        print("still white ", x,y)

    if(count == 1 and x >= 985):
        print("right space")
        count = 0
        time.sleep(0.01 + 0.01*hyperFocus)
        pyautogui.press("space")
        time.sleep(0.01)
        return

    elif(count == 1 and x >= 937):
        print("middle space")
        count = 0
        time.sleep(0.008 + 0.008*hyperFocus)
        pyautogui.press("space")
        time.sleep(0.01)
        return

    elif(count == 1):
        print("left space")
        count = 0
        time.sleep(0.015 + 0.015*hyperFocus)
        pyautogui.press("space")
        time.sleep(1)
        return
    
    return


def wiggleSkillCheck():
    """ whitePlaces = findWhitePlaceOnCircle(960,525,65)
    whitePlaces = whitePlaces[0]

    while(True):
        for num in range(0, len(whitePlaces/2),2):
            if(pyautogui.pixelMatchesColor(whitePlaces[num],whitePlaces[num+1],(255,255,255)) == False):
                print("wiggle")
                time.sleep(0.01)
                pyautogui.press("space")
                time.sleep(0.3) """
    
    if(pyautogui.pixelMatchesColor(895,525,(255,255,255), tolerance=20) == False or pyautogui.pixelMatchesColor(1025,525,(255,255,255), tolerance=20) == False):
        print("wiggle")
        print(pyautogui.pixel(895,525) , pyautogui.pixel(1025,525))
        time.sleep(0)
        pyautogui.press("space")
        time.sleep(0.13)
                




#while(gw.getActiveWindowTitle() == "DeadByDaylight  "):
""" count = 0
hyperFocus = input("are you running hyperFocus (Y/N)? ")
if(hyperFocus == "Y" or hyperFocus == "y"):
    hyperFocus = 0.4
elif(hyperFocus == "N" or hyperFocus == "n"):
    hyperFocus = 0
else:
    print("I SAID Y OR N, try again")
    exit """

while(keyboard.is_pressed("q") == False):
    if(skillCheckDetector() == "regular skill check"): #if there is a skill check
        regularSkillCheck()

    elif(skillCheckDetector == "wiggle"):
        wiggleSkillCheck()
                
