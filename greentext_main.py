from Services.OCR_Service import ocr_text_image
from Services.TTS_Service import tts_from_string
from Services.Video_Service import create_video

def __run__():
    img_name = 'test_1'
    img_path = './Input/Images/%s.jpg'%img_name
    print(img_path)
    image_text = ocr_text_image(img_path)
    tts_from_string(image_text, img_name)
    create_video()

__run__()
