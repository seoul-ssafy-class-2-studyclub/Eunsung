T = int(input())
pascal = [[]]

for i in range(T):
    n = int(input())
    print(f'#{i+1}')
    for m in range(n-1):
        pascal.append([])
    for l in range(n):
        for k in range(l+1):
            if (l == 0) or (k == 0) or (k == l):
                pascal[l].append(1)
            else :
                pascal[l].append(pascal[l-1][k-1]+pascal[l-1][k])
            print(pascal[l][k], end = ' ')
        print('')

    
    pascal = [[]]
