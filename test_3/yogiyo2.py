# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    S = ''.join(''.join(S.split()).split('-'))
    
    result = ''
    if not len(S) % 3:
        for q in range(len(S) // 3):
            result += S[3 * q: 3 * (q + 1)] + '-'
        return result[:-1]
        
    elif len(S) % 3 == 2:
        last = 0
        for q in range(len(S) // 3):
            result += S[3 * q: 3 * (q + 1)] + '-'
            last = q
        result += S[3 * (last + 1) : 3 * (last + 1) + 2]
        return result
    else:
        last = 0
        for q in range(len(S) // 3 - 1):
            result += S[3 * q: 3 * (q + 1)] + '-'
            last = q
        
        result += S[3 * (last + 1) : 3 * (last + 1) + 2] + '-'
        result += S[3 * (last + 1) + 2 :]
        return result
    