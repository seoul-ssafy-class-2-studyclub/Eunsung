N = int(input())
num_list = list(map(int,input().split()))

new_nums = []
count_nums = []

temp_down = 1
temp_up = 1
max_down = 1
max_up = 1

for num in range(len(num_list)):
    if num == 0:
        continue
    
    if num_list[num - 1] < num_list[num]:
        temp_down = 1
        temp_up += 1
        if temp_up > max_up:
            max_up = temp_up
    
    elif num_list[num - 1] > num_list[num]:
        temp_up = 1
        temp_down += 1
        if temp_down > max_down:
            max_down = temp_down
    else:
        temp_down += 1
        temp_up += 1
        if temp_down > max_down:
            max_down = temp_down
        if temp_up > max_up:
            max_up = temp_up
print(max(max_down, max_up))


# count_list = [0 for _ in range(N + 1)]
# max_length = 0
# for i in range(1,N + 1):
#     temp = 0
#     for j in range(i):
#         if num_list[i] >= num_list[j] and count_list[j] > temp:
#             temp = count_list[j]
#     count_list[i] = temp + 1
#     if max_length < count_list[i]:
#         max_length = count_list[i]

# print(max_length)
