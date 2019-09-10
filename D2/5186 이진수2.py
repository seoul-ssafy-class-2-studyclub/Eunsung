for ro in range(int(input())):
    num = float(input())

    res = []

    c = -1
    while num > 0 and c >= -14:
        if num >= 2 ** c:
            res.append('1')
            num -= 2 ** c
        else:
            res.append('0')

        
        print(num)
        
        c -= 1
    if len(res) >= 13:
        res = ['overflow']

    print('#%d %s' %(ro + 1, ''.join(res)))

        
        