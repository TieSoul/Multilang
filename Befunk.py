from PIL import Image
import sys
import random

instrDict = dict((i, str(hex(i))[2:]) for i in range(16))
instrDict.update({50: '>',
                  51: '^',
                  52: 'v',
                  53: '<',
                  54: '_',
                  55: '|',
                  56: '[',
                  57: ']',
                  58: 'x',
                  59: 'w',
                  100: ',',
                  101: '.',
                  102: '&',
                  103: '~',
                  150: '+',
                  151: '-',
                  152: '*',
                  153: '/',
                  154: '%',
                  175: ':',
                  176: '\\',
                  200: '#',
                  201: 'j',
                  202: 'k',
                  256: '"',
                  300: 'g',
                  301: 'p',
                  302: "'",
                  303: 's',
                  350: '!',
                  351: '`',
                  400: '{',
                  401: '}',
                  402: 'u',
                  500: 'n',
                  501: '$',
                  554: 'z',
                  999: '@'})

delta = [0, 1]
x = 0
y = 0
stackstack = [[]]
stringmode = False
skipcounter = 0
origin = [0, 0]
storeoffset = [0, 0]
debug = False


def move(x, y):
    global m, delta
    if x + delta[1] not in range(0, len(m[y])) or y + delta[0] not in range(0, len(m)):
        delta = [-x for x in delta]
        while x + delta[1] in range(0, len(m[y])) and y + delta[0] in range(0, len(m[y])):
            x += delta[1]
            y += delta[0]
        delta = [-x for x in delta]
    else:
        x += delta[1]
        y += delta[0]
    return x, y


def push(x):
    stackstack[-1].append(x)


def pop():
    return stackstack[-1].pop() if stackstack[-1] != [] else 0


