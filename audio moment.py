import os
import pytube
from mutagen.id3 import ID3, TIT2, TPE1, APIC
from mutagen.mp3 import MP3


def video_to_audio(url):
    vid = pytube.YouTube(url)
    stream = vid.streams.filter(only_audio=True).first()
    download_path = stream.download(output_path="data")
    print(download_path)
    BasePath, ext = os.path.splitext(download_path)
    os.rename(download_path, BasePath+".mp3")
    audio = ID3(BasePath+".mp3")
    audio["TIT2"] = TIT2(encoding=3, text=vid.title)
    audio["TPE1"] = TPE1(encoding=3, text=vid.author)
    audio.save()
    # return

def check_tags():
    try:
        tags = ID3("data/Joji - Pretty Boy (ft Lil Yachty).mp3")
    except Exception as ex:
        tags = ID3()
        print(ex)

    tags.save("data/Joji - Pretty Boy (ft Lil Yachty).mp3")
    print(tags)

    tags["TIT2"] = TIT2(encoding=3, text="Pretty Boy TEST")
    tags["TPE1"] = TPE1(encoding=3, text="Joji TEST")
    print(tags)

    tags["APIC"] = APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=open('thumbnails/thumbnail_4989697.jpg', 'rb').read())
    tags.save("data/Joji - Pretty Boy (ft Lil Yachty).mp3")


def main():
    video_to_audio(input("Enter an URL "))
    # check_tags()
if __name__ == "__main__":
    main()