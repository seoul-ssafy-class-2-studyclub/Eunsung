results = []

for rounds in range(int(input())):
    
    result = -1
    L, U, X = map(int,input().split())
    if X < L:
        result = L - X
    elif L <= X <= U:
        result = 0
    
    results.append(f'#{rounds + 1} {result}')
print('\n'.join(results))

