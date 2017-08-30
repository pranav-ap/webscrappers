#extracts all email addresses from the webpage

from bs4 import BeautifulSoup
from pprint import pprint
import re
import requests


def extract(url):
    emails = []
    try:
        response  = requests.get(url)
        data = response.text

    except requests.exceptions.Timeout:
        print("The server didn't respond. Please, try again later.")

    soup = BeautifulSoup(data, 'lxml')
    # print(soup.encode("utf-8"))
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", soup.encode("utf-8").decode("utf-8"))
    
    return emails


def main():
    url = 'https://en.wikipedia.org/wiki/Email_address'
    emails = extract(url)

    pprint(emails)


if __name__ == '__main__':
    main()
