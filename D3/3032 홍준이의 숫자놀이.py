def uclid(x):
    if (A * x) % B == 1 or (A * x)  % B == -1:
        return (x, -(A * x // B))
    return uclid(x + 1)

result = []

for rounds in range(int(input())):
    A , B = map(int,input().split())
    
    x, y = uclid(1)

    result.append('#%d %d %d' %(rounds + 1, x, y))
    

for value in result:
    print(value)