def change_switch(switch):
    switch = 0 if switch else 1
    return switch
    
def mans_do(num):
    for i in range(num - 1, N, num):
        switchs[i] = change_switch(switchs[i])
def womans_do(num):
    switchs[num - 1] = change_switch(switchs[num - 1])
    j = 1
    while num - j >= 1 and num + j <= N and switchs[num - 1 - j] == switchs[num -1 + j]:
        switchs[num - 1 - j] = change_switch(switchs[num - 1 - j])
        switchs[num - 1 + j] = change_switch(switchs[num - 1 + j])
        j += 1


N = int(input())
switchs = list(map(int,input().split()))
P = int(input())
to_do = []
for i in range(P):
    A , D = map(int,input().split())
    if A % 2 :
        mans_do(D)
    else:
        womans_do(D)

for i in range(len(switchs)):
    print(switchs[i], end = ' ')
    if not (i + 1) % 20:
        print('')
