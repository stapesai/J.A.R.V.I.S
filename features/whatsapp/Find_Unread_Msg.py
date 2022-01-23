import pyautogui as jarvis

# Step 2 : Find Unread msg
def Find_Unread_Msg():
    global Unread_Msg
    Unread_Msg=jarvis.locateCenterOnScreen('img\green_dot.png', confidence=0.7)
    print('Unread message Location : ',Unread_Msg)
    if Unread_Msg!=None:
        print('There is a new Message ....')
        x=Unread_Msg[0]-30
        y=Unread_Msg[1]
        jarvis.click(x, y)
        #jarvis.sleep(1)
    else:
        print('No New Message Found....')