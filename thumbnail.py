import requests
from PIL import Image


# to attach thumbnail to the audiofile
# для того, чтобы получить превью для аудиофайла


def normalizethumb(thumb_dir):  # cropping the image to 1:1 to attach to the audio
    try:
        with Image.open(thumb_dir) as img:
            width, height = img.size

            # Calculate the size of the square crop
            size = min(width, height)

            # Calculate the cropping box to center the image
            left = (width - size) // 2
            top = (height - size) // 2
            right = (width + size) // 2
            bottom = (height + size) // 2

            # Crop and save the image
            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save(thumb_dir)
            print("Image cropped successfully.")
    except Exception as e:
        print(f"Error cropping image: {e}")


def download_preview(url, title="kek"):  # url of thumbnail, not a video
    try:
        req = requests.get(url)
        ext = url.split('.')[-1]
        thumb_dir = f"data/thumbnails/{title}.{ext}"
        with open(thumb_dir, "wb") as file:
            file.write(req.content)

        return thumb_dir
    except Exception as e:
        print(f"Error downloading image: {e}")


def main():
    # print("Getting thumbnail of video!")
    # download_preview(url=input("Enter URL of video which thumbnail you want to download: "))
    print("Normalizing thumbnail for uploading into telegram")
    link = input("Enter URL of video which thumbnail you want to download: ")
    normalizethumb(download_preview(url=link))


if __name__ == "__main__":
    main()
