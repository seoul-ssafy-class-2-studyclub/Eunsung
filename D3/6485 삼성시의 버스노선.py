for rounds in range(int(input())):
    counts = []

    for i in range(5001):
        counts.append(0)

    N = int(input())
    for case in range(N):
        start_num, end_num = map(int,input().split())
        for count in range(start_num, end_num+1):
            counts[count] += 1
    P = int(input())
    print(f'#{rounds + 1}', end = ' ')
    for say in range(P):
        c = int(input())
        print(f'{counts[c]}', end = ' ')
    print('')
