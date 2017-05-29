# <replace this line with your name and x500 ID (e.g., John Smith smit1234>
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.

import sys

def rotate(l, n):
    return l[n:] + l[:n]

def encrypt(x,n):
    Astring = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    key = []
    jlist = []
    estring = ''
    for i in range(0,len(n)):
        for j in range(0,len(Astring)):
            if n[i] == Astring[j]:
                key.append(Astring[j:] + Astring[:j])
    for i in range(0,len(x)):
        for j in range(0,len(Astring)):
            if x[i] == Astring[j]:
                jlist.append(j)
    for i in range(0,len(jlist)):
        estring +=(key[0][jlist[i]])
        key = rotate(key,1)
    f = open(sys.argv[3], 'w')
    f.write(estring)
    print('encoded: ' + estring)

def decrypt(x,n):
    Astring = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    key = []
    estring = ''
    for i in range(0, len(n)):
        for j in range(0, len(Astring)):
            if n[i] == Astring[j]:
                key.append(Astring[j:] + Astring[:j])
    for i in range(0, len(x)):
        for j in range(0,len(Astring)):
            if x[i] == key[0][j]:
                estring += Astring[j]
        key = rotate(key,1)
    f = open(sys.argv[3], 'w')
    f.write(estring)
    print('decoded:' + ' ' + estring)

def main():
    try:
        j = open(sys.argv[2], 'r').read()
    except OSError:
        print('cannot open' + sys.argv[2])
    if sys.argv[1] == '-e':
        j = open(sys.argv[2], 'r').read()
        encrypt(j,sys.argv[4])
        f = open(sys.argv[3], 'w')
        f.write(estring)
    elif sys.argv[1] == '-d':
        j = open(sys.argv[2], 'r').read()
        decrypt(j,sys.argv[4])
        f = open(sys.argv[3], 'w')
        f.write(estring)
    else:
        print('Wrong input command')
if __name__ == '__main__':
    main()

j = open('j.txt', 'r').read()
decrypt(j,'BADboy')