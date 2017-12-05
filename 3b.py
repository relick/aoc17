RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

def solution(input):
    num = int(input)
    lm = [[0 for col in range(573)] for row in range(573)]
    x = 286
    y = 286
    lm[x][y] = 1
    dir = RIGHT
    while lm[x][y] <= num:
        if dir == RIGHT:
            x+=1
            if lm[x][y+1] == 0:
                dir = UP
        elif dir == UP:
            y+=1
            if lm[x-1][y] == 0:
                dir = LEFT
        elif dir == LEFT:
            x-=1
            if lm[x][y-1] == 0:
                dir = DOWN
        elif dir == DOWN:
            y-=1
            if lm[x+1][y] == 0:
                dir = RIGHT
        lm[x][y] = lm[x+1][y] + lm[x+1][y+1] + lm[x+1][y-1] + lm[x][y+1] + lm[x][y-1] + lm[x-1][y] + lm[x-1][y+1] + lm[x-1][y-1]
    print(lm[x][y])

if __name__ == "__main__":
    import sys
    #tfile = open(sys.argv[1], 'r')
    #solution(tfile.readlines())
    solution(sys.argv[1])
