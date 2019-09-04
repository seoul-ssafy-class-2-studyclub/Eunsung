directions = {1:(0, -1), 2:(0, 1), 3:(-1, 0), 4:(1, 0)}
aside = {1:2, 2:1, 3:4, 4:3}
def meet1(y, x, d):
    if d == 1:
        d = 2
    elif d == 2:
        d = 4
    elif d == 3:
        d = 1
    else:
        d = 3
    return y + directions[d][1], x + directions[d][0], d

def meet2(y, x, d):
    if d == 1:
        d = 4
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2
    else:
        d = 3
    return y + directions[d][1], x  + directions[d][0], d

def meet3(y, x, d):
    if d == 1:
        d = 3
    elif d == 2:
        d = 1
    elif d == 3:
        d = 4
    else:
        d = 2
    return y + directions[d][1], x + directions[d][0], d

def meet4(y, x, d):
    if d == 1:
        d = 2
    elif d == 2:
        d = 3
    elif d == 3:
        d = 4
    else:
        d = 1
    return y + directions[d][1], x + directions[d][0], d

def meet5(y, x, d):
    if d == 1:
        d = 2
    elif d == 2:
        d = 1
    elif d == 3:
        d = 4
    else:
        d = 3
    return y + directions[d][1], x + directions[d][0], d

def hall(y, x, d, num):
    for wy, wx in halls[num]:
        if (y, x) != (wy, wx):
            return wy + directions[d][1] , wx + directions[d][0], d

# def move(y, x, d):
#     global cnt
    # if y == start[0] and x == start[1] and cnt > 0:
    #     return
    # dx = directions[d][0]
    # dy = directions[d][1]
    # while 0 <= y < N and 0 <= x < N  and not board[y][x]:
    #     y += dy
    #     x += dx
    #     if y == start[0] and x == start[1]:
    #         return


    # if not (0 <= y < N and 0 <= x < N):
    #     d = aside[d]
    #     cnt += 1
    #     x += directions[d][0]
    #     y += directions[d][1]
    #     move(y, x, d)
            
    # elif 1 <= board[y][x] <= 5:
    #     y, x, d = meets[board[y][x]](y, x, d)
    #     cnt += 1
    #     move(y, x, d)
        
    # elif 6 <= board[y][x] <= 10:
    #     y, x, d = hall(y, x, d, board[y][x])
    #     move(y, x, d)
        
    # else: return


meets = [0, meet1, meet2, meet3, meet4, meet5]
for ro in range(int(input())):
    N = int(input())
    starts = []
    board = []
    halls = [[] for _ in range(11)]
    for y in range(N):
        board.append(list(map(int,input().split())))
        for x in range(N):
            if not board[y][x]:
                for d in range(1, 5):
                    starts.append((y, x, d))
            elif 5 < board[y][x] < 11:
                halls[board[y][x]].append((y, x))
    
    res = 0
    while starts:
        
        y, x, d = starts.pop()
        queue = [(y, x, d)]
        cnt = 0
        
        start = (y, x)
        t = 0

        while queue:
            t += 1
            y, x, d = queue.pop(0)
            if y == start[0] and x == start[1] and t != 1:
                break
            dx = directions[d][0]
            dy = directions[d][1]
            while 0 <= y < N and 0 <= x < N  and not board[y][x]:
                y += dy
                x += dx
                if y == start[0] and x == start[1]:
                    break

            if not (0 <= y < N and 0 <= x < N):
                d = aside[d]
                cnt += 1
                x += directions[d][0]
                y += directions[d][1]
                queue.append((y, x, d))
                    
            elif 1 <= board[y][x] <= 5:
                y, x, d = meets[board[y][x]](y, x, d)
                cnt += 1
                queue.append((y, x, d))
                
            elif 6 <= board[y][x] <= 10:
                y, x, d = hall(y, x, d, board[y][x])
                queue.append((y, x, d))
            
            else: break

            print(queue)


        if cnt > res:
            res = cnt
    print('#%d %d' %(ro + 1, res))

    
