import pytesseract
from PIL import Image

def extractFromFile(imagefile=None):
    # pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe' # for windows
    # img = Image.open('Example-code-mixed-sentences-with-words-from-Hindi-and-English-languages-The.png')
    if imagefile!=None:
        img = Image.open(imagefile)
        return pytesseract.image_to_string(img, 'eng')
    else:
        return 'Nothing to show'
print(extractFromFile())