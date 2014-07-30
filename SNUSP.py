from __future__ import print_function


def execute(string):
    mem = [0]
    ptr = 0
    m = []
    for i in string.split('\n'):
        m.append(list(i))
    for j in range(len(m)):
        for i in range(len(m[j])):
            if m[j][i] == '$':
                x = i; y = j
                break
        else:
            continue
        break
    else:
        x = 0
        y = 0
    delta = [0, 1]
    callstack = []
    buffer = []
    while y in range(len(m)) and x in range(len(m[y])):
        if m[y][x] == '>':
            ptr += 1
            while ptr >= len(mem):
                mem.append(0)
        elif m[y][x] == '<':
            ptr -= 1
            if ptr < 0:
                ptr = 0
        elif m[y][x] == '+':
            mem[ptr] += 1
        elif m[y][x] == '-':
            mem[ptr] -= 1
        elif m[y][x] == ',':
            if buffer == []:
                buffer = list(input())
            mem[ptr] = ord(buffer.pop(0)) if buffer else 0
        elif m[y][x] == '.':
            try:
                print(chr(mem[ptr]),end="")
            except:
                pass
        elif m[y][x] == '\\':
            if delta == [0, 1]:
                delta = [1, 0]
            elif delta == [1, 0]:
                delta = [0, 1]
            elif delta == [0, -1]:
                delta = [-1, 0]
            else:
                delta = [0, -1]
        elif m[y][x] == '/':
            if delta == [0, 1]:
                delta = [-1, 0]
            elif delta == [-1, 0]:
                delta = [0, 1]
            elif delta == [0, -1]:
                delta = [1, 0]
            else:
                delta = [0, -1]
        elif m[y][x] == '!':
            y += delta[0]
            x += delta[1]
        elif m[y][x] == '?':
            if mem[ptr] == 0:
                y += delta[0]
                x += delta[1]
        elif m[y][x] == '@':
            callstack.append(([y,x], delta))
        elif m[y][x] == '#':
            try:
                l = callstack.pop()
            except IndexError:
                return
            y = l[0][0]
            x = l[0][1]
            delta = l[1]
            y += delta[0]
            x += delta[1]
        y += delta[0]
        x += delta[1]