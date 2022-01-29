from ast import Call
import pytesseract
from PIL import ImageGrab

def Caller_Name():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\swast\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    cap = ImageGrab.grab(bbox =(1630, 85, 1910, 130))
    ocr = pytesseract.image_to_string(cap, lang ='eng')
    return ocr


while True:
    print(Caller_Name())