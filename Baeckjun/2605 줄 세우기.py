N = int(input())
students = list(map(str,range(1,N + 1)))
lotto = list(map(int,input().split()))

for i in range(1, N):
    temp = students[i]
    if lotto[i] > 0:
        for change in range(0, lotto[i]):
            students[i - change] = students[i - change - 1]
        students[i - lotto[i]] = temp
        
        
print(' '.join(students))
