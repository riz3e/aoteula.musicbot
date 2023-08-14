import random

import requests
from PIL import Image


# to attach thumbnail to the audiofile
# для того, чтобы получить превью для аудиофайла


def normalizethumb(thumb_dir):
    image = Image.open(thumb_dir)
    # image = image.crop((80, 0, 560, 480))
    image = image.crop((140, 60, 500, 420))
    image = image.resize((320, 320), Image.LANCZOS)
    image.save(thumb_dir)


def download_preview(url): # url of thumbnail, not a video
    req = requests.get(url)
    thumb_dir = f"thumbnails/хуй.jpg"
    # id = random.randint(0, 99999999)
    # thumb_dir = f"thumbnails/thumb_{id}.jpg"
    with open(thumb_dir, "wb") as file:
        file.write(req.content)
    # print(f"Ready! your thumbnail saved in thumbnails\thubnail_{id}.jpg")

    # normalizethumb(thumb_dir)

    return thumb_dir


def main():
    # print("Getting thumbnail of video!")
    # download_preview(url=input("Enter URL of video which thumbnail you want to download: "))
    print("Normalizing thumbnail for uploading into telegram")
    link = input("Enter URL of video which thumbnail you want to download: ")
    download_preview(url=link)


if __name__ == "__main__":
    main()
