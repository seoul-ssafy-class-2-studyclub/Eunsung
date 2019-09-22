def check(n, k, t, cnt):
    temp_n = [n - 1, n + 1]
    while k < n:
        # print('n',n, 'k',k)
        k += (t + 1)
        if k in temp_n:
            # print(temp_n)
            # print(n)
            print(k)
            return t + 1
        t += 1
        if cnt % 2:
            temp_n = []
            for temp in range(cnt // 2 + 2):
                temp_n.append(n + 2 * temp + 1)
                temp_n.append(n - 2 * temp - 1)
        else:
            temp_n = []
            for temp in range(cnt // 2 + 2):
                temp_n.append(n + 2 * temp)
                temp_n.append(n - 2 * temp)
        cnt += 1
    return False


n, k = map(int,input().split())
t = 0
result = -1
min_time = 99999

while n <= 500000 and k <= 500000:
    if n == k:
        result = t
        break
    if n < k:
        te = t
        te_k = k
        te_n = n
        while 2 * (te_n - 1) > te_k:
            te_k += te + 1
            te_n -= 1
            # print(te_k,'te_k',te_n,'te_n')
            flag = check(2 * te_n, te_k + te + 2, te + 2, 0)
            if flag:
                if flag < min_time:
                    min_time = flag
            te += 1

        n *= 2
        k += t + 1
        t += 1
        continue
    flag = check(n, k, t, 0)
    if flag:
        if flag < min_time:
            min_time = flag
    
    n *= 2
    k += t + 1
    t += 1
if min_time != 99999:
    result = min_time
print(result)
    