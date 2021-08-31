# required libraries:
# beautufulsoup4, requests, lxml, googletrans

# DONE add Google Translate
# TODO write all in the text file (inside Dropbox folder?)
# DONE remove "Username" in the beginning of each article

from typing import List
from googletrans import Translator
from bs4 import BeautifulSoup
import requests


def main():
    source = requests.get('https://www.giga.de/games/').text
    soup = BeautifulSoup(source, 'lxml')

    # display the article headline
    print(soup.find('a', class_='alice-teaser-link').getText(), '\n')
    
    link = soup.find('a', class_='alice-teaser-link').get('href')

    # follow the link to the first article on the main page
    articlePage = requests.get('https:' + link).text
    articleSoup = BeautifulSoup(articlePage, 'lxml')
    articleText = ""

    for paragraph in articleSoup.find_all('p'):
        articleText += paragraph.getText()


    articleText = articleText.removeprefix('Username')

    # create a list of paragraphs, then slpit on sentences
    paragraphList = articleText.split('\n')

    for i in range(len(paragraphList)-1, 2, -1):
        del paragraphList[i]

    for i in range(len(paragraphList)-1):
        sentenceList = paragraphList[i].split('. ')
        translate(textOnGerman=sentenceList)


def translate(textOnGerman):
    translator = Translator()

    for i in range(len(textOnGerman)-1):
        translation = translator.translate(textOnGerman[i], src = 'de', dest ='en')

        print(textOnGerman[i], '\n(', translation.text, ')')
        print()


if __name__ == '__main__':
    main()
