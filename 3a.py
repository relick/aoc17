import math

def solution(input):
    num = int(input)
    n = int(math.ceil(math.sqrt(num)))
    if n%2 == 0:
        n+=1
    squarelen = (n**2) - (n-2)**2
    striplen = squarelen/4
    test = n**2 - striplen
    while test >= num:
        test -= striplen
    mid = test + (striplen/2)
    stepsfurther = abs(num-mid)
    stepstomid = (n-1)/2
    print(int(stepsfurther + stepstomid))

if __name__ == "__main__":
    import sys
    #tfile = open(sys.argv[1], 'r')
    #solution(tfile.readlines())
    solution(sys.argv[1])
