import cv2 as cv
import re
import numpy as np
from pytesseract import image_to_string, pytesseract, Output

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

class image_service:

    _debug = False

    def __run__(self, img_path, debug = False):
        _debug = debug
        img = cv.imread(img_path)
        processed_img = self.pre_process_img()
        img_text = self.ocr_text_image()
        self.boundary_boxes_on_text()
        self.blur_section_of_image(200)

        if(_debug == True):
            self.show_image(processed_img)

        return [(img_text,img)]

    def pre_process_img(self):
        gray_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        thresh = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
        
        return thresh

    def boundary_boxes_on_text(self):
        results = pytesseract.image_to_data(self.img, output_type=Output.DICT) 

        if(self._debug == True):
            for i in range(0, len(results["text"])):
                # extract the bounding box coordinates of the text region from results
                x = results["left"][i]
                y = results["top"][i]
                w = results["width"][i]
                h = results["height"][i]
                cv.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def blur_section_of_image(self, blur_y):
        img_dimensions = self.img.shape
        blurred_img = cv.GaussianBlur(self.img, (21, 21), 0)
        mask = np.zeros(img_dimensions, dtype=np.uint8)
        mask = cv.rectangle(mask, (img_dimensions[1], blur_y), (0, 0), (255, 255, 255), -1)
        edited_img = np.where(mask==(255, 255, 255), self.img, blurred_img)
        
        return edited_img

    def ocr_text_image(self):
        print('Performing Character Recognition')    
        image_text = self.clean_string(image_to_string(self.img))

        if(self._debug):
            self.write_to_disk('test1', image_text)
            
        return image_text

    def clean_string(self, text):
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

    def write_to_disk(self, file_name, text):
        with open('./Output/Temp/Text/%s.txt'%file_name, 'w') as f:
            f.write(text)

    def show_image(self, img):
        cv.imshow("Display Window", img)
        cv.waitKey(0)

image_service().__run__('./Input/Images/test_1.jpg', True)
