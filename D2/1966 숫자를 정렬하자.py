for rounds in range(int(input())):

    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort()    
    numbers= list(map(str,numbers))
    print(f'#{rounds+1}', end = ' ')
    print(' '.join(numbers))
