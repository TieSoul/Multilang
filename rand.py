from __future__ import print_function


def execute(string):
    string = list(string)
    loopcount = 0
    i = 0
    while i in range(len(string)):
        if string[i] not in '<>[]':
            string.append(string[i])
        elif string[i] == '>':
            try:
                if string[i+1] == '<':
                    print(string.pop(), end="")
                    i += 1
                else:
                    string.append(string.pop(0))
                    i -= 1
            except IndexError:
                string.append(string.pop(0))
                i -= 1
        elif string[i] == '<':
            string = [string.pop()] + string
            i += 1
        elif string[i] == '[':
            if string[0] == string[-1]:
                j = i + 1
                loops = 1
                while j in range(len(string)):
                    if string[j] == '[':
                        loops += 1
                    elif string[j] == ']':
                        loops -= 1
                        if loops == 0:
                            break
                else:
                    return
                i = j
        elif string[i] == ']':
            if string[0] != string[-1]:
                j = i - 1
                loops = 1
                while j in range(len(string)):
                    if string[j] == '[':
                        loops -= 1
                        if loops == 0:
                            break
                    elif string[j] == ']':
                        loops += 1
                    j -= 1
                else:
                    return
                i = j
        i += 1
