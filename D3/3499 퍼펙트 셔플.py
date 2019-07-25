for rounds in range(int(input())):

    N = int(input())
    words = list(input().split())

    words_first = []
    words_second = []

    for i in range(N-1, -1, -1):
        if i < N / 2:
            words_first.append(words.pop())
        else:
            words_second.append(words.pop())
    for i in range(N // 2):
        words.append(words_first.pop())
        words.append(words_second.pop())
    if words_first:
        words.append(words_first.pop())

    print(f'#{rounds + 1} {" ".join(words)}')
     