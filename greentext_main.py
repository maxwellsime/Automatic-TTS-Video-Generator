from Services.OCR_Service import ocr_text_image
from Services.TTS_Service import tts_from_string
from Services.Video_Service import create_video

def __run__():
    img_name = 'grandad_fishing'
    img_path = './Input/Images/%s.png'%img_name
    image_text = ocr_text_image(img_path)
    tts_from_string(image_text, img_name)
    create_video(img_name)

__run__()
