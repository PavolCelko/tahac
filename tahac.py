from pytube import YouTube

# link = 'https://www.youtube.com/watch?v=GB3RGu8Go2s&t=36s'
link = 'https://youtu.be/ay9MSPUKoNg'

yt = YouTube(link)

streams_list = yt.streams.all()

for st in streams_list:
    if "audio/mp" in st.mime_type:
        audio_stream = st

audio_stream.download(filename="ytfile")

print "DOWNLOAD finished"
