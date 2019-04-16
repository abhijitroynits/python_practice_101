# A web crawler project to gather information from https://soundcloud.com/

import requests
from bs4 import BeautifulSoup


def music_spider(band_list):
    try:
        print('Fetching data from Soundcloud...\n')
        for band in band_list:
            url = 'https://soundcloud.com/search?q=' + band
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            for link in soup.find_all("ul"):
                for item in link.find_all("h2"):
                    # print(item.next_element.next_element)
                    print(item.string)
    except Exception as e:
        print("Oops! Connection not established: ", e)


music_spider(['iron maiden', 'metallica', 'megadeth', 'kreator'])
