from bs4 import BeautifulSoup
import requests

try:
  url = 'https://en.wikipedia.org/wiki/Main_Page'

  response  = requests.get(url)
  data = response.text

except requests.exceptions.Timeout:
    print("The server didn't respond. Please, try again later.")

soup = BeautifulSoup(data, 'lxml')

for link in soup.find_all('a'):
    if link.has_attr('href'):
        print(link.get('href'))
