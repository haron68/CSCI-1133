def difference(amountData, data, dV, average):
    oldList = [float(data) for data in data.split(' ', amountData)]
    j = 0
    outLier = []
    while j < amountData:
        if (average + dV) < oldList[j]:
            outLier += [oldList[j]]
        elif (average - dV) > oldList[j]:
            outLier += [oldList[j]]
        j += 1
    return outLier

def newDifference(amountData, data, average, dV):
    oldList = [float(data) for data in data.split(' ', amountData)]
    outLier = difference(amountData, data, dV, average)

    print("Outliers: ", str(outLier).strip('[]'))

    k = 0
    newList = oldList
    n = len(newList)
    while k < n:
        if (average + dV) < newList[k]:
            newList.remove(newList[k])
            n -= 1
        elif (average - dV) > newList[k]:
            newList.remove(newList[k])
            n -= 1
        k += 1

    l = 0
    listSum = 0
    newAverage = 0
    while l < len(newList):
        listSum += newList[l]
        newAverage = listSum / len(newList)
        l += 1

    newAverage = float("{0:.2f}".format(newAverage))
    print("Average excluding outliers: ", newAverage)

    newDV = input("Do you wish to input another difference (y/n)? ")

    if newDV == 'y':
        ndV = float(input("Input difference: "))
        newDifference(amountData, data, average, ndV)
    elif newDV == 'n':
        newData = input("Do you wish to input another data set (y/n)? ")
        if newData == 'y':
            amountDatas = int(input("How many data? "))
            datas = input("Input data values: ")
            outlier(amountDatas, datas)
        elif newData == 'n':
            print("")

def outlier(amountData, data):
    List = [float(data) for data in data.split(' ', amountData)]

    i = 0
    listSum = 0
    while i < len(List):
        listSum += List[i]
        average = listSum / len(List)
        i += 1

    average = float("{0:.2f}".format(average))
    print("Average: ", average)

    dV = float(input("Input difference: "))

    newDifference(amountData, data, average, dV)


amountData  = int(input("How many data? "))
data        = input("Input data values: ")
outlier(amountData, data)