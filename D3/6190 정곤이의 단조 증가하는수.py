# # def check_danjo(number):
# #     number = str(number)
# #     for i in range(len(number) - 1):
# #         if number[i] > number[i + 1]:
# #             return False
# #     return True

result = []
for rounds in range(int(input())):
    N = int(input())
    numbers = list(map(int,input().split()))
    times = sorted(set(x*y for x in numbers for y in numbers if x != y), reverse=True)
    
    max_danjo = -1

    for number in times:
        check = True
        number = str(number)
        for i in range(len(number) - 1):
            if number[i] > number[i + 1]:
                check = False
        if check == True:
            max_danjo = number
            break

    result.append(f'#{rounds + 1} {max_danjo}')
for value in result:
    print(value)


# for rounds in range(int(input())):
#     N = int(input())
#     numbers = list(map(int,input().split()))
#     times = sorted(set(x*y for x in numbers for y in numbers if x != y))
    
#     max_danjo = -1

#     for j in range(len(times)-1, 0, -1):
#         check = True
#         times[j] = str(times[j])
#         for i in range(len(times[j]) - 1):
#             if times[j][i] > times[j][i + 1]:
#                 check = False
#                 times.pop(j)
#         if check == True:
#             max_danjo = times[j]
#             break

#     print(f'#{rounds + 1} {max_danjo}')
