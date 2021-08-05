import codecs
import random


def main():

    # put all questions for the exam in the 'questios.txt' file
    # Russian language is supported
    inputFile = codecs.open("questions.txt", 'r', 'utf-8')

    questionList = []

    for line in inputFile:
        questionList.append(line)

    # random.seed(a=None, version=2)
    print("Type 'ext' to exit the program\n")

    inp = ""
    while inp != "ext":
        print(questionList[random.randrange(len(questionList))])
        inp = input()

if __name__ == '__main__':
    main()
