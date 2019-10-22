from pytube import YouTube
import json

with open("list.json", "r") as read_file:
    videos_list = json.load(read_file)['videos']

for video in videos_list:
    if 'karpis-FED' in video['title']:
        link = video['link']

yt = YouTube(link)

streams_list = yt.streams.all()

for st in streams_list:
    if "audio/mp" in st.mime_type:
        audio_stream = st

audio_stream.download(filename="ytfile")

print "DOWNLOAD finished"
