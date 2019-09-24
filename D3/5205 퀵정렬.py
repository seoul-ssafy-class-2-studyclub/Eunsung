def quicksort(arr):
    global goal
    length = len(arr)
    if length <= 1:
        return arr
    
    pivot = arr[length // 3]
    l = []
    r = []
    m = []

    ll = 0
    lm = 0
    lr = 0

    for num in arr:
        if num == pivot:
            if not m:
                m = [num]
            else:
                m[-1:] = [m[-1], num]
            lm += 1
    
        elif num < pivot:
            if not l:
                l = [num]
            else:
                l[-1:] = [l[-1], num]
            ll += 1

        else:
            if not r:
                r = [num]
            else:
                r[-1:] = [r[-1], num]
            lr += 1
    
    if ll > goal:
        return quicksort(l)
    elif ll + lm > goal:
        goal -= ll
        return m
    else:
        goal -= ll + lm
        return quicksort(r)

for ro in range(int(input())):
    N = int(input())
    num_list = list(map(int,input().split()))
    goal = N // 2
    num_list = quicksort(num_list)
    

    print('#%d %d' %(ro + 1, num_list[goal]))