user_input = input()

# starting pointer 와 메모리를 구분하여 정수형태로 저장
user_input = user_input.split()
memory = list(map(int, user_input[1:]))

# starting_point 를 찾는다 ; 가 있으므로 마지막 글자 제외하여 추출 
starting_point = int(user_input[0][:-1])


# 복사할 메모리 생성 및 길이 체크 변수 추가
res = ['0'] * 8
length_of_res = 0
now_pointer = starting_point
# starting_point 부터 시작
while True:
    if memory[now_pointer] == 0:
        # 포인터가 가르키는 주소로 이동결과가 포인터라면, 
        res[length_of_res] = '0'
        # 복사한 주소값은 res 메모리의 길이가 되어야한다.
        res[length_of_res + 1] = (str(length_of_res + 2))
        # 그리고 새로운 포인터로 이동
        now_pointer = memory[now_pointer + 1]
        length_of_res += 2
        if length_of_res >= 8:
            # 결과의길이가 8을 넘어가면 메모리 초과 에러
            print('메모리 초과 에러')
            break
    else: # 포인터가 가르키는 주소로 이동결과가 값이라면
        # 1과 값을 결과에 추가하고 종료
        res[length_of_res] = '1'
        res[length_of_res + 1] = str(memory[now_pointer + 1])
        break
    
# 복사된 메모리는 항상 0; 으로 시작
print('0; ' + ' '.join(res))