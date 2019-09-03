near = [(0, 1), (1, 0)]
def makezero(y, x, cnt_y, cnt_x):
    for ry in range(y, y + cnt_y):
        board[ry][x: x + cnt_x] = [0] * (cnt_x)

def countfriend(y, x):
    cnt_y = 1
    cnt_x = 1

    while board[y][x] and 0 <= y < N - 1:
        y += 1
        if board[y][x]:
            cnt_y += 1
    
    while board[y - 1][x] and 0 <= x < N - 1:
        x += 1
        if board[y - 1][x]:
            cnt_x += 1
    return cnt_y, cnt_x

for ro in range(int(input())):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int,input().split())))
    
    results = []
    
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                results.append(countfriend(y, x))
                cnt_y, cnt_x = results[-1][0], results[-1][1]
                makezero(y, x, cnt_y, cnt_x)
                
    results.sort(key=lambda x: x[0])
    results.sort(key=lambda x: x[0] * x[1])
    print('#%d %d' %(ro + 1, len(results)), end=' ')
    for an1, an2 in results:
        
        print('%d %d' %(an1, an2) ,end=' ')
    print()
