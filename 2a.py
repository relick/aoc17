def solution(lines):
    checksum = 0
    for l in lines:
        sp = l.split()
        max = 0
        min = 999999
        for s in sp:
            i = int(s)
            if i < min:
                min = i
            if i > max:
                max = i
        if max != 0:
            checksum += (max - min)
    print(checksum)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
