N = int(input())

length = 1
num_list = [N]
for i in range(N // 2, N + 1):
    temp_num_list = [N]
    temp_num_list.append(i)
    temp = N - i
    while temp >= 0:
        temp_num_list.append(temp)
        temp = temp_num_list[-2] - temp_num_list[-1]
    
    temp_length = len(temp_num_list)
    if temp_length > length:
        length = temp_length
        num_list = temp_num_list
num_list = list(map(str,num_list))
print(length)
print(' '.join(num_list))


