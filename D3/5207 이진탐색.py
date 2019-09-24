def binaryfind(l, r, before):
    global cnt
    if l > r or board[r] < num or num < board[l]:
        return

    m = (l + r) // 2
    
    if board[m] == num:
        cnt += 1
        return
    
    elif board[m] > num and before in [0, 1]:
        binaryfind(l, m - 1, 2)
    elif board[m] < num and before in [0, 2]:
        binaryfind(m + 1, r, 1)

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
    result = []

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
    N, M = map(int,input().split())
    board = list(map(int,input().split()))
    finded = list(map(int,input().split()))
    board = sorting(board)
    
    cnt = 0
    for num in finded:
        binaryfind(0, N - 1, 0)
    
    print('#%d %d' %(ro + 1, cnt))

