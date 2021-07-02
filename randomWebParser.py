# required libraries:
# beautufulsoup4, requests, lxml


from bs4 import BeautifulSoup
import requests

# GIGA GAMES

source = requests.get('https://www.giga.de/games/').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

# list of the articles' headers

for article in soup.find_all('a', class_ = 'alice-teaser-link'):
  headline = article.text
  print(headline)
