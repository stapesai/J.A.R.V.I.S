import pyautogui as jarvis
def openobsstudio():
    jarvis.press('winleft')
    jarvis.write('obs')
    jarvis.press('enter')

    cords=jarvis.locateCenterOnScreen('startcam.png',confidence=0.5)
    while True:
        if cords!=None:
            print('cords founded',cords)
        else:
            print('not found...')
openobsstudio()

