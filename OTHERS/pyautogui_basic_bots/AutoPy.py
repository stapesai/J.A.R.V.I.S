import pyautogui
pyautogui.sleep(5)
#import random
rocku=open('C:\\Users\\swast\\Downloads\\realuniq.lst','r',encoding="CP1252")
lines=rocku.read(22)
print(lines)
for j in rocku:
    print(j)
    pyautogui.write(j)
    pyautogui.press('enter')

# pyautogui.write('This is to demonstrate my new automation code, Enjoy!')
#for i in range(1,2):
    #for z in range(10000000,99999999):
        #x=str(z)
        #pyautogui.write(x)
        # pyautogui.keyDown('ctrl')
        #pyautogui.press('enter')
        # pyautogui.keyUp('ctrl')