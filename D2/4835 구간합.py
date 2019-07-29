def my_max(arr):
    temp_max = arr[0]
    for i in range(1, len(arr)):
        if temp_max < arr[i]:
            temp_max = arr[i]
    return temp_max

def my_min(arr):
    temp_min = arr[0]
    for i in range(1, len(arr)):
        if temp_min > arr[i]:
            temp_min = arr[i]
    return temp_min

for rounds in range(int(input())):
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))

    sums = []

    for i in range(N- M + 1):
        range_sum = 0
        for l in range(i, i + M):
            range_sum += numbers[l]
        sums += [range_sum]

    result = my_max(sums) - my_min(sums)

    print('#%d %d' %((rounds + 1), result))
    