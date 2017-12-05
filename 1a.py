def solution(lines):
    total = 0
    i = 1
    for c in lines[0]:
        if i == len(lines[0])-1: # -1 because of \n
            i = 0
        if c == lines[0][i]:
            total += int(c)
        i += 1

    print(total)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
