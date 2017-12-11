def getdist(x, y):
    steps = 0
    while x != 0:
        steps += 1
        if x > 0:
            x -= 1
            if y > 0:
                y -= 0.5
            else:
                y += 0.5
        else:
            x += 1
            if y > 0:
                y -= 0.5
            else:
                y += 0.5
    steps += abs(y)
    return steps
def solution(lines):
    x = 0
    y = 0
    maxy = 0
    for s in lines[0].split()[0].split(','):
        if s == 'n':
            y += 1
        elif s == 'ne':
            y += 0.5
            x += 1
        elif s == 'se':
            y -= 0.5
            x += 1
        elif s == 's':
            y -= 1
        elif s == 'sw':
            y -= 0.5
            x -= 1
        elif s == 'nw':
            y += 0.5
            x -= 1
        k = getdist(x, y)
        if k > maxy:
            maxy = k
    print(maxy)
        

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
