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
    N = int(input())
    numbers = list(map(int,input().split()))
    gap = my_max(numbers) - my_min(numbers)
    print('#%d %d' %((rounds + 1), gap))
