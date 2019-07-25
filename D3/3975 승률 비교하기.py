results = []

for rounds in range(int(input())):

    result = 'BOB'
    a, b, c, d = map(int,(input().split()))
    A = a * d - b * c
    
    if not A:
        result = 'DRAW'
    elif A > 0:
        result = 'ALICE'
       
    results.append(f'#{rounds + 1} {result}')
print('\n'.join(results))    
    
