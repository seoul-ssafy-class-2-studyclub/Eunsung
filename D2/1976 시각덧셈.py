import math

for test_round in range((int(input()))):

    hour_f, minu_f, hour_s, minu_s = tuple(map(int,input().split()))
    
    result_h = hour_f + hour_s
    result_m = minu_f + minu_s
    
    if minu_f + minu_s >= 60:
        result_h += 1
        result_m -= 60
    
    if result_h % 12 == 0:
        result_h = 12
    else:
        result_h %= 12

    
    print(f'#{test_round + 1} {result_h} {result_m}')