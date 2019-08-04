from math import sqrt

for rounds in range(int(input())):
    goal_num = int(input())
    count = 0


    for i in range(1,int(sqrt(2 * goal_num)+1)):
        if not (goal_num - i*(i-1) // 2) % i:
            count +=1
    print(count)