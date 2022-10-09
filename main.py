import cv2
import requests
import os

URL_zebra = "https://yandex.ru/images/search?text=zebra"
URL_bay_horse = "https://yandex.ru/images/search?text=bay%20horse"

if not os.path.isdir("dataset"):
    os.mkdir("dataset")
    if not os.path.isdir("zebra"):
        os.makedirs("dataset/zebra")
    if not os.path.isdir("bay_horse"):
        os.makedirs("dataset/bay_horse")








