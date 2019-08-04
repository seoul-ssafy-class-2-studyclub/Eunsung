
near = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def find_0(y, x):
    for (dy, dx) in near:
        if 0 <= y + dy <= N-1 and 0 <= x + dx <= N-1:
            if count_board[y + dy][x + dx] == 0 and type(count_board[y + dy][x + dx]) != bool:
                return True
    return False


class mine_find:

    def __init__(self, y, x):
        
        if count_board[y][x] == 0 and type(count_board[y][x]) != bool:
            count_board[y][x] = False
            temp.add((y, x))
            for (dy, dx) in near:
                if 0 <= y + dy <= N-1 and 0 <= x + dx <= N-1:
                    mine_board[y + dy][x + dx] = mine_find(y + dy, x + dx)
        elif type(count_board[y][x]) != bool:
            if not find_0(y, x):    
                count_board[y][x] = False
                temp.add((y, x))


for rounds in range(int(input())):
    N = int(input())
    mine_board = [[[1] for _ in range(N)] for _ in range(N)]
    result = []
    count_board = []

    for i in range(N):
        count_board.append(list(input()))
    
    for y in range(N):
        for x in range(N):
            if count_board[y][x] != '*':
                count = 0
                for (dy, dx) in near:
                    if 0 <= y + dy <= N-1 and 0 <= x + dx <= N-1 and count_board[y + dy][x + dx] == '*':
                        count += 1
                count_board[y][x] = count
    
    for y in range(N):
        for x in range(N):
            if count_board[y][x] != '*' and type(count_board[y][x]) != bool:
                temp = set()
                mine_board[y][x] = mine_find(y, x)
                if temp:
                    result.append(temp)

    print(f'#{rounds + 1} {len(result)}')
