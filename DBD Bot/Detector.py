import pyautogui
import keyboard



def findSkillCheckCoords():
    space = pyautogui.locateCenterOnScreen("space.png", confidence=0.8)

    if (space != None):
        return space[0]-1, space[1]
    
    return 0,0


def whitchSkillCheck(): #detects whitch skill check it is (wiggle or non wiggle)
    wiggleText = pyautogui.locateCenterOnScreen("wiggle text.png", confidence=0.8) #detects if the wiggle text at the bottom of the screen (if resolution is different you may need to change the region)

    if(wiggleText != None):
        print("wiggle skill check")
        return "wiggle"
    
    print("regular skill check")
    return "regular skill check"


def skillCheckDetector():
    if(findSkillCheckCoords() != 0,0):
        skillCheckType = whitchSkillCheck()
        return skillCheckType
    

