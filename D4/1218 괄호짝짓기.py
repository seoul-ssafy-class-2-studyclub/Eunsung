opens = ['{', '[', '(', '<']
closes =  ['}', ']', ')', '>']

for rounds in range(1,11):
    result = 0
    N = int(input())
    words = input()
    count = 0
    
    for start_index in range(N):
        for kind in range(4):
            if words[start_index] == opens[kind]:
                for l in range(start_index,N):
                    if words[l] == closes[kind]:
                        count += 2
                        break
    if count == N:
        result = 1

        for kind in range(4):
            if words.count(opens[kind]) != words.count(closes[kind]):
                result = 0
                break
        
    print(f'#{rounds} {result}')
