def Find_Unread_Msg():
    import pyautogui as jarvis
    Unread_Msg=jarvis.locateCenterOnScreen('img\green_dot.png', confidence=0.7)
    if Unread_Msg!=None:
        print('There is a new Message ....')
        x=Unread_Msg[0]-30
        y=Unread_Msg[1]
        jarvis.click(x, y)
        return True
    else:
        print('No New Message Found....')
        return False