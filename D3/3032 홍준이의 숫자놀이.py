result = []
for rounds in range(int(input())):
    B , A = map(int,input().split())
    y = 1
    while True:
        if not (-B * y + 1) % A:
            break
        y += 1
    x = (-B * y + 1) // A

    result.append(f'#{rounds + 1} {y} {x}')  

for value in result:
    print(value)