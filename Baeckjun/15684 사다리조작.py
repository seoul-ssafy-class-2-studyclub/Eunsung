S, G, H = map(int,input().split())
lines = []
for h in range(1, H + 1):
    for s in range(1, S):
        lines.append((h, s))

def combi(arr, now):
    global result
    if len(arr) == line_cnt:
        for h, s in arr:
            board[h][s] = 1
            board[h][s + 1] = -1
        
        for start_idx in range(1, S + 1):
            temp = start_idx
            for y in range(1, H + 1):
                temp += board[y][temp]
            
            if temp != start_idx:
                print(temp, start_idx)
                for h, s in arr:
                    board[h][s] = 0
                    board[h][s + 1] = 0
                return
            
        result = len(arr)    
        return
    
    for idx in range(now + 1, len(lines)):
        combi(arr + [lines[idx]], idx)
        if result != -1:
            return


board = [[0 for _ in range(S + 1)] for _ in range(H  + 1)]
for _ in range(G):
    h, s = map(int,input().split())
    lines.remove((h, s))
    board[h][s] = 1
    board[h][s + 1] = -1
result = -1
for temp in range(4):
    line_cnt = temp
    combi([],-1)
    if result != -1:
        break

print(result)

