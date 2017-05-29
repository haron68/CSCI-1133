from collections import OrderedDict

def wordRepition(sentence):
    counter = OrderedDict()
    words = sentence.split(' ')
    for i, word in enumerate(words):
        word = word.lower()
        if word not in counter:
            counter[word] = []
        counter[word].append(i)
    for word in counter:
        print(word, " ".join(map(str , counter[word])))

sentence = input("Input the sentence: ")
wordRepition(sentence)

i = 0
j = 1
while i < j:
    cont = input("Do you wish to input another sentence (y/n)? ")
    if cont == 'y':
        sentence = input("Input the sentence: ")
        wordRepition(sentence)
        i += 1
        j += 1
    elif cont == 'n':
        break
