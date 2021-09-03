# required libraries:
# beautufulsoup4, requests, lxml, googletrans

# DONE add Google Translate
# TODO write all in the text file (inside Dropbox folder?)
# DONE remove "Username" in the beginning of each article
# DONE add ability to choose the source of an article (add another resource)


from googletrans import Translator
from bs4 import BeautifulSoup
import requests
from enum import IntEnum


class SitesToParse(IntEnum):
    GIGA_GAMES = 0
    GAME_STAR = 1


def main():
    userInput = int(input(list(SitesToParse)))

    if userInput == SitesToParse.GIGA_GAMES:
            parseGigaGames()
    elif userInput == SitesToParse.GAME_STAR:
            parseGameStar()


def parseGigaGames():
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


def parseGameStar():
    source = requests.get('https://www.gamestar.de/').text
    soup = BeautifulSoup(source, 'lxml')

    # find a good link to the article
    for link in soup.find_all('a', class_='js-ga'):
        if link.get('title') != None and link.get('data-category') == 'Home':
            break

    # display headline
    print(link.getText())

    # follow the link to the first article on the main page
    articlePage = requests.get('https://www.gamestar.de' + link.get('href')).text
    articleSoup = BeautifulSoup(articlePage, 'lxml')
    articleText = ""

    for paragraph in articleSoup.find_all('p'):
        articleText += paragraph.getText()

    paragraphList = articleText.split('\n')

    for i in range(0, len(paragraphList)//2):
        if len(paragraphList[i])<40:
            del paragraphList[i]

    for i in range(len(paragraphList)-1, 0, -1):
        if len(paragraphList[i])<40:
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
