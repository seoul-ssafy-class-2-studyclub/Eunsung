# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    dic = dict()
    cnt = 1
    for s in S:
        if dic.get(s) != None:
            dic = dict()
            cnt += 1
            dic[s] = 1
            continue
        
        else:
            dic[s] = 1
    
    return cnt