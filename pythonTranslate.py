# pip install googletrans

from googletrans import Translator

# supports cyrillics, needed for Russian lang
import codecs

translator = Translator()


# two files needed: (1) text.txt - source file, (2) translatoin.txt - the result
inputFile = open("text.txt", 'r')
outputFile = codecs.open("translation.txt", 'w', 'utf-8')

for line in inputFile:

    sentences = line.split('.')

    for i in range(len(sentences)-1):

        # supports translations from English to Russian (use 'de' for German)
        translation = translator.translate(sentences[i], src = 'en', dest ='ru')

        outputFile.write(sentences[i] + " (" + translation.text + ").\n")

inputFile.close()
outputFile.close()
