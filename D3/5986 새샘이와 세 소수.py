demical_num = []

def check_num(num):
    for i in range(2,int(num/2) + 1):
        if num % i == 0 :
            return False
    return True

for i in range(2,1000):
    if check_num(i):
        demical_num.append(i)
        
for rounds in range(int(input())):
    goal = int(input())

    count = 0

    for i in range(len(demical_num)):
        for j in range(i, len(demical_num)):
            if goal - (demical_num[i] + demical_num[j]) in demical_num[j:]:
                count += 1

    print(f'#{rounds + 1} {count}')
