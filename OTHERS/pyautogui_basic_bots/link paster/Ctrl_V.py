import pyautogui
def Ctrl_V():
    # Holds down the alt key
    pyautogui.keyDown("ctrl")

    # Presses the tab key once
    pyautogui.press("v")

    # Lets go of the alt key
    pyautogui.keyUp("ctrl")