def exec(num):
    global y, x, delta, stringmode, skipcounter, storeoffset, origin, m
    if num == 555 and stringmode:
        push(555)
    while num == 555:
        x, y = move(x, y)
        num = m[y][x]
    if num == 556:
        x, y = move(x, y)
        num = m[y][x]
        while num != 556:
            x, y = move(x, y)
            num = m[y][x]
    if not stringmode:
        if num in range(16):
            push(num)
        elif num == 50:
            delta = [0, 1]
        elif num == 51:
            delta = [-1, 0]
        elif num == 52:
            delta = [1, 0]
        elif num == 53:
            delta = [0, -1]
        elif num == 54:
            delta = [0, 1] if pop() == 0 else [0, -1]
        elif num == 55:
            delta = [1, 0] if pop() == 0 else [-1, 0]
        elif num == 56:
            delta = [-delta[1], delta[0]]
        elif num == 57:
            delta = [delta[1], -delta[0]]
        elif num == 58:
            delta = [pop(), pop()]
        elif num == 59:
            a, b = pop(), pop()
            delta = [-delta[1], delta[0]] if a < b else [delta[1], -delta[0]] if a > b else delta
        elif num == 60:
            delta = random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
        elif num == 100:
            print(chr(pop() % 256), end="")
        elif num == 101:
            print(pop(), end="")
        elif num == 102:
            good = False
            while not good:
                a = input()
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
                    pass
        elif num == 103:
            try:
                for i in input():
                    push(ord(i))
            except:
                push(10)
        elif num == 150:
            push(pop() + pop())
        elif num == 151:
            a, b = pop(), pop()
            push(b - a)
        elif num == 152:
            push(pop() * pop())
        elif num == 153:
            a, b = pop(), pop()
            push(0 if a == 0 else b // a)
        elif num == 154:
            a, b = pop(), pop()
            push(0 if a == 0 else b % a)
        elif num == 175:
            a = pop()
            push(a); push(a)
        elif num == 176:
            a, b = pop(), pop()
            push(a); push(b)
        elif num == 200:
            skipcounter += 1
        elif num == 201:
            skipcounter += pop()
        elif num == 202:
            a = pop()
            if a > 0:
                i, j = move(x, y)
                while m[j][i] == 555:
                    i, j = move(i, j)
                for k in range(a):
                    exec(m[j][i])
            else:
                skipcounter += 1
        elif num == 256:
            stringmode = True
        elif num == 300:
            try: push(m[pop() + storeoffset[0] + origin[0]][pop() + storeoffset[1] + origin[1]])
            except IndexError: push(555)
        elif num == 301:
            a, b, c = pop(), pop(), pop()
            if a + storeoffset[0] + origin[0] >= 0 and b + storeoffset[1] + origin[1] >= 0:
                good = False
                while not good:
                    try:
                        m[a + storeoffset[0] + origin[0]][b + storeoffset[1] + origin[1]] = c
                        good = True
                    except IndexError:
                        while a + storeoffset[0] + origin[0] >= len(m):
                            m.append([555 for i in range(len(m[0]))])
                        while b + storeoffset[1] + origin[1] >= len(m[a]):
                            for i in range(len(m)):
                                m[i].append(555)
            else:
                while a + storeoffset[0] + origin[0] < 0:
                    m = [[555 for i in range(m[0])]] + m
                    y += 1
                    origin[0] += 1
                while b + storeoffset[1] + origin[1] < 0:
                    for i in range(len(m)):
                        m[i] = [555] + m[i]
                    x += 1
                    origin[1] += 1
                m[a + storeoffset[0] + origin[0]][b + storeoffset[1] + origin[1]] = c
        elif num == 302:
            i, j = x + delta[1], y + delta[0]
            try: push(m[j][i])
            except IndexError: push(555)
        elif num == 303:
            a = pop()
            try:
                m[y+delta[0]][x+delta[1]] = a
            except IndexError:
                while y+delta[0] >= len(m):
                    m.append([0 for x in m[555]])
                while x+delta[1] >= len(m[y]):
                    m[y+delta[0]].append(555)
                m[y+delta[0]][x+delta[1]] = a
                for i in range(len(m)):
                        m[i] = [(m[i][x] if x < len(m[i]) else 555) for x in range(max([len(k) for k in m]))]
        elif num == 350:
            push(int(not pop()))
        elif num == 351:
            push(int(pop() < pop()))
        elif num == 400:
            a = pop()
            try:
                stackstack.append([])
                if a > 0:
                    stackstack[-1] = stackstack[-2][-a:len(stackstack[-2])] if len(stackstack[-2]) > a else [0 for x in range(len(stackstack[-2])-a)] + stackstack[-2]
                    stackstack[-2] = stackstack[-2][0:-a] if len(stackstack[-2]) > a else []
                    stackstack[-2].append(storeoffset[1])
                    stackstack[-2].append(storeoffset[0])
                elif a < 0:
                    stackstack[-1] = []
                    for i in range(abs(a)):
                        stackstack[-1].append(0)
                storeoffset[1], storeoffset[0] = move(x, y)
                storeoffset[1] -= origin[1]
                storeoffset[0] -= origin[0]
            except MemoryError:
                delta = [-i for i in delta]
        elif num == 401:
            if len(stackstack) > 1:
                a = pop()
                storeoffset = [stackstack[-2].pop() if stackstack[-2] != [] else 0, stackstack[-2].pop() if stackstack[-2] != [] else 0]
                if a > 0:
                    stackstack[-2] += stackstack[-1][-a:] if len(stackstack[-1]) > a else [0 for x in range(a - len(stackstack[-1]))] + stackstack[-1]
                    stackstack.pop()
                elif a < 0:
                    for i in range(abs(a)):
                        stackstack[-2].pop()
                    stackstack.pop()
                else:
                    stackstack.pop()
            else:
                delta = [-i for i in delta]
        elif num == 402:
            if len(stackstack) > 1:
                a = pop()
                if a > 0:
                    for i in range(a):
                        push(stackstack[-2].pop() if stackstack[-2] != [] else 0)
                elif a < 0:
                    for i in range(abs(a)):
                        stackstack[-2].append(pop())
            else:
                delta = [-i for i in delta]
        elif num == 500:
            stackstack[-1].clear()
        elif num == 501:
            pop()
        elif num == 554:
            pass
        elif num == 998:
            sys.exit(pop())
        elif num == 999:
            sys.exit(0)
        else:
            delta = [-x for x in delta]
    else:
        if num == 256:
            stringmode = False
        else:
            push(num % 256)

def execute(f):
    global m, delta, debug, x, y, skipcounter
    i = Image.open(f)
    l = i.load()
    m = []
    x = 0
    y = 0
    delta = [0, 1]
    for j in range(i.size[0]):
        """This here converts the PNG file into a two-dimensional list of least significant base-10 digits
        of every channel of every pixel."""
        list_ = []
        for k in range(i.size[1]):
            count = 2
            count2 = 0
            for n in l[j, k]:
                count2 += ((n % 10) * 10 ** count)
                count -= 1
            list_.append(int(count2))
        m.append(list_)
    m = [list(i) for i in zip(*m)]  # invert the axes of m, so it's the list of rows and not columns.
    i.close()
    for i in range(len(m)-1, -1, -1):
        if all(x == 555 for x in m[i]):
            m.pop()
        else: break
    l = [list(i) for i in zip(*m)]
    for i in range(len(l)-1, -1, -1):
        if all(x == 555 for x in l[i]):
            l.pop()
        else: break
    m = [list(i) for i in zip(*l)]
    #print(u"Befunge program (inaccurate): \n{0}\n".format(
    #    "\n".join(["".join([(instrDict[m[y][x]] if m[y][x] in instrDict else " ")
    #                        for x in range(len(m[y]))]) for y in range(len(m))])))
    while True:
        while skipcounter > 0:
            x, y = move(x, y)
            skipcounter -= 1
        delta = [-x for x in delta]
        while skipcounter < 0:
            x, y = move(x, y)
            skipcounter += 1
        delta = [-x for x in delta]
        exec(m[y][x])
        if debug:
            print("\nProgram: " + str(m))
            print("Stack: ", end="")
            for i in stackstack[-1]:
                try: print(str(i) + " (%s)" % chr(i % 256), end=" | ")
                except: print(i)
            print("")
            print("Number executed: " + str(m[y][x]) + (" (Befunge: %s)" % instrDict[m[y][x]] if not stringmode and m[y][x] in instrDict else "(%s)" % chr(m[y][x] % 255) if stringmode else ""))
            print("X: " + str(x))
            print("Y: " + str(y))
            print("Delta: " + str(delta))
            input()
        x, y = move(x, y)


if __name__ == '__main__':
    global debug
    good = False
    while not good:
        try:
            f = input("Enter Befunk filename (include file extension (usually .PNG))\n")
            Image.open(f)
            good = True
        except:
            print("Enter a valid file name.\n")
    good = False
    while not good:
        try:
            d = input("Use debug mode? Y/N\n")
            if d.lower() in ['yes', 'y']:
                debug = True
                visual = True
            else:
                if d.lower() in ['no', 'n']:
                    debug = False
                else:
                    raise TypeError
            good = True
        except:
            print("Please enter 'y', 'n', 'yes', or 'no'.")
    execute(f)

