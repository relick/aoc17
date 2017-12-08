def solution(lines):
    reg = dict()
    for l in lines:
        sp = l.split()
        if sp[5] == ">":
            t = 0
            if sp[4] in reg:
                t = reg[sp[4]]
            if t > int(sp[6]):
                k = 0
                if sp[0] in reg:
                    k = reg[sp[0]]
                if sp[1] == "inc":
                    reg[sp[0]] = k+ int(sp[2])
                else:
                    reg[sp[0]] = k- int(sp[2])
        elif sp[5] == "<":
            t = 0
            if sp[4] in reg:
                t = reg[sp[4]]
            if t < int(sp[6]):
                k = 0
                if sp[0] in reg:
                    k = reg[sp[0]]
                if sp[1] == "inc":
                    reg[sp[0]] = k+ int(sp[2])
                else:
                    reg[sp[0]] = k- int(sp[2])
        elif sp[5] == ">=":
            t = 0
            if sp[4] in reg:
                t = reg[sp[4]]
            if t >= int(sp[6]):
                k = 0
                if sp[0] in reg:
                    k = reg[sp[0]]
                if sp[1] == "inc":
                    reg[sp[0]] = k+ int(sp[2])
                else:
                    reg[sp[0]] = k- int(sp[2])
        elif sp[5] == "==":
            t = 0
            if sp[4] in reg:
                t = reg[sp[4]]
            if t == int(sp[6]):
                k = 0
                if sp[0] in reg:
                    k = reg[sp[0]]
                if sp[1] == "inc":
                    reg[sp[0]] = k+ int(sp[2])
                else:
                    reg[sp[0]] = k- int(sp[2])
        elif sp[5] == "<=":
            t = 0
            if sp[4] in reg:
                t = reg[sp[4]]
            if t <= int(sp[6]):
                k = 0
                if sp[0] in reg:
                    k = reg[sp[0]]
                if sp[1] == "inc":
                    reg[sp[0]] = k+ int(sp[2])
                else:
                    reg[sp[0]] = k- int(sp[2])
        elif sp[5] == "!=":
            t = 0
            if sp[4] in reg:
                t = reg[sp[4]]
            if t != int(sp[6]):
                k = 0
                if sp[0] in reg:
                    k = reg[sp[0]]
                if sp[1] == "inc":
                    reg[sp[0]] = k+ int(sp[2])
                else:
                    reg[sp[0]] = k- int(sp[2])
    max = 0
    for k, v in reg.items():
        if v > max:
            max = v
    print(max)


if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
