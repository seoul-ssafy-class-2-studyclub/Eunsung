for rounds in range(int(input())):
    K, N, M = map(int,input().split())
    battery = list(map(int,input().split()))

    step = 0
    stop = False
    result = 0
    while step < N:
        for i in range(K,0,-1):
            if (step + i) >= N:
                step += i
                break
            if (step + i) in battery:
                step += i
                result += 1
                break
            if i == 1:
                stop = True
                break
        if stop:
            result = 0
            break

    print('#%d %d' %((rounds + 1), result))
    