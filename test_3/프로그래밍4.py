N = int(input())
seats = list(map(int,input().split()))


max_cnt = 0
per = 0

for idx in range(N):
    cnt = 0
    if not seats[idx]:
        
        flag = 0
        for di in range(N):
            for x in [di, -di]:
                if 0 <= idx + x < N:
                    if seats[idx + x]:
                        if max_cnt < cnt:
                            max_cnt = cnt
                        flag = 1
                        break
            cnt += 1
            if flag:
                break
print(max_cnt)

