#importing the module 
from pytube import YouTube 

link="https://www.youtube.com/watch?v=xobeTscjOM0"
  
video=YouTube(link)
# Reference
# https://towardsdatascience.com/the-easiest-way-to-download-youtube-videos-using-python-2640958318ab

# stream = yt.streams.first()
# stream.download()
# print(video.streams)
video.streams.get_by_itag(18).download()
# video.streams.get_audio_only(18)


