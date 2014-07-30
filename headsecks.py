def execute(s):
    new = ''
    for i in s:
        o = ord(i) % 8
        new += '+' if o == 0 else '-' if o == 1 else '<' if o == 2 else '>' if o == 3 else '.' if o == 4 else\
               ',' if o == 5 else '[' if o == 6 else ']'
    from brainfuck import execute
    execute(new)