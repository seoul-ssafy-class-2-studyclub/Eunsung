def bubun(cnt, num, now, su):
    if num > 12 or num > K:
        return cnt
    
    if now != K and su == N:
        return cnt

    if now == K and su == N:
        cnt += 1
        return cnt

    if cache[su][now][num] != -1:
        return cache[su][now][num]
    
    #얘를 안넣을거야
    cnt = bubun(cnt, num + 1, now, su)

    if now + num <= K and su < N:
        cnt += bubun(cnt, num + 1, now + num, su+ 1)
    
    cache[su][now][num] = cnt
    return cnt

result = []
for rounds in range(int(input())):
    N, K = map(int,input().split())
    cache = [[[-1 for _ in range(K + 2)] for _ in range(K + 1)] for _ in range(N + 1)]
    result.append(f'#{rounds + 1} {bubun(0,1,0,0)}')
for value in result:
    print(value)