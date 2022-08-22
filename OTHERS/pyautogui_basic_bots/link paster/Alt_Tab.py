import pyautogui
def Alt_Tab():
    # Holds down the alt key
    pyautogui.keyDown("alt")

    # Presses the tab key once
    pyautogui.press("tab")

    # Lets go of the alt key
    pyautogui.keyUp("alt")