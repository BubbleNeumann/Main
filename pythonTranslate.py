from googletrans import Translator
import codecs

translator = Translator()

inputFile = open("text.txt", 'r')
outputFile = codecs.open("translation.txt", 'w', 'utf-8')

for line in inputFile:

    sentences = line.split('.')

    for i in range(len(sentences)-1):

        translation = translator.translate(sentences[i], src = 'en', dest ='ru')

        outputFile.write(sentences[i] + " (" + translation.text + ").\n")

inputFile.close()
outputFile.close()
