import cv2

def create_video(input_name, title, height = 1920, width = 1080):
    img = cv2.imread('%s.jpg'%input_name)
    video = cv2.VideoWriter('./Output/Videos/%s.avi'%title,-1,1,(width,height))
    video.write(img)        

    cv2.destroyAllWindows()
    video.release()
