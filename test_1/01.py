def solution(new_id):
    answer = ''

    # 변경이 쉽도록 리스트화
    new_id = list(new_id)

    for i in range(len(new_id)):
        # 1단계 변환
        if 'A' <= new_id[i] <= 'Z':
            new_id[i] = chr(ord(new_id[i]) - ord('A') + ord('a'))
        if not 'a' <= new_id[i] <= 'z' and not '0' <= new_id[i] <= '9' and new_id[i] not in ['-', '_', '.']:
            new_id[i] = ''
    
    new_id = list(''.join(new_id))

    idx_dot = -2
    for i in range(len(new_id)):    
        if new_id[i] == '.':
            if idx_dot + 1 == i:
                new_id[i] = ''
            
            idx_dot = i

    new_id = list(''.join(new_id))
    if not new_id:
        new_id = ['a']

    if new_id[0] == '.': new_id = new_id[1:]
    if not new_id:
        new_id = ['a']
    if new_id[-1] == '.': new_id = new_id[:-1]

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    if not new_id:
        new_id = ['a']

    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    answer = ''.join(new_id)
    return answer

print(solution("=.="))