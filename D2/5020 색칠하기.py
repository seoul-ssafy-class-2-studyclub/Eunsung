result = []
for round in range(int(input())):
    board = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    count = 0 #카운트 초기화
    for color in range(N): 
        r1, c1, r2, c2, color = map(int,input().split()) #정보를 받아온다
        for y in range(r1, r2 + 1):
            for x in range(c1, c2 + 1):
                if board[y][x] == 0: #보드가 0이면 색칠
                    board[y][x] = color
                elif board[y][x] != color and board[y][x] != 3: #색깔이 다르고 3이아니라면 
                    board[y][x] = 3# 보라색 색칠후 카운트 +1
                    count += 1
        
    result.append('#%d %d' %(round + 1, count))

for value in result:
    print(value)
    

