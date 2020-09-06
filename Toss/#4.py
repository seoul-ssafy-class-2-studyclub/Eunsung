# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 기억을 저장하는 linked_list 생성
class mem:
    def __init__(self, data, before=None, next=None):
        self.before = before
        self.next = next
        self.data = data

user_input = input()

# 인풋을 리스트 형식으로 정제
inputs = user_input.split()

# 시작 기억을 빈값으로 선정
head = mem('')

# 시작 before 를 헤드로 설정
before = head
for bank in inputs:
    tmp_node = mem(bank)
    before.next = tmp_node
    tmp_node.before = before

    # 최신 기억부터 출력하기
    tmp_mem = tmp_node
    
    mem_list = [''] * 5
    length_of_mem = 0
    while tmp_mem.before != None: # 전 결제 수단이 있을때까지
        # 5개 넘으면 브레이크
        if length_of_mem >= 5:
            break

        if tmp_mem.data in mem_list: # 이미 최근 결제수단에 있을 경우 컨티뉴
            tmp_mem = tmp_mem.before
            continue
        else:
            #기억에 저장하고 컨티뉴
            mem_list[length_of_mem] = tmp_mem.data
            length_of_mem += 1
            tmp_mem = tmp_mem.before
            continue
       
    print(' '.join(mem_list))
    # before 을 현재 node로 변경 후 컨티뉴
    before = tmp_node