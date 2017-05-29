def main():
    try:
        j = open('j.txt', 'r').read()
    except FileNotFoundError:
        print('fuck you')
    #j = open('fuck', 'r')


main()