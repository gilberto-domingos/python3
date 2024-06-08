append = open('files/word-texts.txt', 'a')

append.write("cada cidade possui muitas ruas.")

append.close()

'''
with open('files/word-texts.txt', 'r') as r:
    line_number = 0

    for line in r:
        line_number += 1

        if line_number == 3:
            print(line)
            break

r.close()
'''
'''
r = open("files/word-texts.txt", "r")
# print(r.read())

    # line = r.readline()
    # print(line)

        for line in r:
        print(line)
'''
