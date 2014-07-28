def execute(string):
    debug = False
    program = [i for i in list(string[string.index("PROG:")+5:]) if i != '\n']
    assert all(i not in program for i in ['+', '-', '>', '<', '[', ']', ',', '.'])
    for i in string.split('\n'):
        name = i[:i.index(":")]
        if name == "PROG":
            break
        bf = i[i.index(":")+1:]
        for i in bf:
            assert i in ['[', ']', ',', '.', '+', '-', '>', '<'] or i in name
        name2 = ''
        vars = ''
        intoVars = False
        for i in name:
            if i not in bf:
                assert not intoVars
                name2 += i
            else:
                intoVars = True
                vars += i
        while name2 in ''.join(program):
            if vars == '':
                program = list(''.join(program).replace(name2, bf))
                break
            index = ''.join(program).index(name2)
            del program[index:index+len(name2)]
            thing = program[index:]
            del program[index:]
            newvars = []
            vardict = {}
            for i in vars:
                newvars.append(int(thing[0], 16))
                del thing[0]
            for i in range(len(vars)):
                vardict.update({vars[i]: newvars[i]})
            for j in vars:
                while j in bf:
                    dex = bf.index(j)
                    char = bf[dex-1]
                    bf = bf[:dex-1] + bf[dex:]
                    bf = bf.replace(j, char * vardict[j], 1)
            thing = list(bf) + thing
            program += thing
    if debug or False:
        print("Final Brainfuck program: %s" % ''.join(program))
        print("Program is now executing.")
        import time, os
        time.sleep(1)
        os.system(['clear', 'cls'][os.name == 'nt'])
    from brainfuck import execute
    execute(''.join(program))

if __name__ == '__main__':
    execute(open(input("Please input a replacefuck source file's filename.")).read())