def find_5(arr, min_result_list, max_result_list):
    min_num = arr[0]
    max_num = arr[0]
    max_index = 0
    min_index = 0
    for i in range(1, len(arr)):
        if min_num > arr[i]:
            min_num = arr[i]
            min_index = i
        if max_num < arr[i]:
            max_num = arr[i]
            max_index = i
    
    arr.remove(max_num)
    arr.remove(min_num)

    min_result_list.append(min_num)
    max_result_list.append(max_num)
    
    if len(min_result_list) == 5:
        return min_result_list, max_result_list
    return find_5(arr, min_result_list, max_result_list)
    

result_list = []
for round in range(int(input())):
    N = int(input())
    numbers = list(map(int,input().split()))

    maxs = []
    mins = []

    mins, maxs = find_5(numbers, mins, maxs)

    result = []
    for i in range(5):
        result.append(maxs[i])
        result.append(mins[i])
    result = list(map(str,result))
    result_list.append('#%d %s' %(round + 1, ' '.join(result)))
for value in result_list:
    print(value)
