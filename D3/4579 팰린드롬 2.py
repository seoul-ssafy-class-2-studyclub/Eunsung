for rounds in range(int(input())):
    word = list(input())
    word_reversed = list(reversed(word))
    
    if not '*' in word:
        if word == word_reversed:
            result = 'Exist'
        else:
            result = 'Not exist'
    else:
        location = min(word.index('*'), word_reversed.index('*'))
        if word[0:location] == word_reversed[0:location]:
            result = 'Exist'
        else:
            result = 'Not exist'

    print(f'#{rounds + 1} {result}')