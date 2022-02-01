import pyautogui as jarvis
def openobsstudio():
    jarvis.press('winleft')
    jarvis.write('obs')
    jarvis.press('enter')
    jarvis.sleep(10)
    cords=jarvis.locateCenterOnScreen('startcam.png',confidence=0.8)
    while True:
        if cords!=None:
            print('cords founded',cords)
            jarvis.click(cords)
            break
        else:
            print('not found...')
openobsstudio()
