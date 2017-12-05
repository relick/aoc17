def solution(input):
    totalsteps = 0
    for i, v in enumerate(input):
        input[i] = int(v.split()[0])
    
    currentpos = 0
    while 0 <= currentpos < len(input):
        input[currentpos] += 1
        currentpos += input[currentpos]-1
        totalsteps += 1
    print(totalsteps)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
