result_list = []
for _ in range(int(input())):
    A_count = [0,0,0,0,0]
    B_count = [0,0,0,0,0]

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    for a in range(1,A[0] + 1):
        A_count[A[a]] += 1
    for b in range(1,B[0] + 1):
        B_count[B[b]] += 1
    
    result = 'D'
    for number in range(4,0,-1):
        if A_count[number] > B_count[number]:
            result = 'A'
            break
        elif A_count[number] < B_count[number]:
            result = 'B'
            break
    result_list.append(result)
for value in result_list:
    print(value)
    
        

    
