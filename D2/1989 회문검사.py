for text_round in range((int(input()))):
    words = list(input())
    leng = len(words)
    result = 0

    check = 0
    for letter in range(leng):
        if words[letter] == words[leng-letter-1]:
            check += 1
    if check == leng:
        result = 1

    print(f'#{text_round+1} {result}')
