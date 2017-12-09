def solution(lines):
    score = 0
    curgroup = 0
    garbagecount = 0
    ingarbage = False
    skip = False
    for c in lines[0]:
        if skip:
            skip = False
            continue
        elif c == "!":
            skip = True
            continue
        elif c == "{" and not ingarbage:
            curgroup += 1
        elif c == "}" and not ingarbage:
            score += curgroup
            curgroup -= 1
        elif c == "<" and not ingarbage:
            ingarbage = True
        elif c == ">" and ingarbage:
            ingarbage = False
        elif ingarbage:
            garbagecount += 1
    print(garbagecount)


if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
