import cv2 as cv
import re
from pytesseract import image_to_string, pytesseract, Output

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def __run__(img_path, debug = False):
    img = cv.imread(img_path)
    processed_img = pre_process_img(img)
    img_text = ocr_text_image(processed_img, debug)
    boundary_boxes_on_text(img)
    if(debug == True):
        show_image(processed_img)

    return [(img_text,img)]

def pre_process_img(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
    
    return thresh

def boundary_boxes_on_text(img):
    results = pytesseract.image_to_data(img, output_type=Output.DICT) 

    for i in range(0, len(results["text"])):
        # extract the bounding box coordinates of the text region from results
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    show_image(img)

def ocr_text_image(img, debug):
    print('Performing Character Recognition')    
    image_text = clean_string(image_to_string(img))
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

    # Remove empty lines
    text = "".join([s for s in text.strip().splitlines(True) if s.strip()])
    
    return text

def write_to_disk(file_name, text):
    with open('./Output/Temp/Text/%s.txt'%file_name, 'w') as f:
        f.write(text)

def show_image(img):
    cv.imshow("Display Window", img)
    cv.waitKey(0)

__run__('./Input/Images/test_1.jpg', True)