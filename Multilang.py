from __future__ import print_function
import befunge_exec as befunge, brainfuck, replacefuck, eitherfuck, rand as random, os
print("""
+-----------------------------------+
|     Multilang esoteric shell      |
|            by TieSoul             |
|  Replacefuck (rf), Befunge (bf),  |
|  Brainfuck (b), Eitherfuck (ef),  |
|             Random (r)            |
|           are supported.          |
+-----------------------------------+"""
)
while True:
    try:
        dir = os.getcwd()
        a = input(dir + '> ')
        efcode = ''
        bfcode = ''
        bcode = ''
        rfcode = ''
        rcode = ''
        if a.lower() == 'ef':
            while True:
                try:
                    efcode += input('ef> ')
                except KeyboardInterrupt:
                    break
                except:
                    try:
                        input()
                    except KeyboardInterrupt:
                        break
                    except:
                        print("An error occurred.")
        elif a[:3].lower() == 'ef ':
            efcode = a[3:]
        if a.lower() == 'bf':
            while True:
                try:
                    bfcode += input('bf> ') + '\n'
                except KeyboardInterrupt:
                    break
                except:
                    try:
                        input()
                    except KeyboardInterrupt:
                        break
                    except:
                        print("An error occurred.")
        elif a[:3].lower() == 'bf ':
            bfcode = a[3:]
        if a.lower() == 'b':
            while True:
                try:
                    bcode += input('b> ')
                except KeyboardInterrupt:
                    break
                except:
                    try:
                        input()
                    except KeyboardInterrupt:
                        break
                    except:
                        print("An error occurred.")
        elif a[:2].lower() == 'b ':
            bcode = a[2:]
        if a.lower() == 'rf':
            while True:
                try:
                    rfcode += input('rf> ') + '\n'
                except KeyboardInterrupt:
                    break
                except:
                    try:
                        input()
                    except KeyboardInterrupt:
                        break
                    except:
                        print("An error occurred.")
        if a.lower() == 'r':
            while True:
                try:
                    rcode += input('r> ')
                except KeyboardInterrupt:
                    break
                except:
                    try:
                        input()
                    except KeyboardInterrupt:
                        break
                    except:
                        print("An error occurred.")
        elif a[:2].lower() == 'r ':
            rcode = a[2:]
        elif a[:4].lower() == 'exit':
            break
        elif a[:4].lower() == 'help':
            print("""List of commands:
bf <befunge code>: execute befunge-98 code
bf: enter befunge-98 environment
b <brainfuck code>: execute brainfuck code
b: enter brainfuck environment
rf: enter replacefuck environment
ef <eitherfuck code>: execute eitherfuck code
ef: enter eitherfuck environment
r <random code>: execute random code
r: enter random environment
cd: go to directory
dir: list files
f <programming language> <file>: execute file in programming language
ctrl+C: exit an environment and execute code
exit: exit the shell""")
        elif a[:3].lower() == 'cd ':
            try:
                os.chdir(a[3:])
            except:
                pass
            dir = os.getcwd()
        elif a.lower() == 'dir':
            os.system('dir')
        elif a[:2].lower() == 'f ':
            if a[2:4].lower() == 'b ':
                if os.path.exists(a[4:]):
                    brainfuck.execute(open(a[4:]).read())
                    print()
            elif a[2:5].lower() == 'bf ':
                if os.path.exists(a[5:]):
                    befunge.execute(open(a[5:]).read())
                    print()
            elif a[2:5].lower() == 'ef ':
                if os.path.exists(a[5:]):
                    eitherfuck.execute(open(a[5:]).read())
                    print()
            elif a[2:5].lower() == 'rf ':
                if os.path.exists(a[5:]):
                    replacefuck.execute(open(a[5:]).read())
            elif a[2:4].lower() == 'r ':
                if os.path.exists(a[4:]):
                    replacefuck.execute(open(a[4:]).read())
        if efcode != '':
            eitherfuck.execute(efcode)
            print()
        if bfcode != '':
            befunge.execute(bfcode)
            print()
        if bcode != '':
            brainfuck.execute(bcode)
            print()
        if rfcode != '':
            replacefuck.execute(rfcode)
            print()
        if rcode != '':
            random.execute(rcode)
            print()
    except KeyboardInterrupt:
        pass
    except:
        try:
            input()
        except KeyboardInterrupt:
            pass
        except:
            print("An error has occurred.")