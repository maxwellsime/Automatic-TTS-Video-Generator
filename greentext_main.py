from Services.OCR_Service import ocr_text_image
from Services.TTS_Service import tts_from_string

def __run__():
    img_name = 'test_1'
    img_path = './Images/%s.jpg'%img_name
    print(img_path)
    image_text = ocr_text_image(img_path)
    tts_from_string(image_text, img_name)

__run__()
