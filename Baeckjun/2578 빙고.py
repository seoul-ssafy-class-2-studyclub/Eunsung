board = []

for i in range(5):
    board.append(list(map(int,input().split())))

checkbingo = {}
counting = {}
bingo = 0

for i in range(26):
    checkbingo[i] = []
    if i < 12:
        counting[i] = 0

for y in range(5):
    for x in range(5):
        checkbingo[board[y][x]].append(y)
        checkbingo[board[y][x]].append(x + 5)
        if y == x:
            checkbingo[board[y][x]].append(10)
        if y + x == 4:
            checkbingo[board[y][x]].append(11)

check_list = []
for i in range(5):
    check_list += list(map(int,input().split()))

for checknum in range(len(check_list)):
    for bingnum in checkbingo[check_list[checknum]]:
        counting[bingnum] += 1
        if counting[bingnum] == 5:
            bingo += 1

    if bingo >= 3:
        result = checknum + 1
        break
print(result)

