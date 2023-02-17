from moviepy.editor import *
from search import *

clip = VideoFileClip("854982.mp4").subclip(5, 7)
sec_clip = VideoFileClip("855282.mp4").subclip(5, 7)

final = concatenate_videoclips([sec_clip, clip])

final.write_videofile("edited_video.mp4")
