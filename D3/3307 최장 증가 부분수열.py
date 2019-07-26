def counting(arr):
    arr.insert(0, 0)
    board = [0] * (N + 1)
    
    for i in range(1, N + 1):

        temp = []

        for l in range(i):
            if arr[l] < arr[i]:
                temp.append(board[l] + 1)
        
        board[i] = max(temp)
    return max(board)

for rounds in range(int(input())):

    N = int(input())

    arr = list(map(int,input().split()))

    print(f'#{rounds + 1} {counting(arr)}')

