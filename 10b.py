def reverse(arr, start, leng):
    upto = start
    k = start + leng
    k %= len(arr)
    newarr = []
    while upto != k:
        newarr.append(arr[upto])
        upto += 1
        if upto == len(arr):
            upto -= len(arr)
    newarr = newarr[::-1]
    upto = start
    n = 0
    while upto != k:
        arr[upto] = newarr[n]
        upto += 1
        n += 1
        if upto == len(arr):
            upto -= len(arr)

def solution(lines):
    nums = [i for i in range(256)]
    curpos = 0
    skipsize = 0
    lens = []
    if len(lines) == 1:
        for c in lines[0]:
            lens.append(ord(c))
    lens = lens + [17,31,73,47,23]

    for j in range(64):
        for n in lens:
            reverse(nums, curpos, n)
            curpos += n + skipsize
            curpos %= len(nums)
            skipsize += 1

    n = 0
    xx = 0
    hexy = []
    for j in nums:
        xx ^= j
        n += 1
        if (n % 16) == 0 and n != len(nums):
            hexy.append(xx)
            xx = 0
    hexy.append(xx)
    finalstr = ''
    for x in hexy:
        p = hex(x)[2:]
        if len(p) < 2:
            p = '0' + p
        finalstr = finalstr + p
    print(finalstr)

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
