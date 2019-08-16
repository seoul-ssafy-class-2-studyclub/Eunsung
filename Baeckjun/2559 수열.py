days, goal = map(int,input().split())

degrees = list(map(int,input().split()))
degreesum = 0
for i in range(goal):
    degreesum += degrees[i]

max_degree = -100000000
if max_degree < degreesum:
    max_degree = degreesum

for i in range(goal, days):
    degreesum -= degrees[i - goal]
    degreesum += degrees[i]
    # print(temp_degrees)

    if max_degree < degreesum:
        max_degree = degreesum

print(max_degree)
    
    