from __future__ import print_function


def execute(string):
    mem = [0]
    point = 0
    oring = 0
    ostore = 0
    oactive = True
    mring = 0
    mstore = 0
    oclock = True
    mclock = True
    execution = True
    buffer = []
    i = 0
    while i in range(len(string)):
        char = string[i]
        if char == '1':
            if oactive:
                if oclock:
                    oring += 1 if oring < 11 else -11
                else:
                    oring -= 1 if oring > 0 else -11
            else:
                if mclock:
                    mring += 1 if mring < 11 else -11
                else:
                    mring -= 1 if mring > 0 else -11
            execution = True
        elif char == '0':
            if oactive:
                oclock = not oclock
            else:
                mclock = not mclock
            if not i == 0 and string[i-1] == '0' and execution:
                if oactive:
                    if oring == 0:
                        pass
                    elif oring == 1:
                        if __name__ == '__main__':
                            import sys
                            sys.exit(0)
                        else:
                            return
                    elif oring == 2:
                        ostore = 1
                    elif oring == 3:
                        ostore = 0
                    elif oring == 4:
                        ostore = mem[point]
                    elif oring == 5:
                        mem[point] = ostore
                    elif oring == 6:
                        i += ostore - 1
                    elif oring == 7:
                        point += ostore
                        while point >= len(mem):
                            mem.append(0)
                    elif oring == 8:
                        if mem[point] == 0:
                            ostore = 0
                        else:
                            ostore = int(ostore and True)
                    elif oring == 9:
                        if mem[point] == 0:
                            i += ostore - 1
                    elif oring == 10:
                        if ostore == 0:
                            good = False
                            while not good:
                                try:
                                    mem[point] = int(input())
                                    good = True
                                except:
                                    pass
                        else:
                            print(mem[point], end="")
                    elif oring == 11:
                        if ostore == 0:
                            if buffer == []:
                                buffer = list(input())
                            mem[point] = buffer.pop(0)
                        else:
                            print(chr(mem[point]), end="")
                else:
                    if mring == 0:
                        pass
                    elif mring == 1:
                        mstore = mem[point]
                    elif mring == 2:
                        mem[point] = mstore
                    elif mring == 3:
                        mstore += mem[point]
                    elif mring == 4:
                        mstore *= mem[point]
                    elif mring == 5:
                        mstore //= mem[point]
                    elif mring == 6:
                        mstore = 0
                    elif mring == 7:
                        if mstore < mem[point]:
                            mstore = 1
                        else:
                            mstore = 0
                    elif mring == 8:
                        if mstore > mem[point]:
                            mstore = 1
                        else:
                            mstore = 0
                    elif mring == 9:
                        if mstore == mem[point]:
                            mstore = 1
                        else:
                            mstore = 0
                    elif mring == 10:
                        mstore = int(not mstore)
                    elif mring == 11:
                        mstore = -mstore
                execution = False
                oactive = not oactive
            else:
                execution = True

        i += 1