N = int(input())

if N == 1:
    print(2)
    print(1)
    print(2)

else:
    tube_1 = [2 * N] + [i for i in range(1, N - 1)] + [2 * N - 1]
    tube_2 = [2 * N - 2] + [i for i in range(N - 1, 2 * N - 2)]

    sums = (2 * N) * (2 * N + 1) // 2
    cnt = 0


    for i in range(N):
        sums -= tube_2[N - 1 - i]
        cnt += sums * (i + 1)

    for i in range(N):
        sums -= tube_1[N - 1 - i]
        cnt += sums * (N + i + 1)
    tube_1 = ' '.join(list(map(str, tube_1)))
    tube_2 = ' '.join(list(map(str, tube_2)))
    print(cnt) 
    print(tube_1)
    print(tube_2)
    

