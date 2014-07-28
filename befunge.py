from random import choice
from time import sleep
import getopt
import sys


def execute(m, debug, visual, slow):
    m = m.split("\n")
    for i in range(len(m)):
        m[i] = [(ord(x)) for x in m[i]]
    for i in range(len(m)):
        m[i] = [(m[i][x] if x < len(m[i]) else 32) for x in range(max([len(k) for k in m]))]
    x = 0
    y = 0
    storeoffset = [0,0]
    stackstack = [[], []]
    stringmode = False
    skipcounter = 0
    repeatcounter = 0
    tempdelta = [0, 1]
    delta = [0, 1]
    outputstring = ''
    skipping = False
    def pop():
        return stackstack[-1].pop() if stackstack[-1] != [] else 0
    def push(x):
        stackstack[-1].append(x)
    while True:
        if skipcounter != 0:
            y = (y + skipcounter * delta[0]) % len(m)
            x = (x + skipcounter * delta[1]) % len(m[y])
            skipcounter = 0
        if chr(m[y][x]) == ' ':
            if stringmode:
                push(32)
            while chr(m[y][x]) == ' ':
                if x + delta[1] not in range(0, len(m[y])) or y + delta[0] not in range(0, len(m)):
                    delta = [-x for x in delta]
                    while x + delta[1] in range(0, len(m[y])) and y + delta[0] in range(0, len(m[y])):
                        x += delta[1]
                        y += delta[0]
                        if debug:
                            temp2 = m[y][x]
                            m[y][x] = ord('\\') if delta[1] == -delta[0] else ord('|') if abs(delta[1]) > abs(delta[0]) else ord("-") if abs(delta[1]) < abs(delta[0]) else ord('/')
                            print(str(''.join([''.join([chr(i) for i in k] + ['\n']) for k in m])))
                            m[y][x] = temp2
                    delta = [-x for x in delta]
                else:
                    x += delta[1]
                    y += delta[0]
        if not stringmode:
            if repeatcounter > 0:
                repeatcounter -= 1
                delta = [0, 0]
                if repeatcounter == 0:
                    delta = tempdelta
            if chr(m[y][x]) == '>':
                delta = [0, 1]
            elif chr(m[y][x]) == '<':
                delta = [0, -1]
            elif chr(m[y][x]) == '^':
                delta = [-1, 0]
            elif chr(m[y][x]) == 'v':
                delta = [1, 0]
            elif chr(m[y][x]) == '"':
                stringmode = True
                firstturn = False
            elif chr(m[y][x]) == ',':
                a = chr(pop())
                print(a, end="")
                outputstring += a
            elif chr(m[y][x]) == '.':
                a = pop()
                print(a, end="")
                outputstring += str(a)
            elif chr(m[y][x]) == '?':
                delta = choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
            elif chr(m[y][x]) in [str(hex(x))[2:] for x in range(0, 16)]:
                push(int('0x' + str(chr(m[y][x])), 16))
            elif chr(m[y][x]) == '#':
                skipcounter = 1
            elif chr(m[y][x]) == 'j':
                skipcounter = pop()
            elif chr(m[y][x]) == 'k':
                tempdelta = delta
                repeatcounter = pop() + 1
            elif chr(m[y][x]) == '+':
                b = pop()
                a = pop()
                push(a+b)
            elif chr(m[y][x]) == '-':
                b = pop()
                a = pop()
                push(a-b)
            elif chr(m[y][x]) == '*':
                b = pop()
                a = pop()
                push(a*b)
            elif chr(m[y][x]) == '/':
                b = pop()
                a = pop()
                push(a//b if b != 0 else 0)
            elif chr(m[y][x]) == '%':
                b = pop()
                a = pop()
                push(a % b if b != 0 else 0)
            elif chr(m[y][x]) == '\\':
                b = pop()
                a = pop()
                push(b)
                push(a)
            elif chr(m[y][x]) == "'":
                push(m[y+delta[0]][x+delta[1]])
                skipcounter = 1
            elif chr(m[y][x]) == '$':
                pop()
            elif chr(m[y][x]) == ':':
                a = pop()
                push(a)
                push(a)
            elif chr(m[y][x]) == 'n':
                stackstack[-1].clear()
            elif chr(m[y][x]) == 'g':
                a = pop()
                b = pop()
                push(m[a + storeoffset[0]][b + storeoffset[1]] if a < len(m) and b < m[a][b] else 0)
            elif chr(m[y][x]) == 'p':
                a = pop()
                b = pop()
                c = pop()
                good = False
                while not good:
                    try:
                        m[a + storeoffset[0]][b + storeoffset[1]] = c
                        good = True
                        for i in range(len(m)):
                            m[i] = [(m[i][x] if x < len(m[i]) else 0) for x in range(max([len(k) for k in m]))]
                    except:
                        while a >= len(m):
                            m.append([0 for x in m[0]])
                        while b >= len(m[a]):
                            m[a].append(0)
            elif chr(m[y][x]) == '!':
                a = pop()
                if a == 0:
                    a = 1
                else:
                    a = 0
                push(a)
            elif chr(m[y][x]) == '`':
                a = pop()
                b = pop()
                push(0 if a >= b else 1)
            elif chr(m[y][x]) == '_':
                a = pop()
                if a != 0:
                    delta = [0, -1]
                else:
                    delta = [0, 1]
            elif chr(m[y][x]) == '|':
                a = pop()
                if a != 0:
                    delta = [1, 0]
                else:
                    delta = [-1, 0]
            elif chr(m[y][x]) == '[':
                delta[0] = -delta[1]
                delta[1] = delta[0]
            elif chr(m[y][x]) == ']':
                delta[1] = -delta[0]
                delta[0] = delta[1]
            elif chr(m[y][x]) == 'x':
                a = pop()
                b = pop()
                delta = [b, a]
            elif chr(m[y][x]) == '&':
                good = False
                while not good:
                    a = input("Input a number:\n")
                    intstr = ""
                    for i in range(len(a)):
                        if a[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            intstr += a[i]
                            i += 1
                            while i < len(a) and a[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                intstr += a[i]
                                i += 1
                            break
                    try:
                        push(int(intstr))
                        good = True
                    except:
                        good = False
            elif chr(m[y][x]) == '~':
                try:
                    for i in input():
                        push(ord(i))
                except:
                    push(10)
            elif chr(m[y][x]) == 'w':
                a = pop()
                b = pop()
                if a > b:
                    delta[0] = -delta[1]
                    delta[1] = delta[0]
                elif a < b:
                    delta[1] = -delta[0]
                    delta[0] = delta[1]
            elif chr(m[y][x]) == 's':
                a = pop()
                try:
                    m[y+delta[0]][x+delta[1]] = a
                    for i in range(len(m)):
                            m[i] = [(m[i][x] if x < len(m[i]) else 0) for x in range(max([len(k) for k in m]))]
                except:
                    while a >= len(m):
                        m.append([0 for x in m[0]])
                    while b >= len(m[a]):
                        m[a].append(0)
            elif chr(m[y][x]) == '{':
                a = pop()
                try:
                    stackstack.append([])
                except MemoryError:
                    delta[0] = -delta[0]
                    delta[1] = -delta[1]
                else:
                    if a > 0:
                        stackstack[-1] = stackstack[-2][-a:len(stackstack[-2])] if len(stackstack[-2]) > a else [0 for x in range(len(stackstack[-2])-a)] + stackstack[-2]
                        stackstack[-2] = stackstack[-2][0:-a] if len(stackstack[-2]) > a else []
                        stackstack[-2].append(storeoffset[1])
                        stackstack[-2].append(storeoffset[0])
                    elif a < 0:
                        stackstack[-1] = []
                        for i in range(abs(a)):
                            stackstack[-1].append(0)
            elif chr(m[y][x]) == '}':
                if len(stackstack) > 1:
                    a = pop()
                    storeoffset = [stackstack[-2].pop(), stackstack[-2].pop()]
                    if a > 0:
                        stackstack[-2] = stackstack[-1][-a:] if len(stackstack[-2]) > a else [0 for x in range(len(stackstack[-2])-1)] + stackstack[-2]
                        stackstack.pop()
                    elif a < 0:
                        for i in range(abs(a)):
                            stackstack[-2].pop()
                        stackstack.pop()
                    else:
                        stackstack.pop()
                else:
                    delta[0] = -delta[0]
                    delta[1] = -delta[1]
            elif chr(m[y][x]) == 'u':
                a = pop()
                if len(stackstack) > 1:
                    if a > 0:
                        for i in range(a):
                            push(stackstack[-2].pop() if stackstack[-2] != [] else 0)
                    elif a < 0:
                        for i in range(a):
                            stackstack[-2].append(pop())
                else:
                    delta[0] = -delta[0]
                    delta[1] = -delta[1]
            elif chr(m[y][x]) == '@':
                break
            elif chr(m[y][x]) == 'z':
                True

        else:
            if chr(m[y][x]) != '"':
                push(m[y][x])
            else:
                stringmode = False
        firstturn = False
        m[y][x], temp = ord('.') if delta == [0, 0] else ord('\\') if delta[1] == -delta[0] else ord('|') if abs(delta[1]) > abs(delta[0]) else ord("-") if abs(delta[1]) < abs(delta[0]) else ord('/'), m[y][x]
        if visual:
            print("\n" * 10)
            stackstack[-1].reverse()
            print("Stack: ",end="")
            for i in stackstack[-1]:
                print("%s (%s) | " % (str(i),chr(i)),end="")
            print('\n')
            stackstack[-1].reverse()
            print("Script: \n%s" % str(''.join([''.join([chr(i) for i in k] + ['\n']) for k in m])))
            print("Output: " + outputstring)
            if debug:
                print("SOSS: ", end="")
                for i in stackstack[-2]:
                    print("%s (%s) | " % (str(i),chr(i)),end="")
                print("\nY: %i" % y)
                print("X: %i" % x)
                print("String Mode: " + str(stringmode))
                print("Character Executed: %s" % chr(temp))
                print("Loop counter (k): %i" % repeatcounter)
                print("Skip counter (j): %i" % skipcounter)
                print("Delta (y,x): " + str(delta))
                input()
            else:
                sleep(.2)
        if slow:
            if visual:
                sleep(.2)
        m[y][x] = temp
        if x + delta[1] not in range(0, len(m[y])) or y + delta[0] not in range(0, len(m)):
            delta = [-x for x in delta]
            while x + delta[1] in range(0, len(m[y])) and y + delta[0] in range(0, len(m[y])):
                x += delta[1]
                y += delta[0]
                if debug:
                    temp2 = m[y][x]
                    m[y][x] = ord('\\') if delta[1] == -delta[0] else ord('|') if abs(delta[1]) > abs(delta[0]) else ord("-") if abs(delta[1]) < abs(delta[0]) else ord('/')
                    print(str(''.join([''.join([chr(i) for i in k] + ['\n']) for k in m])))
                    m[y][x] = temp2
            delta = [-x for x in delta]
        else:
            x += delta[1]
            y += delta[0]

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hf:vds", ["file=", "visual", "debug", "slow"])
    inopts = False
    visual = False
    debug = False
    slow = False
    for opt, arg in opts:
        if opt in ['-f', '--file']:
            inopts = True
            try:
                f = open(arg).read()
            except:
                print("File not found.")
                sys.exit(0)
        elif opt in ['-v', '--visual']:
            visual = True
        elif opt in ['-d', '--debug']:
            debug = True
            visual = True
        elif opt in ['-s', '--slow']:
            slow = True
    if not inopts:
        print('befunge.py -f <befungefile>')
        sys.exit(2)
    execute(f, debug, visual, slow)