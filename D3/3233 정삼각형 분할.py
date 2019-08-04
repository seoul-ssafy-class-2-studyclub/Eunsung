result = []
for rounds in range(int(input())):
    a, b = map(int,input().split())
    triangle = int((a//b) ** 2)

    result.append(f'#{rounds + 1} {triangle}')

for value in result:
    print(value)