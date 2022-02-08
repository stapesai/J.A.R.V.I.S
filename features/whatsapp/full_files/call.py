import pyautogui as jarvis

def attend_call():
    global attend_call_cordinates
    attend_call_cordinates=jarvis.locateCenterOnScreen('img\call_attend.png', confidence=0.7)
    if attend_call_cordinates!=None:
        print('Attending Call....',attend_call_cordinates)
        x=attend_call_cordinates[0]
        y=attend_call_cordinates[1]
        jarvis.click(x, y)
        jarvis.sleep(1)
    else:
        print('Can not find call_attend button...')

def decline_call():
    global decline_call_cordinates
    decline_call_cordinates=jarvis.locateCenterOnScreen('img\call_decline.png', confidence=0.7)
    if decline_call_cordinates!=None:
        print('Declining Call....',decline_call_cordinates)
        x=decline_call_cordinates[0]
        y=decline_call_cordinates[1]
        jarvis.click(x, y)
        jarvis.sleep(1)
    else:
        print('Can not find decline_attend button...')

def cut_call():
    global cut_call_cordinates
    cut_call_cordinates=jarvis.locateCenterOnScreen('img\call_cut.png', confidence=0.7)
    if cut_call_cordinates!=None:
        print('Cutting Call....',cut_call_cordinates)
        x=cut_call_cordinates[0]
        y=cut_call_cordinates[1]
        jarvis.click(x, y)
        jarvis.sleep(1)
#attend_call()
#decline_call()