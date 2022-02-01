import pyautogui as jarvis
def openobsstudio():
    jarvis.press('winleft')
    jarvis.sleep(1)
    jarvis.write('obs')
    jarvis.sleep(1)
    jarvis.press('enter')
    jarvis.sleep(7)
    
    while True:
        cords=jarvis.locateCenterOnScreen('startcam.png',confidence=0.8)
        if cords!=None:
            print('cords founded',cords)
            jarvis.click(cords)
            break
        else:
            print('not found...')

