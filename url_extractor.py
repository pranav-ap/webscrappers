from bs4 import BeautifulSoup
import requests

def extract(url):
    links = []
    try:
        response  = requests.get(url)
        data = response.text

    except requests.exceptions.Timeout:
        print("The server didn't respond. Please, try again later.")

    soup = BeautifulSoup(data, 'lxml')

    for link in soup.find_all('a'):
        if link.has_attr('href'):
            links.append(link.get('href'))
    
    print(links)


def main():
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    extract(url)


if __name__ == '__main__':
    main()
