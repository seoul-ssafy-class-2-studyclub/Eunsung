def check(arr):
    if list(arr) == list(range(1, N + 1)):
        return True
    if list(arr) == list(range(N, 0, -1)):
        return True
    return False

def shuffle(tup, x):

    arr = list(tup)

    for _ in range(x):
        temp = []
        for i in range(N - 1):
            if arr[i] in left_deck and arr[i + 1] in right_deck:
                temp.append((i, i + 1))
        for (c1, c2) in temp:
            arr[c1], arr[c2] = arr[c2], arr[c1]
                
    return tuple(arr)

for ro in range(int(input())):
    cache = {}
    N = int(input())
    card_list = tuple(map(int,input().split()))

    queue = [(card_list, 0)]
    
    result = -1
    while True:
        if not queue:
            break
        temp = queue.pop(0)
        if check(temp[0]):
            result = temp[1]
            break

        if temp[1] > 5:
            break
        
        if cache.get(temp[0]) == None:
            cache[temp[0]] = True        
            for x in range(1, N - 1):
                left_deck = temp[0][:N // 2]
                right_deck = temp[0][N // 2:]
                queue.append((shuffle(temp[0], x), temp[1] + 1))
            
    
    print('#%d %d' %(ro + 1, result))
