def execute(string):
    string = ''.join([i for i in string[1:] if i in ['0', '1']])
    string = [string[i:i+3] for i in range(0, len(string), 3)]
    new = []
    for i in string:
        new.append('+' if i == '000' else '-' if i == '001' else '>' if i == '010' else '<' if i == '011' else
                   '.' if i == '100' else ',' if i == '101' else '[' if i == '110' else ']' if i == '111' else '')
    new = ''.join(new)
    from brainfuck import execute
    execute(new)