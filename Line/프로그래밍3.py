N = int(input())
toilets = []
for _ in range(N):
    toilets.append(tuple(map(int,input().split())))

board = [0] * 151

for start, end in toilets:
    for time in range(start, end):
        board[time] += 1

print(max(board))