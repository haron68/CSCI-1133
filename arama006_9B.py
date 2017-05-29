def classify(object, object1, object2):
    dictionary = {"literature": [],"government": []}
    wordCountDict  = {"literature": 0, "government": 0}

    words = object.split('\n')
    words1 = object1.split(' ')
    words2 = object2.split(' ')

    for i, word in enumerate(words):
        word = word.lower()

        for j, word1 in enumerate(words1):
            word1 = word1.lower()

            if word == word1:
                wordCountDict['literature'] += 1

        for k, word2 in enumerate(words2):
            word2 = word2.lower()

            if word == word2:
                wordCountDict['government'] += 1

        if wordCountDict['literature'] < wordCountDict['government']:
            dictionary['literature'].append(word)
        elif wordCountDict['literature'] > wordCountDict['government']:
            dictionary['government'].append(word)
        elif wordCountDict['literature'] == wordCountDict['government'] and (wordCountDict['literature'] + wordCountDict['government']) != 0:
            dictionary['literature'].append(word)
            dictionary['government'].append(word)

        wordCountDict['literature'] = 0
        wordCountDict['government'] = 0
    print(dictionary)

fhWordFile = open("wordFile.txt", "r", encoding="UTF-8")
fhFederalist = open("Federalist.txt", "r", encoding="UTF-8")
fhJaneEyre = open("JaneEyre.txt", "r", encoding="UTF-8")

wordFile = fhWordFile.read()
fedChar = fhFederalist.read()
janeChar = fhJaneEyre.read()

classify(wordFile, fedChar, janeChar)