import pytesseract
import pyautogui
from PIL import ImageGrab

def Caller_Name():
    attend_call_cordinates=pyautogui.locateCenterOnScreen('img\call_attend.png', confidence=0.7)
    if attend_call_cordinates!=None:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Reinstall Tesseract-OCR in this location 'C:\Program Files\Tesseract-OCR'
        cap = ImageGrab.grab(bbox =(1630, 85, 1910, 130))
        ocr = pytesseract.image_to_string(cap, lang ='eng')
        return ocr
    else:
        return 'No incoming call user....'