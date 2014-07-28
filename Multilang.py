import befunge, brainfuck, replacefuck, eitherfuck

print("""
+-----------------------------------+
|     Multilang esoteric shell      |
|            by TieSoul             |
|  Replacefuck (rf), Befunge (bf),  |
|  Brainfuck (b), Eitherfuck (ef)   |
|           are supported.          |
+-----------------------------------+"""
)

while True:
    try:
        a = input('> ')
        efcode = ''
        bfcode = ''
        bcode = ''
        rfcode = ''
        if a == 'ef':
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
                        print("An error occurrec.")
        elif a[:3] == 'ef ':
            efcode = a[3:]
        if a == 'bf':
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
                        print("An error occurrec.")
        elif a[:3] == 'bf ':
            bfcode = a[3:]
        if a == 'b':
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
                        print("An error occurrec.")
        elif a[:2] == 'b ':
            bcode = a[2:]
        if a == 'rf':
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
                        print("An error occurrec.")
        elif a[:4] == 'exit':
            break
        elif a[:4] == 'help':
            print("""List of commands:
bf <befunge code>: execute befunge code
bf: enter befunge environment
b <brainfuck code>: execute brainfuck code
b: enter brainfuck environment
rf: enter replacefuck environment
ef <eitherfuck code>: execute eitherfuck code
ef: enter eitherfuck environment
ctrl+C: exit an environment
exit: exit the shell""")
        if efcode != '':
            eitherfuck.execute(efcode)
            print()
        if bfcode != '':
            befunge.execute(bfcode, False, False, False)
            print()
        if bcode != '':
            brainfuck.execute(bcode)
            print()
        if rfcode != '':
            replacefuck.execute(rfcode)
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