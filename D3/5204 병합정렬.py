def sorting(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = sorting(left)
    right = sorting(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            if not result:
                result.append(left[i])
                
            else:
                result[-1:] = [result[-1], left[i]]
            i += 1
        else:
            if not result:
                result.append(right[j])
            else:
                result[-1:] = [result[-1], right[j]]
            j += 1
    
    if i < len(left):
        result[-1:] = [result[-1]] + left[i:]
    elif j < len(right):
        result[-1:] = [result[-1]] + right[j:]

    return result

for ro in range(int(input())):
    N = int(input())
    num_list = list(map(int,input().split()))
    cnt = 0
    res = sorting(num_list)

    print('#%d %d %d' %(ro + 1, res[N // 2], cnt))