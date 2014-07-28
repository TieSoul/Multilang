eitherDict = {'+': '-',
              '-': '+',
              '[': ']',
              ']': '[',
              '.': ',',
              ',': '.',
              '>': '<',
              '<': '>',
              '0': '',
              '#': ''}


def to_brainfuck(ef):
    bf = ''
    ef = list(ef)
    ef = [i for i in ef if i in eitherDict]
    if len(ef) % 2 == 0:
        print("Source code is of even length")
        return bf
    index = int(len(ef) / 2)
    while len(ef) > 1:
        bf += eitherDict[ef.pop(index)]
        bf += ef.pop(index)
        index -= 1
    bf += eitherDict[ef.pop(index)]
    return bf

from brainfuck import execute as ex
def execute(string):
    ex(to_brainfuck(string))