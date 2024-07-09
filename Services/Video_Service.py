import cv2
import moviepy.editor as mp

def create_video(input_name, title = None):
    title = '%s_video'%input_name if title is None else title
    img = cv2.imread('./Input/Images/%s.png'%input_name)
    height, width, layer = img.shape

    video_path = './Output/Temp/Videos/%s.avi'%title
    audio_path = './Output/Temp/Audio/%s.wav'%input_name
    output_path = './Output/%s.mp4'%title

    video = cv2.VideoWriter(video_path, 0, 1, (width,height))
    video.write(img)
    cv2.destroyAllWindows()
    video.release()

    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(audio_path)
    video = video.set_audio(audio)
    video.write_videofile(output_path)
