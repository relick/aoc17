def getdist(x, y):
    return (abs(x) + abs(y))/2
def solution(lines):
    x = 0
    y = 0
    for s in lines[0].split()[0].split(','):
        if s == 'n':
            y += 2
        elif s == 'ne':
            y += 1
            x += 1
        elif s == 'se':
            y -= 1
            x += 1
        elif s == 's':
            y -= 2
        elif s == 'sw':
            y -= 1
            x -= 1
        elif s == 'nw':
            y += 1
            x -= 1
    print(getdist(x,y))
        

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
