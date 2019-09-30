N = int(input())
board = [0] * N
for day in range(N):
    board[day] = tuple(map(int,input().split()))

counting = [0] * (N + 1)
counting[0] = board[0][1]
for day in range(N):
    gap, earn = board[day]

    if day + gap > N - 1:
        temp = N - 1
    else:
        temp = day + gap
    for i in range(gap, gap + board[temp][0] + 1):
        if day + i <= N - 1:
            tem = board[day + i][1] + counting[day]
            if tem > counting[day + i]:
                counting[day + i] = tem
    if day + gap <= N:
        if counting[day] > counting[N]:
            counting[N] = counting[day]

print(counting[N])
