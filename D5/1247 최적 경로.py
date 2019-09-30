def distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def permu(arr, dis):
    global min_dis

    if len(arr) == N:
        dis += distance(home, houses[arr[-1]])

        if dis < min_dis:
            min_dis = dis
            return
    if dis >= min_dis:
        return
    
    for idx in range(N):
        if visisted[idx]:
            continue
            
        visisted[idx] = True
        permu(arr + [idx], dis + distance(houses[idx], houses[arr[-1]]))
        visisted[idx] = False

            

for ro in range(int(input())):
    N = int(input())
    houses = [0] * (N + 2)
    visisted = [False] * N
    min_dis = 99999
    temp = list(map(int,input().split()))
    for y in range(N + 2):
        houses[y] = (temp[2 * y], temp[2 * y + 1])

    company = houses.pop(0)
    home = houses.pop(0)

    for idx in range(N):
        visisted[idx] = True
        permu([idx], distance(company, houses[idx]))
        visisted[idx] = False
    
    print('#%d %d' %(ro + 1, min_dis))

