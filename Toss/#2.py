# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

# 인풋을 int 형이 담긴 list 로 바꿔준다
inputs = list(map(int, user_input.split()))

# before 를 0으로 초기화
before = 0
flag = 'true'
length = 0

for num in inputs:
    
    # input의 길이 체크
    length += 1

    # num 이 범위 밖에 있으면 false 후 브레이크
    if not 1 <= num <= 45:
        flag = 'false'
        break    

    # 오름차순이 아니라면 브레이크
    if num <= before:
        flag = 'false'
        break

    # 통과하면 before 을바꿔주고 컨티뉴
    before = num

#길이가 6이 아니라면 false
if length != 6:
    flag = 'false'
print(flag)