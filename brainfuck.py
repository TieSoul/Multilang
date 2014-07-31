from __future__ import print_function


def execute(r):
    s = [0]
    i = 0
    inputstring = ''
    j = 0
    while j in range(len(r)):
        if r[j] == '>':
            i += 1
            if i >= len(s):
                s.append(0)
        elif r[j] == '<':
            i = max(0, i-1)
        elif r[j] == '+':
            s[i] += 1
        elif r[j] == '-':
            s[i] -= 1
        elif r[j] == '.':
            try:
                print(chr(s[i]), end="")
            except:
                pass
        elif r[j] == ',':
            if inputstring == '':
                inputstring = input() + '\n'
            s[i] = ord(inputstring[0])
            inputstring = inputstring[1:]
        elif r[j] == '[':
            if s[i] == 0:
                loopcount = 1
                while loopcount > 0:
                    j += 1
                    if r[j] == '[':
                        loopcount += 1
                    elif r[j] == ']':
                        loopcount -= 1
        elif r[j] == ']':
            if s[i] != 0:
                loopcount = 1
                while loopcount > 0:
                    j -= 1
                    if r[j] == ']':
                        loopcount += 1
                    elif r[j] == '[':
                        loopcount -= 1
        j += 1




if __name__ == '__main__':
    execute(input("Enter Brainfuck code:\n"))