# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
input_of_kim_to_lee = input()
input_of_lee_to_kim = input()

# 인풋을 int 형이 담긴 list 로 바꿔준다

kim_to_lee = list(map(int, input_of_kim_to_lee))
lee_to_kim = list(map(int, input_of_lee_to_kim))

length = len(kim_to_lee)
# 김토스가 이토스에게 받을 돈 기록
mem_of_gap = 0
res = []

for i in range(length):
    # 김이 줄 돈 계산
    tmp_k_to_l = kim_to_lee[i] - (lee_to_kim[i] + mem_of_gap)
    if tmp_k_to_l >= 0:
        res.append(str(tmp_k_to_l))

        # 받을 돈이 없어짐
        mem_of_gap = 0

    else: # 줄 돈이 더 적다면
        # 돈을 못주고
        res.append('0')

        # 받을 돈이 늘어난다
        mem_of_gap = - tmp_k_to_l

print(' '.join(res))