import pyautogui as jarvis
import pyperclip
jarvis.FAILSAFE=False
message='sample'
def Copy_Msg():
    Copy_Msg=jarvis.locateCenterOnScreen('img\smiley.png', confidence=0.5)
    if Copy_Msg!=None:
        x=Copy_Msg[0]+30
        y=Copy_Msg[1]-70
        jarvis.moveTo(x,y)
        jarvis.tripleClick()
        jarvis.keyDown('ctrl')
        jarvis.write('c')
        jarvis.keyUp('ctrl')
        global message
        message = pyperclip.paste()
        jarvis.click()
        print("message received: " + message)
        
        # Clicking on text box
        Click_On_Text_Box=jarvis.locateCenterOnScreen('img/textbox.png', confidence=0.5)
        if Click_On_Text_Box!=None:
            jarvis.click(Click_On_Text_Box[0], Click_On_Text_Box[1])

    else:
        print('None')
while True:
    print('Copy_Msg file output : ',message)
    # Getting Out of loop
    if message=='sample':
        break