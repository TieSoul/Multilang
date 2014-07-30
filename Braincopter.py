from PIL import Image


def execute(f):
    i = Image.open(f)
    m = i.load()
    ll = []
    for j in range(i.size[1]):
        l = []
        for k in range(i.size[0]):
            v = m[k, j]
            l.append((65536*v[0] + 256*v[1] + v[2]) % 11)
        ll.append(l)
    x = 0
    y = 0
    delta = [0, 1]
    list_ = []
    while x in range(len(ll[0])) and y in range(len(ll)):
        if ll[y][x] == 8:
            delta = [delta[1], -delta[0]]
        elif ll[y][x] == 9:
            delta = [-delta[1], delta[0]]
        elif ll[y][x] == 10:
            pass
        else:
            list_.append(ll[y][x])
        y += delta[0]
        x += delta[1]
    bf = ''
    for i in list_:
        bf += '>' if i == 0 else '<' if i == 1 else '+' if i == 2 else '-' if i == 3 else '.' if i == 4 else \
              ',' if i == 5 else '[' if i == 6 else ']' if i == 7 else ''
    from brainfuck import execute
    execute(bf)