def solution(S):
    leftword = ''
    rightword = ''
    N = len(S)
    for i in range(N // 2):
        if S[i] == '?' and S[-1-i] == '?':
            leftword += 'a'
            rightword = 'a' + rightword
        elif S[i] == '?' and not S[-1-i] == '?':
            leftword += S[-1-i]
            rightword = S[-1-i] + rightword
        elif not S[i] == '?' and S[-1-i] == '?':
            leftword += S[i]
            rightword = S[i] + rightword
        elif S[i] != S[-1-i]:
            return 'No'
        else:
            leftword += S[i]
            rightword = S[-1-i] + rightword
    if N % 2:
        if S[N//2] == '?':
            leftword += 'a'
        else:
            leftword += S[N//2]
    return leftword + rightword

print(solution('bab??a'))