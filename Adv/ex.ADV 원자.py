
for ro in range(int(input())):
    N = int(input())

    board = [[0 for _ in range(2002)] for _ in range(2002)]

    energys = 0
    stack = []
    atoms = []
    for _ in range(N):
        x, y, v, e = map(int,input().split())
        x += 1000
        y += 1000
        board[x][y] = (v, e)
        atoms.append((x, y, v, e))
    
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms))
        

    


