import hw7Tests

def recursion(test_list):
    if type(test_list) == float:
        return test_list
    elif len(test_list) == 1:
        return recursion(test_list[0])
    elif len(test_list) == 0:
        return 0
    else:
        summation = 0
        for i in range(len(test_list)):
            summation += recursion(test_list[i])

        average = summation / len(test_list)
        return average

for testList in hw7Tests.tests:
    averagedList   = []
    for element in testList:
        averagedList.append(recursion(element))
    print(averagedList)