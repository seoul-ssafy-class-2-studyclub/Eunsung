for rounds in range(int(input())):
    words = list(input())
    moeum = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(words)-1, -1, -1):
        if words[i] in moeum:
            words.pop(i)
    print(f'#{rounds + 1} ' + ''.join(words))