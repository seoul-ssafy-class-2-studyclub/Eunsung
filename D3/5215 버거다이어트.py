import sys
sys.stdin = open('input.txt.txt', 'r')

def diet(cal, menu):
    if menu == N:
        return 0
    
    if cache[cal][menu] != -1:
        res = cache[cal][menu]
    
    # 안넣고 넘어감
    res = diet(cal, menu + 1)

    if cal + arr[menu][1] <= C:
        res = max(res, diet(cal + arr[menu][1], menu + 1) + arr[menu][0])
    
    cache[cal][menu] = res
    return res

result = []
for rounds in range(int(input())):

    N, C = map(int, input().split())
    cache = [[-1] * (N + 2)] * (C + 2)
    
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    
    result.append(f'#{rounds + 1} {diet(0,0)}')
for value in result:
    print(value)
    

    
