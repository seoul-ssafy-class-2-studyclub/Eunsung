N = int(input())

persons = []

sums_result = []
for i in range(N):
    persons.append(list(map(int,input().split())))
    max_sum = 0

    for x in range(3):
        for y in range(x + 1, 4):
            for z in range(y + 1, 5):
                temp = persons[i][x] + persons[i][y] + persons[i][z]
                if max_sum < temp % 10:
                    max_sum = temp % 10
    
    sums_result.append(max_sum)

result = 0
for x in range(N):
    if sums_result[x] >= sums_result[result]:
        result = x

print(result + 1)





