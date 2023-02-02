import random

import pytube
import requests


# to attach thumbnail to the audiofile
# для того, чтобы получить превью для аудиофайла

def download_preview(url):
    vid = pytube.YouTube(url)
    # print(f"title: {vid.title}")
    # print(f"author: {vid.author}")
    # print(f"thumbnail url: {vid.thumbnail_url}\n")
    thumbnail_url = vid.thumbnail_url
    # print(vid.thumbnail_url)
    req = requests.get(thumbnail_url)
    id = str(random.randint(1000000, 9999999))
    thumb_dir = f"thumbnails/thumbnail_{id}.jpg"
    with open(thumb_dir, "wb") as file:
        file.write(req.content)
    # print(f"Ready! your thumbnail saved in thumbnails\thubnail_{id}.jpg")
    return thumb_dir


def main():
    print("Getting thumbnail of video!")
    download_preview(url=input("Enter URL of video which thumbnail you want to download: "))


if __name__ == "__main__":
    main()
