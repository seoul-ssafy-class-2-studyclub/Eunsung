for rounds in range(int(input())):
    N = int(input())
    numbers = list(map(int,input().split()))

    i = N - 1
    while i > 0:
        if numbers[i] != max(numbers[:i + 1]):
            numbers.remove(max(numbers[:i + 1]))
            i -= 1
        i -= 1
    print(numbers)


