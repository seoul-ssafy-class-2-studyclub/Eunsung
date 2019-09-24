def combi(now, sums):
    global result

    if now == N - 1:
        if sums >= H:
            if sums - H < result:
                result = sums - H
            return
        if sums + num_list[now] >= H:
            if sums + num_list[now] - H < result:
                result = sums + num_list[now] - H
            return
        return
    
    combi(now + 1, sums + num_list[now])
    combi(now + 1, sums)


for ro in range(int(input())):
    N, H = map(int,input().split())
    num_list = list(map(int,input().split()))
    result = 99999

    combi(0, 0)
    print('#%d %d' %(ro + 1, result))