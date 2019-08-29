for ro in range(int(input())):
    N, M = map(int,input().split())
    num_list = list(map(int,input().split()))

    na = M % N

    print('#%d %d' %(ro + 1, num_list[na]))
