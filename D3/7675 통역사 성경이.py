def check(string):
    for letter_num in range(len(string)):
        if letter_num == 0:
            if not('A'<=string[letter_num]<='Z'):
                return False
        else:
            if not('a'<=string[letter_num]<='z'):
                return False
    return True

for rounds in range(int(input())):

    N = int(input())
    words = input().replace('.', '^').replace('!', '^').replace('?', '^').split('^')
    words.pop()

    print(f'#{rounds + 1}', end= ' ')

    for i in range(N):
        words[i] = words[i].split()
    
    
    for i in range(N):
        count = 0
        for j in range(len(words[i])):
            if check(words[i][j]):
                count += 1
        print(count, end = ' ')
    
    print('')
