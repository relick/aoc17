def solution(lines):
    checksum = 0
    for l in lines:
        sp = l.split()
        for i in range(len(sp)):
            for j in range(len(sp)):
                if (i != j) and (int(sp[i]) >= int(sp[j])) and ((int(sp[i]) % int(sp[j])) == 0):
                    checksum += (int(sp[i]) / int(sp[j]))
                    break
    print(checksum)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
