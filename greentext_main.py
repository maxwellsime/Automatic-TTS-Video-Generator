from Services.OCR_Service import ocr_text_image
from Services.TTS_Service import tts_from_string

def __init__():
    #image_text = ocr_text_image("\Images\test.png")
    image_text = "Hello World"
    tts_from_string(image_text)
