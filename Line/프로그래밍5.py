def fact(num):
    if num == 0:
        return 1
        
    if num == 1:
        return num
    return num * fact(num - 1)

N, M = map(int,input().split())
X, Y = map(int,input().split())

if X > N or Y > M:
    result = ['fail']
else:
    result = [X + Y, fact(X + Y) // fact(X) // fact(Y)]

for re in result:
    print(re)