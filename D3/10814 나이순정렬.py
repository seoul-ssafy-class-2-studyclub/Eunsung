N = int(input())
name_list = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    name_list.append((age, name))
    name_list.sort(key= lambda x: x[0])

for value in name_list:
    print(f'{value[0]} {value[1]}')