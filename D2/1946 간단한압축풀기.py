for rounds in range(int(input())):

    N = int(input())
    words = {}
    letters = []
    for num in range(N):
        i, words[i] = map(lambda x: x if 'A'<=x<='Z' else int(x),input().split())
        for letter_num in range(words[i]):
            letters.append(i)

    print(f'#{rounds + 1}')

    for tens in range((len(letters)-1)//10+1):
        for o in range(10):
            try:
                print(letters[o + tens * 10], end = '')
            except:
                break
        print('')
