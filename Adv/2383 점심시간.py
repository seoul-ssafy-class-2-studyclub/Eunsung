def permutaion(arr):
    if len(arr) == P:
        stair_choice.append(arr)
        return
    
    for i in range(2):
        permutaion(arr + [i])
    
for ro in range(int(input())):
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int,input().split())))
    
    people = []
    stairs = []
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                people.append((y, x))
            elif board[y][x] > 1:
                stairs.append((y, x, board[y][x]))
    
    P = len(people)
    stair_choice = []
    permutaion([])
    res = 999999
    waiting_1 = []
    waiting_2 = []
    waitings_list = [waiting_1, waiting_2]
    stair_1 = []
    stair_2 = []
    stairs_list = [stair_1, stair_2]

    while stair_choice:

        choices = stair_choice.pop(0)
        for i in range(P):
            dy = abs(people[i][0] - stairs[choices[i]][0])
            dx = abs(people[i][1] - stairs[choices[i]][1])
            waitings_list[choices[i]].append(dy + dx)
        
        waiting_1.sort()
        waiting_2.sort()
        t = -1
        while stair_1 or stair_2 or waiting_1 or waiting_2:
            t += 1

            for i in range(2):

                for _ in range(len(stairs_list[i])):
                    temp = stairs_list[i].pop(0)
                    if temp == stairs[i][2] - 1:
                        continue

                    stairs_list[i].append(temp + 1)

                while waitings_list[i] and len(stairs_list[i]) < 3:
                    if  waitings_list[i][0] <= t:
                        waitings_list[i].pop(0)
                        stairs_list[i].append(0)
                    else: break
                        
                
        if t < res:
            res = t

    print('#%d %d' %(ro+ 1, res + 1))
