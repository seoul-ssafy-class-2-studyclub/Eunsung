def check_gin(arr, idx):
    if idx <= 1:
        return False

    if arr[idx - 1] and arr[idx - 2]:
        return True
    return False


for ro in range(int(input())):
    A = []
    B = []
    num_list = list(map(int,input().split()))
    for turn in range(12):
        if turn % 2:
            B.append(num_list[turn])
        else:
            A.append(num_list[turn])
    
    count_A = [0] * 10
    count_B = [0] * 10
    res = 0
    flag = 0
    for idx in range(6):
        count_A[A[idx]] += 1
        if count_A[A[idx]] >= 1:
            if check_gin(count_A, A[idx]):
                res = 1
                flag = 1
                
        if count_A[A[idx]]>= 3:
            res = 1
            flag = 1
            
        
        count_B[B[idx]] += 1
        if count_B[B[idx]] >= 1:
            if check_gin(count_B, B[idx]):
                res = 2
                if flag:
                    res = 0
                    print('@@@@')
                    print(idx)
                break
        if count_B[B[idx]] >= 3:
            res = 2
            if flag:
                res = 0
                print('!!!')
            break
    print(A)
    print(B)
    print(count_A)
    print(count_B)
    print('#%d %d' %(ro + 1, res))
        
