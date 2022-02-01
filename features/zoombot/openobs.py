import pyautogui as jarvis
def openobsstudio():
    jarvis.press('winleft')
    jarvis.write('obs')
    jarvis.press('enter')
    jarvis.sleep(10)
    cords=jarvis.locateCenterOnScreen('image\startcam.png',confidence=0.5)
    while True:
        if cords!=None:
            print('cords founded',cords)
            break
        else:
            print('not found...')
openobsstudio()

