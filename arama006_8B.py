def findClosest(firstColorList, color):
    colorName = []
    c_list    = []
    d_List    = []

    for i in range(0, len(firstColorList)):
        colorName.append(firstColorList[i][3])

    for j in range(0, len(firstColorList)):
        r1 = int(firstColorList[j][0])
        g1 = int(firstColorList[j][1])
        b1 = int(firstColorList[j][2])
        r2 = int(color[0])
        g2 = int(color[1])
        b2 = int(color[2])

        distance = (((r2 - r1)**2) + ((g2 - g1)**2) + ((b2 - b1)**2))**(0.5)
        d_List.append(distance)

    for j in range(0, len(d_List)):
        if min(d_List) == d_List[j]:
            c_list.append(colorName[j])

    return '{:.2f} {}'.format(min(d_List), c_list)

with open('xcolorsB_old.txt') as xcolorsB:
    xcolorsB = xcolorsB.read()

with open('testColors_old.txt') as testColors:
    testColors = testColors.read()

xcolorsB      = xcolorsB.split('\n')
xcolorsB_list = []

for i in range(0, len(xcolorsB)):
    xcolorsB_list.append(xcolorsB[i].split(','))

testColors        = testColors.split('\n')
testColors_list   = []

for i in range(0, len(testColors)):
    testColors_list.append(testColors[i].split())

xcolorsB_list.remove([''])
testColors_list.remove([])

x = xcolorsB_list

for i in range(0, len(testColors_list)):
   print(findClosest(x, testColors_list[i]))