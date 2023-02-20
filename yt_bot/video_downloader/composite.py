from moviepy.editor import *
from search import *


clip = VideoFileClip("/home/mircous/Downloads/gitytbot/yt_bot/video_downloader/854288.mp4").subclip(5, 7)
sec_clip = VideoFileClip("/home/mircous/Downloads/gitytbot/yt_bot/video_downloader/"+ id()).subclip(5, 7)

final = concatenate_videoclips([sec_clip, clip])

final.write_videofile("edited_video.mp4")
