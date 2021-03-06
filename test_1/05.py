def solution(play_time, adv_time, logs):
    answer = ''

    time_info = {}
    play_time = int(''.join(play_time.split(':')))
    adv_time = int(''.join(adv_time.split(':')))
    def is_time_ok(time):
        a= time
        if (time % 100) >= 60:
            time += 40

        if (time % 10000) // 100 >= 60:
            time += 4000
        if time >= play_time:
            return play_time + 1
        return time
    
    def time_delta(time1,  time2):
        
        a1,b1,c1 = str(time1 // 10000), str((time1 % 10000) // 100), str(time1 % 100)
        a2,b2,c2 = str(time2 // 10000), str((time2 % 10000) // 100), str(time2 % 100)

        if int(c1) < int(c2):
            c1 = str(int(c1) - (60 - int(c2)))
            b1 = str((int(b1) - 1) % 60)
        
        if int(b1) < int(b2):
            b1 = str(int(b1) - (60 - int(b2)))
            a1 = str((int(a1) - 1))
        a = a1 + b1 + c1
        print(a)
        return int(a)


    for log in logs:
        start_end = log.split('-')
        start = start_end[0].split(':')
        end = start_end[1].split(':')
        start = 10000 * int(start[0]) + 100 * int(start[1]) + int(start[2])
        end = 10000 * int(end[0]) + 100 * int(end[1]) + int(end[2])
        if time_info.get(start):
            time_info[start]['start'] += 1
        else:
            time_info[start] = {'start' : 1, 'end' : 0}

        if time_info.get(is_time_ok(end + 1)):
            time_info[is_time_ok(end + 1)]['end'] += 1
        else:
            time_info[is_time_ok(end + 1)] = {'start' : 0, 'end' : 1}

    adv_play = 0
    adv_start = 0
    max_adv_start = 0
    adv_cnt = 0
    max_adv_cnt = 0
    now_view = 0

    view_logs = [0] * 1000001
    for t in range(play_time + 1):
        if (t % 10000) // 100 >= 60 or (t % 100) >= 60:
            continue
        if time_info.get(t):
            now_view += time_info[t]['start']
            now_view -= time_info[t]['end']
        
        view_logs[t] = now_view

        if t <= adv_time:
            adv_cnt += now_view
        
        else:
            adv_cnt += now_view
            adv_cnt -= view_logs[time_delta(t, adv_time + 1)]
            if max_adv_cnt < adv_cnt:
                max_adv_cnt = adv_cnt
                max_adv_start = time_delta(t, adv_time)

    max_adv_start = str(max_adv_start)
    if len(max_adv_start) < 6:
        max_adv_start = '0' * (6 - len(max_adv_start)) + max_adv_start
    answer = max_adv_start[:2] + ':' + max_adv_start[2:4] + ':' + max_adv_start[4:]
    return answer

print(solution("99:59:59", "25:00:00", ["00:00:00-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))