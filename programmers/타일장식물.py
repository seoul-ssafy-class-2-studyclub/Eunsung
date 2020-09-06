def solution(N):

    a = [0, 1, 1] + [0] * N
    b = [0] + [0] * N
    
    for i in range(3, N + 2):
        a[i] = a[i - 1] + a[i - 2]
    for i in range(1, N + 1):
        b[i] = a[i] * 2 + a[i + 1]* 2

    answer = b[N]
    return answer

print(solution(5))