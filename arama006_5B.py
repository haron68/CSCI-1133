def match(sList, pList):
    sList = sList.format(' ', len(sList))
    pList = pList.format(' ', len(pList))

    i = 0
    while i < len(sList) - (len(pList) - 1):
        j = 0
        count = 0
        while j < len(pList):
            if sList[i + j] == pList[j]:
                count += 1

            if i == len(sList):
                break
            j += 1
        if count == 3:
            m = i + len(pList)
            print("Starting at position ", i + 1, ": one-character match with ", sList[i:m])
        i += 1

i = 0
j = 1
while i < j:
    S = input("Input the string to search: ")
    P = input("Input the pattern string: ")
    match(S, P)
    m = input("Do you wish to check another pair (y/n)? ")

    if m == 'y':
        j = 1
    elif m == 'n':
        break