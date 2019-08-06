def max_prices(depth, number):
    if depth == K:
        return number

    if cache[depth].get(number) != None:
        res = cache[depth][number]
        return res

    res = 0
    for [x,y] in change_cases:
        temp = changelist(list(number), x, y)
        res = max(res, int(max_prices(depth + 1, temp)))
    
    cache[depth][number] = res
    return res

def changelist(arr, c1, c2):
    arr[c1], arr[c2] = arr[c2], arr[c1]
    arr = ''.join(arr)
    return arr

for round in range(int(input())):
    number, K = input().split()
    K = int(K)
    length = len(number)
    
    digits = list(range(length)) #자리수.
    change_cases = [] #자리바꿀수있는경우의수
    for i in range(1 << length):
        bubun = []
        for j in range(length):
            if i & (1 << j):
                bubun.append(digits[j])
        if len(bubun) == 2:
            change_cases.append(bubun)
    
    cache = [{} for _ in range(K + 1)]

    print(f'#{round + 1} {max_prices(0,number)}')