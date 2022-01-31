import pyautogui as jarvis
def openobsstudio():
    jarvis.press('winleft')
    jarvis.write('obs')
    jarvis.press('enter')
    vc_on=jarvis.locateCenterOnScreen('startcam.png',confidence=0.5)

