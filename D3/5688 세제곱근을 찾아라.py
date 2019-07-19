import math

for rounds in range(int(input())):
    cubic = int(input())

    k = cubic ** (1/3)

    upper = math.ceil(k)
    under = math.floor(k)

    if upper ** 3 == cubic:
        result = upper
    elif under ** 3 == cubic:
        result = under
    else:
        result = -1

    print(f'#{rounds + 1} {result}')

     


    