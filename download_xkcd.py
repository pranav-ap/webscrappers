#Downloads every single XKCD comic.

import os
import requests
from bs4 import BeautifulSoup

page_url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not page_url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % page_url)

    response = requests.get(page_url)
    response.raise_for_status()
    # print(response.text)

    soup = BeautifulSoup(response.text, 'lxml')

    # Find the URL of the comic image.
    comic_element = soup.select('#comic img')
    if comic_element is []:
        print('Could not find comic image.')
    else:
        comic_url = comic_element[0].get('src')
        print('Downloading image %s...' % comic_url)
        response = requests.get('http:' + comic_url)
        response.raise_for_status()

        # Save the image to ./xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')

        for chunk in response.iter_content(100000):
            image_file.write(chunk)

        image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    page_url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')
