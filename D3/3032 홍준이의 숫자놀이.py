def uclid(A, B):
    x = 1
    while (A * x) % B != 1:
        x += 1
        if x > 100:
            x = -100
            break
    return x

result = []
for rounds in range(int(input())):
    A , B = map(int,input().split())
    
    x = uclid(A, B)

    y = - (x * A - 1) // B

    temp_result = ' '.join([str(x), str(y)])

    if x == -100:
        temp_result = '-1'

    result.append('#%d %s' %(rounds + 1, temp_result))
    

for value in result:
    print(value)