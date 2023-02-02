from pydub import AudioSegment
from pytube import YouTube
import json


link = "https://www.youtube.com/watch?v=djV11Xbc914&list=RDMM&index=27"

# my_proxies = {
#     'https': 'https://46.8.213.29:5501',
#     'http': 'https://46.8.213.29:5501',
# }
# yt = YouTube(url=link)

yt = YouTube(
        url=link,
        # on_progress_callback=progress_func,
        # on_complete_callback=complete_func,
        # proxies=my_proxies,
        use_oauth=False,
        allow_oauth_cache=True
    )

# print(f'title: {yt.titlews}')e}')
# # print(f'views : {yt.vi
# print(f'author : {yt.author}')
# print(f'publish date : {yt.publish_date}')
# print(f'is age restricted : {yt.age_restricted}')
# print(f'thumbnail : {yt.thumbnail_url}\n')


for stream in yt.streams.filter(type="audio"):
    # print(stream)
    path = stream.download(output_path="data")
    print(path)
    sound = AudioSegment.from_file(path, format="m4a")
# print(yt.streams)

