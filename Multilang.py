from __future__ import print_function
import befunge_exec as bf, brainfuck as b, replacefuck as rf, eitherfuck as ef, rand as r, Whirl as wh, Befunk as bk,\
       SNUSP as sn, binaryfuck as bi, headsecks as hd, Braincopter as bc, ABC as abc, os
try:
    from PIL import Image
    has_PIL = True
except ImportError:
    has_PIL = False
print("""
+-----------------------------------+
|     Multilang esoteric shell      |
|            by TieSoul             |
|  Replacefuck (rf), Befunge (bf),  |
|  Brainfuck (b), Eitherfuck (ef),  |
|      Random (r), Whirl (wh),      |
|      Befunk (bk), SNUSP (sn),     |
|    Braincopter (bc), ABC (abc)    |
|           are supported.          |
+-----------------------------------+"""
)
dir = os.getcwd()
while True:
    try:
        c = input(dir + '>> ')
        a = c.split()
        langs = ['ef', 'bf', 'b', 'rf', 'r', 'wh', 'sn', 'bi', 'hd', 'abc']
        nontexts = ['bk', 'bc']
        for i in langs:
            exec("%scode = ''" % i)
        if c.lower() in langs:
            while True:
                try:
                    exec("%scode = %scode + input('%s> ') + '\\n'" % (c.lower(), c.lower(), c.lower()))
                except KeyboardInterrupt:
                    break
                except:
                    try:
                        print()
                    except KeyboardInterrupt:
                        break
                    except:
                        print("An error occurred.")
        elif a[0].lower() in langs:
            exec("%scode = c[len(a[0])+1:]" % a[0].lower())
        elif a[0].lower() == 'exit':
            break
        elif a[0].lower() == 'help':
            print("""List of commands:
<programming language> <code>: execute code in programming language
<programming language>: enter code environment for programming language
cd: go to directory
dir or ls: list files
f <programming language> <file>: execute file in programming language
ctrl+C: exit an environment and execute code
exit: exit the shell

List of languages:
bf - befunge-98
b  - brainfuck
rf - replacefuck
ef - eitherfuck
r  - random
wh - whirl
sn - SNUSP (modular)

NOTE: The following languages are non-textual and cannot be used outside of f.
bk - befunk
bc - braincopter""")
        elif a[0].lower() == 'cd':
            try:
                os.chdir(c[3:])
            except:
                pass
            dir = os.getcwd()
        elif a[0].lower() == 'dir' or a[0].lower() == 'ls':
            os.system('dir')
        elif a[0].lower() == 'f':
            if a[1].lower() in langs:
                if os.path.exists(a[2]):
                    exec("%s.execute(open(a[2]).read())" % a[1].lower())
                    print()
            elif a[1].lower() in nontexts:
                if not has_PIL:
                    print("You need the PIL library to run non-textual languages.")
                elif os.path.exists(a[2]):
                    exec('%s.execute(a[2])' % a[1].lower())
        for i in langs:
            exec("if %scode != '': %s.execute(%scode); print()" % (i, i, i))
    except KeyboardInterrupt:
        pass
    except:
        try:
            print()
        except KeyboardInterrupt:
            pass
        except:
            print("An error has occurred.")