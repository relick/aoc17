def solution(input):
    totalsteps = 0
    for i, v in enumerate(input):
        input[i] = int(v.split()[0])
    
    currentpos = 0
    while 0 <= currentpos < len(input):
        k = 1
        if input[currentpos] >= 3:
            k = -1
            input[currentpos] += k
        else:
            input[currentpos] += k
        currentpos += input[currentpos]-k
        totalsteps += 1
    print(totalsteps)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
