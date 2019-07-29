def my_max(arr):
    temp_max = arr[0]
    for i in range(1, len(arr)):
        if temp_max < arr[i]:
            temp_max = arr[i]
    return temp_max

for rounds in range(int(input())):
    N = int(input())
    numbers = list(map(int,input()))

    count_numbers = [0] * 10

    for num in numbers:
        count_numbers[num] += 1
    
    max_count = my_max(count_numbers)

    for i in range(9, -1, -1):
        if count_numbers[i] == max_count:
            result = i
            break
        
    print('#%d %d %d' %((rounds + 1), (result), (max_count)))



