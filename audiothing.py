import yt_dlp
from mutagen.id3 import ID3, TIT2, TPE1, APIC
from moviepy.editor import *

from thumbnail import download_preview


class audio:
    def __init__(self, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'ffprobe_location': os.path.realpath(r"C:\Program Files\ffmpeg\bin\ffprobe.exe"),
            'ffmpeg_location': os.path.realpath(r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"),
            # вот эту хуйню не трогать блять, которая ffmpeg
            # иначе хуй найдешь след раз
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'title - aoteulabot',  # Название выходного mp3 файла
        }

        with yt_dlp.YoutubeDL(params=ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # retrieving info about video and uses for metadata
            title = info_dict.get('title', '')
            author = info_dict.get('uploader', '')
            duration = info_dict.get('duration', 0)
            thumbnail = info_dict.get('thumbnail', '')

        ydl_opts['outtmpl'] = f'data/{title} - aoteulabot' # Video title
        with yt_dlp.YoutubeDL(params=ydl_opts) as ydl:
            ydl.download([url])

        download_path = f'data/{title} - aoteulabot.mp3'

        self.download_path = download_path
        self.thumbnail = thumbnail  # link to the thumbnail
        self.duration = duration

        thumb_dir = download_preview(url=thumbnail, title=f"{title} - {author}")

        audio = ID3()
        audio["TIT2"] = TIT2(encoding=3, text=title)
        audio["TPE1"] = TPE1(encoding=3, text=author)
        audio["APIC"] = APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover',
                            data=open(thumb_dir, 'rb').read())
        audio.save(download_path)


# def check_tags():
#     try:
#         tags = ID3("data/Joji - Pretty Boy (ft Lil Yachty).mp3")
#     except Exception as ex:
#         tags = ID3()
#         print(ex)
#
#     tags.save("data/Joji - Pretty Boy (ft Lil Yachty).mp3")
#     print(tags)
#
#     tags["TIT2"] = TIT2(encoding=3, text="Pretty Boy TEST")
#     tags["TPE1"] = TPE1(encoding=3, text="Joji TEST")
#     print(tags)
#
#     tags["APIC"] = APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover',
#                         data=open('thumbnails/thumbnail_4989697.jpg', 'rb').read())
#     tags.save("data/Joji - Pretty Boy (ft Lil Yachty).mp3")


def main():
    print(audio(input("Enter an URL ")).download_path)
    # check_tags()


if __name__ == "__main__":
    main()
