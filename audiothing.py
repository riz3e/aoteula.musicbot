import pytube
from mutagen.id3 import ID3, TIT2, TPE1, APIC
from moviepy.editor import *


class audio:
    def __init__(self, url):
        vid = pytube.YouTube(url,
                             use_oauth=True,
                             allow_oauth_cache=True
                             )
        stream = vid.streams.filter(only_audio=True).first()
        download_path = stream.download(output_path="data")
        # print(download_path)
        duration = vid.length
        BasePath, ext = os.path.splitext(download_path)
        FILETOCONVERT = AudioFileClip(download_path)
        download_path = BasePath + ".mp3"
        FILETOCONVERT.write_audiofile(download_path)
        FILETOCONVERT.close()
        audio = ID3()
        audio["TIT2"] = TIT2(encoding=3, text=vid.title)
        audio["TPE1"] = TPE1(encoding=3, text=vid.author)
        audio.save(download_path)

        self.download_path = download_path
        self.thumbnail_url = vid.thumbnail_url
        self.duration = duration

    # def duration(self):
    #     return self.duration
    #
    # def thumbnail_url(self):
    #     return self.thumbnail_url
    #
    # def download_path(self):
    #     return self.download_path


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
