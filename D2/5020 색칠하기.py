result = []
for round in range(int(input())):
    board = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    count = 0
    for color in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for y in range(r1, r2 + 1):
            for x in range(c1, c2 + 1):
                if board[y][x] == 0:
                    board[y][x] = color
                elif board[y][x] != color and board[y][x] != 3:
                    board[y][x] = 3
                    count += 1
        
    result.append('#%d %d' %(round + 1, count))

for value in result:
    print(value)
    

