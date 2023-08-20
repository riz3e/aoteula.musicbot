import yt_dlp
from mutagen.id3 import ID3, TIT2, TPE1, APIC
from moviepy.editor import *

from thumbnail import download_preview


def normalize_filename(filename: str) -> str:
    illegal_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    normalized_filename = ''.join(['_' if char in illegal_characters else char for char in filename])
    return normalized_filename


class audio:
    def __init__(self, url: str):
        ydl_opts = {
            'format': 'bestaudio/best',
            'ffprobe_location': os.path.realpath(r"C:\Program Files\ffmpeg\bin\ffprobe.exe"),
            'ffmpeg_location': os.path.realpath(r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"),
            # вот это не трогать, которая ffmpeg
            # иначе не найдешь след раз
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
            print(thumbnail)
        title = normalize_filename(title)
        author = normalize_filename(author)
        ydl_opts['outtmpl'] = f'data/{title} - {author} - aoteulabot'  # Video title
        with yt_dlp.YoutubeDL(params=ydl_opts) as ydl:
            ydl.download([url])

        download_path = f'data/{title} - {author} - aoteulabot.mp3'
        try:
            thumb_dir = download_preview(url=thumbnail, title=f"{title} - {author}")
        except:
            thumb_dir = "errorthing"
        audiofile = ID3()
        audiofile["TIT2"] = TIT2(encoding=3, text=title)  # setting the title
        audiofile["TPE1"] = TPE1(encoding=3, text=author)  # setting the author

        if thumb_dir != "errorthing":
            audiofile["APIC"] = APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover',  # setting the thumbnail
                                     data=open(thumb_dir, 'rb').read())

        audiofile.save(download_path)

        self.download_path = download_path
        self.thumbnail = thumb_dir  # link to the thumbnail
        self.duration = duration


def main():
    print(audio(input("Enter an URL ")).download_path)
    # check_tags()


if __name__ == "__main__":
    main()
