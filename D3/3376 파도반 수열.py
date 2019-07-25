padoban = []
for i in range(100):
    if i <= 2:
        padoban.append(1)
    elif i <= 4:
        padoban.append(2)
    else:
        padoban.append(padoban[i - 1] + padoban[i - 5])

results = []
for rounds in range(int(input())):
    num = int(input())

    results.append(f'#{rounds + 1} {padoban[num - 1]}')

print('\n'.join(results))
