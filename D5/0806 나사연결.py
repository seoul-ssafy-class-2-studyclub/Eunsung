result = []
for round in range(int(input())):
    N = int(input())
    bolt_list = list(map(int,input().split()))
    bolts = []
    for i in range(N):
        bolts.append((bolt_list[i * 2], bolt_list[i * 2 + 1]))
    
