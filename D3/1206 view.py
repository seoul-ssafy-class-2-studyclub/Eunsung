def my_sort(arr):
    for i in range(len(arr)):

        for l in range(len(arr) - i - 1):
            if arr[l] < arr[l + 1]:
                arr[l], arr[l + 1] = arr[l + 1], arr[l]
    return arr

for rounds in range(10):
    N = int(input())
    buildings = list(map(int,input().split()))
    count = 0
    for i in range(2,N - 2):
        temp = buildings[i-2:i+3]
        temp = my_sort(temp)

        if buildings[i]==temp[0]:
            count += buildings[i] - temp[1]
    
    print('%d %d' %((rounds+ 1), (count)))
