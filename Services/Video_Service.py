import cv2
from ffpyplayer.player import MediaPlayer

def create_video(input_name, title = None):
    img = cv2.imread('./Input/Images/grandad_fishing.png')
    height, width, layer = img.shape
    
    title = '%s_video'%input_name if title is None else title
    video = cv2.VideoWriter('./Output/Videos/%s.avi'%title, 0, 1, (width,height))
    video.write(img)

    cv2.destroyAllWindows()
    video.release()
