def solution(input):
    total = 0
    for l in input:
        sp = l.split()
        hits = set()
        fail = False
        for s in sp:
            if s in hits:
                fail = True
                break
            else:
                hits.add(s)
        if not fail:
            total += 1
    print(total)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
