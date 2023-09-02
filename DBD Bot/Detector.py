import pyautogui
import os



def findSkillCheckCoords():
    #space = pyautogui.locateCenterOnScreen("space.png", confidence=0.8)
    space = pyautogui.locateCenterOnScreen(os.path.join('resources',"space.png"), confidence=0.8)

    if (space != None):
        print(f"skill check at {space[0]} {space[1]}")
        return space[0], space[1]
    
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
    

