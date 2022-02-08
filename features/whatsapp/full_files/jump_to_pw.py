import pyautogui as jarvis

def jump_to_pw():
    pw_cordinates=jarvis.locateCenterOnScreen('img\pw_logo.png', confidence=0.5)
    if pw_cordinates!=None:
        print('Jumpinging To PW....',pw_cordinates)
        x=pw_cordinates[0]
        y=pw_cordinates[1]
        jarvis.click(x, y)
        #jarvis.sleep(1)
    else:
        print('Can not jump to PW....')

#jump_to_pw()