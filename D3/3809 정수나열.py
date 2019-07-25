
def find_min(arr):

    for i in range(10):
        if not str(i) in set(sum_list):
            return i
    num = 2
    while num < N:
        board = [False] * 10 ** num
        for i in range(len(arr) - num + 1):
            board[int(''.join(arr[i:i + num]))] = True
    
        for number in range(10**(num-1), 10**num):
            if board[number] == False:
                return number
        num += 1
    

for rounds in range(int(input())):
    N = int(input())
    
    sum_list = []
    while len(sum_list) < N:
        sum_list.extend(list(input().split()))
    
    result = find_min(sum_list)

    print(f'#{rounds + 1} {result}')
