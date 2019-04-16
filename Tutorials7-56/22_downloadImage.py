import random
import urllib.request


def download_web_image(url_image):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpeg'
    urllib.request.urlretrieve(url_image, full_name)


try:
    download_web_image(r"https://www.python.org/static/community_logos/python-logo-master-v3-TM.png")
except Exception as e:
    print('Image could not be downloaded ', e)

