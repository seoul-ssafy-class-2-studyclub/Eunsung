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

def find_index(x, arr):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


for rounds in range(1,11):
    N = int(input())
    boxes = list(map(int,input().split()))

    for dump in range(N):
        max_height = my_max(boxes)
        min_height = my_min(boxes)
        max_index = find_index(max_height, boxes)
        min_index = find_index(min_height, boxes)

        boxes[max_index] -= 1
        boxes[min_index] += 1

    print('#%d %d'%(rounds, my_max(boxes) - my_min(boxes)))