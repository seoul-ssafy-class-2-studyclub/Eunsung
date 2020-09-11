def solution(record):

    nicknames = {}
    cnt = 0
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            nicknames[r[1]] = r[2]
            cnt += 1 
        elif r[0] == 'Change':
            nicknames[r[1]] = r[2]
        else:
            cnt += 1
    answer = [0] * cnt
    i = 0
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer[i] = f'{nicknames[r[1]]}님이 들어왔습니다.'
            i += 1
        elif r[0] == 'Leave':
            answer[i] = f'{nicknames[r[1]]}님이 나갔습니다.'
            i += 1


    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])