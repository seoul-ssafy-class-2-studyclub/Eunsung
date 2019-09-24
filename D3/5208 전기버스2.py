def drive(charge, cnt, now):
    global min_cnt
    if now == goal:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    
    if cnt > min_cnt:
        return

    if charge:
        drive(charge - 1, cnt, now + 1)

    drive(batterys[now] - 1, cnt + 1, now + 1)
    return
    
        
for ro in range(int(input())):
    batterys = list(map(int,input().split()))
    goal = batterys.pop(0) - 1
    now = 1
    charge = batterys[0] - 1
    min_cnt = 99999

    drive(charge, 0, now)
    print('#%d %d' %(ro + 1, min_cnt))

