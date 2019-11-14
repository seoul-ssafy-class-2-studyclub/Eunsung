
eq = ['+', '-', '*', '/']

def permu(arr, length, count):
    global min_v
    global max_v

    if length == N - 1:

        stack = [nums[0]]
        idx = 1
        while arr:
            ee = arr.pop(0)
            num2 = nums[idx]
            num1 = stack.pop(0)
            idx += 1
            res = equ(num1, num2, eq[ee])
            stack.append(res)

        if res < min_v:
            min_v = res
        if res > max_v:
            max_v = res
        return
    
    for idx in range(4):
        if count[idx] == eqs[idx]:
            continue
        count[idx] += 1
        permu(arr + [idx], length + 1, count)
        count[idx] -= 1

def equ(l,r,e):
    if e == '+':
        return l + r
    elif e == '-':
        return l - r
    elif e == '*':
        return l * r
    else:
        if l // r < 0 and l % r:
            return l // r + 1
        return l // r
    

for ro in range(int(input())):
    N = int(input())
    eqs = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    
    min_v = 100000001
    max_v = -100000001
    permu([], 0, [0, 0, 0, 0] )

    print('#%d %d' %(ro + 1, max_v - min_v))



