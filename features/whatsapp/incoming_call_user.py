import pytesseract
import pyautogui as jarvis
from PIL import ImageGrab

def Caller_Name():
    attend_call_cordinates=jarvis.locateCenterOnScreen('img\call_attend.png', confidence=0.5)
    if attend_call_cordinates!=None:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\swast\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        cap = ImageGrab.grab(bbox =(1630, 120, 1910, 130))
        cap.save()
        #print(type(cap))
        ocr = pytesseract.image_to_string(cap, lang ='eng')
        return ocr
    else:
        return 'No incoming call user....'

# while True:
#     print(Caller_Name())