import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

population = int(input())
relation = [[0 for _ in range(population + 1)] for _ in range(population + 1)]


for i in range(int(input())):
    rel = input().split()
    if rel[0] == 'E':
        relation[int(rel[2])][int(rel[1])] = -1
    else:
        relation[int(rel[2])][int(rel[1])] = 1

# pprint(relation)
count = 1
while count > 0:
    count = 0
    for y in range(1,population + 1):
        for x in range(y):
            if relation[y][x]:
                for temp in range(y+1,population + 1):
                    if relation[temp][x] == relation[y][x] and not relation[temp][y]:
                        relation[temp][y] = 1
                        count += 1



for y in range(1,population + 1):
    for x in range(y):
        relation[x][y] = relation[y][x]


team = [[1]]

for player in range(2,population + 1):
    inp = True
    for each in team:
        for friend in each:
            if relation[player][friend] == 1:
                each.append(player)
                inp = False
                break
        if not inp:
            break

    if inp:
        team.append([])
        team[-1].append(player)
print(len(team))