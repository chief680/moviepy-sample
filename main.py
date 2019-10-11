from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, ImageClip, CompositeVideoClip, TextClip

txtClip1 = TextClip('This is a Picture 2sec',color='white', font="Amiri-Bold",
                   kerning = 5, fontsize=48).set_pos('center')
clip1 = ImageClip('1.jpg', duration=2)
cc1 = CompositeVideoClip([clip1, txtClip1]).set_duration(2)

txtClip2 = TextClip('This is a Video 10sec',color='white', font="Amiri-Bold",
                   kerning = 5, fontsize=48).set_pos('center')
clip2 = VideoFileClip('2.mp4').subclip(10,20)
cc2 = CompositeVideoClip([clip2, txtClip2]).set_duration(10)

txtClip3 = TextClip('This is a Picture 5sec',color='white', font="Amiri-Bold",
                   kerning = 5, fontsize=48).set_pos('center')
clip3 = ImageClip('3.jpg', duration=5)
cc3 = CompositeVideoClip([clip3, txtClip3]).set_duration(5)

clip4 = VideoFileClip('4.mp4')
txtClip4 = TextClip('This is a Video Any sec',color='white', font="Amiri-Bold",
                   kerning = 5, fontsize=48).set_pos('center')
cc4 = CompositeVideoClip([clip4, txtClip4]).set_duration(clip4.duration)


clip = concatenate_videoclips([cc1,cc2,cc3,cc4])
audio = AudioFileClip('music.mp3').subclip(0,clip.duration)
finalclip = clip.set_audio(audio)
clip480 = finalclip.resize(width=480)
clip480.write_videofile('clip480.mp4', fps=24)

clip720 = finalclip.resize(width=720)
clip720.write_videofile('clip720.mp4',fps=24)
