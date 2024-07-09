import cv2 as cv
import PIL
import re
from pytesseract import image_to_string, pytesseract

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def ocr_text_image(img_path, debug = False):
    img = cv.imread(img_path)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    print('Performing Character Recognition')
    otsu_thresh_image = PIL.Image.fromarray(gray_img)
    
    image_text = clean_string(image_to_string(otsu_thresh_image))
    if(debug):
        write_to_disk('test1', image_text)
        
    return image_text

def clean_string(text):
    # Remove header
    poster_id_index = text.find('No.')
    text = text[text.find('\n', poster_id_index):]

    # Remove file and image formatting
    file_line_index = text.find('File:')
    if(file_line_index != -1):
        text = text[file_line_index+1:]
    else:
        img_file_regex = r'\d*\s?(KB|MB)\s?(JPEG|PNG|JPG)'
        text = re.sub(img_file_regex, '', text)

    # Remove user IDs
    user_id_regex = r'=?[>=]\d{9}\d?'
    text = re.sub(user_id_regex, '', text)

    # Replace specific characters, improving TTS
    replace_chars = ['|', 'I']
    remove_chars = '>�'
    trans_table = str.maketrans(replace_chars[0], replace_chars[1], remove_chars)
    text = text.translate(trans_table)
    
    return text

def write_to_disk(file_name, text):
    with open('./%s.txt'%file_name, 'w') as f:
        f.write(text)
