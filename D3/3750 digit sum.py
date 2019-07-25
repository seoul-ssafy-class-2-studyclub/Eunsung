def digit_sum(num):
    if len(num) == 1:
        return num
    digit = 0
    for i in range(len(num)):
        digit += int(num[i])
    return digit_sum(str(digit))
    

result = []
for rounds in range(int(input())):


    result.append(f'#{rounds + 1} {digit_sum(input())}')

print('\n'.join(result))
    