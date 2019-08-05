result = []
for rounds in range(int(input())):
    N, M = map(int,input().split())
    
    words1 = input().split()
    words2 = input().split()

    wordbook = {}

    for i in range(N):
        wordbook[words1[i]] = i
    count = 0
    for value in words2:
        if wordbook.get(value, 'NOP') != 'NOP':
            count += 1
    
    result.append(f'#{rounds + 1} {count}')
for value in result:
    print(value)
