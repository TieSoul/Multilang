def execute(r):
    s = [0]
    i = 0
    inputstring = ''
    loopstack = []
    j = 0
    while j in range(len(r)):
        if r[j] == '>':
            i += 1
            if i >= len(s):
                s.append(0)
        elif r[j] == '<':
            i -= 1
        elif r[j] == '+':
            s[i] = min(s[i] + 1, 0x110000)
        elif r[j] == '-':
            s[i] = max(s[i] - 1, 0)
        elif r[j] == '.':
            try:
                print(chr(s[i]), end="")
            except ValueError:
                pass
        elif r[j] == ',':
            if inputstring == '':
                inputstring = input()
                s[i] = ord(inputstring[0]) if inputstring != '' else ord(' ')
                inputstring = inputstring[1:]
            elif len(inputstring) == 2 and not '\n' in inputstring:
                inputstring += '\n'
                s[i] = ord(inputstring[0])
                inputstring = inputstring[1:]
            else:
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
            else:
                loopstack.append(j)
        elif r[j] == ']':
            if s[i] > 0:
                j = loopstack.pop() - 1
        else:
            j += 1
            continue
        j += 1




if __name__ == '__main__':
    execute(input("Input your Brainfuck code:\n"))