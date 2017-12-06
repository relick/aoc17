def findmax(arr):
    max = 0
    pos = 0
    for i, v in enumerate(arr):
        if v > max:
            max = v
            pos = i
    return pos, max

def solution(input):
    sp = input[0].split()
    for i, v in enumerate(sp):
        sp[i] = int(v)
    seen = set()
    going = True
    total = 0
    while going:
        total += 1
        i, max = findmax(sp)
        sp[i] = 0
        i += 1
        if i >= len(sp):
            i = 0
        while max > 0:
            sp[i] += 1
            max -= 1
            i += 1
            if i >= len(sp):
                i = 0
        if tuple(sp) in seen:
            going = False
        else:
            seen.add(tuple(sp))
    print(total)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
