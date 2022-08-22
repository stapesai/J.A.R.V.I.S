import pyautogui
def Ctrl_C():
    # Holds down the alt key
    pyautogui.keyDown("ctrl")

    # Presses the tab key once
    pyautogui.press("c")

    # Lets go of the alt key
    pyautogui.keyUp("ctrl")