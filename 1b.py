def solution(lines):
    total = 0
    j = int((len(lines[0])-1)/2)
    numdig = int(j*2)
    for i in range(numdig):
        j %= numdig
        if lines[0][i] == lines[0][j]:
            total += int(lines[0][i])
        j += 1

    print(total)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
