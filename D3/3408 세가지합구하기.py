results = []

for rounds in range(int(input())):
    
    result = []

    N = int(input())
    result.append(str(N*(N+1)//2))
    result.append(str(N**2))
    result.append(str(N**2+N))

    results.append(f'#{rounds + 1} {" ".join(result)}')

print('\n'.join(results))