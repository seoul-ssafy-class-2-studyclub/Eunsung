# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

# before을 2로, flag = True로 초기화한다. 첫 문자는 아무거나 나와도 상관 x
before = '2'
flag = 'true'

for num in user_input:

    # before 이 2라면 컨티뉴
    if before == '2':
        before = num
        continue
    # 1이라면 num == 1 이면 False
    else : 
        if num == '2':
            before = num
            continue
        else:
            flag = 'false'
            break

# 모두 통과했지만 마지막이 1인경우 false
if flag == 'true':
	if num == '1':
		flag = 'false'
print(flag)