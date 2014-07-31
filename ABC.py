from __future__ import print_function
from random import randrange


def execute(string):
    acc = 0
    asc = False
    j = 0
    while j in range(len(string)):
        i = string[j]
        if i == 'a':
            acc += 1
        elif i == 'b':
            acc -= 1
        elif i == 'c':
            if asc:
                try:
                    print(chr(acc),end="")
                except: pass
            else:
                print(acc,end="")
        elif i == 'd':
            acc = -acc
        elif i == 'r':
            acc = randrange(0,acc+1)
        elif i == 'n':
            acc = 0
        elif i == '$':
            asc = not asc
        elif i == 'l':
            j = -1
        elif i == ';':
            try:
                print(chr(acc),end="")
            except: pass
            print(acc,end="")
        j += 1