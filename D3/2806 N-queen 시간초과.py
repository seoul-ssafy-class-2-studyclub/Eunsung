def put_queen(already_queens, num):
    
    if len(already_queens) == N - 1:
        result.append(1)
        
        return True
    
    for i in range(N * (num // N + 1), N ** 2):
        if check_queen(already_queens + [num], i):
            put_queen(already_queens + [num], i)

    # return False
def check_queen(arr, i):
    for z in arr:
        if cache[z][i] != -1:
            if cache[z][i]:
                continue
            else:
                return cache[z][i]
            
        if locations[z][0] == locations[i][0] or locations[z][1] == locations[i][1]:
            cache[z][i] = False
            return False

        j = 1
        while locations[i][0] - j >= 0 and locations[i][1] - j >= 0:
            if locations[z] == (locations[i][0] - j, locations[i][1] - j):
                cache[z][i] = False
                return False
            j += 1

        j = 1
        while locations[i][0] - j >= 0 and locations[i][1] + j <= N - 1:
            if locations[z] == (locations[i][0] - j, locations[i][1] + j):
                cache[z][i] = False
                return False
            j += 1

    cache[z][i] = True
    return True


    ls2 = ls[:]
# cache = [[-1 for _ in range(10** 2)] for _ in range(10 ** 2)]
for round in range(int(input())):
    N = int(input())
    locations = []
    result = []

    for y in range(N):
        for x in range(N):
            locations.append((y, x))
    cache = [[-1 for _ in range(N ** 2)] for _ in range(N ** 2)]

    if N % 2:
        for i in range(N):
            put_queen([], i)
        res = len(result)
        
    else:
        for i in range(N//2):
            put_queen([], i)
        res = len(result) * 2

    print('#%d %d' %(round+ 1, res))