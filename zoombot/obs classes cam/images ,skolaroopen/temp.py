import pyautogui as zoombot

while True:

    cords=zoombot.locateCenterOnScreen('obs classes cam\images ,skolaroopen\skaolarosite.PNG',confidence=0.9)
    if cords!=None:
        print('cordinates founded:',cords)
     #   zoombot.click(cords)
    else:
        print('cords not founded')