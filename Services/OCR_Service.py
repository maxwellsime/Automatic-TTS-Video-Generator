import cv2 as cv
import PIL
from pytesseract import image_to_string, pytesseract

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def ocr_text_image(img_path):
    print("Reading Image")
    img = cv.imread(img_path)

    print("Pre-Processing Image")
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # edged_img = cv.Canny(gray_img, 30, 30)

    print("Performing Character Recognition")
    otsu_thresh_image = PIL.Image.fromarray(gray_img)
    return image_to_string(otsu_thresh_image)
