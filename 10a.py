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
    for n in lines[0].split(','):
        reverse(nums, curpos, int(n))
        curpos += int(n) + skipsize
        curpos %= len(nums)
        skipsize += 1
    print(nums[0]*nums[1])

if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
