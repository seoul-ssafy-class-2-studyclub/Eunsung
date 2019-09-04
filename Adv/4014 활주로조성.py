def check(arr):
    flag = 0
    cnt = 0
    temp = arr[0]
    for x in range(len(arr)):
        if temp == arr[x]:
            cnt += 1
            if flag:
                if cnt == X:
                    cnt = 0
        else:
            if not flag:
                if temp > arr[x]:
                    cnt = 0
                    flag = 1
                elif temp < arr[x]:
                    if cnt < X:
                        return False
            
            else:
                if cnt < X:
                    return False
                cnt = 0



for ro in range(int(input())):
    N, X = map(int,input().split())
    board = []
    cnt = 0
    setuped = [False] * N
    for y in range(N):
        board.append(list(map(int,input().split())))

        