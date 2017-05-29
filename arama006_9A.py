fhFederalist = open("Federalist.txt", "r", encoding="UTF-8")

fhJaneEyre = open("JaneEyre.txt", "r", encoding="UTF-8")

dictFederalist = {'.': 0, ',': 0, ';': 0, '(': 0, ')': 0, '"': 0, '?': 0, '-': 0, ':': 0}

dictJaneEyre = {'.': 0, ',': 0, ';': 0, '(': 0, ')': 0, '"': 0, '?': 0, '-': 0, ':': 0}

fedChar = fhFederalist.read()

janeChar = fhJaneEyre.read()

for i in range(0, len(fedChar)):
    if   fedChar[i] == '.':
        dictFederalist['.'] += 1
    elif fedChar[i] == ',':
        dictFederalist[','] += 1
    elif fedChar[i] == ';':
        dictFederalist[';'] += 1
    elif fedChar[i] == '(':
        dictFederalist['('] += 1
    elif fedChar[i] == ')':
        dictFederalist[')'] += 1
    elif fedChar[i] == '"':
        dictFederalist['"'] += 1
    elif fedChar[i] == '?':
        dictFederalist['?'] += 1
    elif fedChar[i] == '-':
        dictFederalist['-'] += 1
    elif fedChar[i] == ':':
        dictFederalist[':'] += 1

for i in range(0, len(janeChar)):
    if   janeChar[i] == '.':
        dictJaneEyre['.'] += 1
    elif janeChar[i] == ',':
        dictJaneEyre[','] += 1
    elif janeChar[i] == ';':
        dictJaneEyre[';'] += 1
    elif janeChar[i] == '(':
        dictJaneEyre['('] += 1
    elif janeChar[i] == ')':
        dictJaneEyre[')'] += 1
    elif janeChar[i] == '"':
        dictJaneEyre['"'] += 1
    elif janeChar[i] == '?':
        dictJaneEyre['?'] += 1
    elif janeChar[i] == '-':
        dictJaneEyre['-'] += 1
    elif janeChar[i] == ':':
        dictJaneEyre[':'] += 1

width = 10
print('.{0: >{width}}{1: >{width}}'.format(dictFederalist['.'], dictJaneEyre['.'], width=width))
print(',{0: >{width}}{1: >{width}}'.format(dictFederalist[','], dictJaneEyre[','], width=width))
print(';{0: >{width}}{1: >{width}}'.format(dictFederalist[';'], dictJaneEyre[';'], width=width))
print('({0: >{width}}{1: >{width}}'.format(dictFederalist['('], dictJaneEyre['('], width=width))
print('){0: >{width}}{1: >{width}}'.format(dictFederalist[')'], dictJaneEyre[')'], width=width))
print('"{0: >{width}}{1: >{width}}'.format(dictFederalist['"'], dictJaneEyre['"'], width=width))
print('?{0: >{width}}{1: >{width}}'.format(dictFederalist['?'], dictJaneEyre['?'], width=width))
print('-{0: >{width}}{1: >{width}}'.format(dictFederalist['-'], dictJaneEyre['-'], width=width))
print(':{0: >{width}}{1: >{width}}'.format(dictFederalist[':'], dictJaneEyre[':'], width=width))