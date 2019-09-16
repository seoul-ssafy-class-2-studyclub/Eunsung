for ro in range(int(input())):
    N = int(input())
    
    cases = []
    for y in range(N):
        cases.append(list(map(int,input().split())))
        cases[-1].append(cases[-1][1] - cases[-1][0])
    
    cases.sort(key=lambda x: x[-1])
    times = [False] * 25
    res = 0
    for case in cases:
        flag = 0
        for time in range(case[0] + 1, case[1] + 1):
            if times[time]:
                flag = 1
                break
        if flag:
            continue
        res += 1
        for time in range(case[0] + 1, case[1] + 1):
            times[time] = True
    print('#%d %d' %(ro + 1, res))
