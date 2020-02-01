def solution(A, B):
    
    result = [0] * 70
    A_binary = [0] * 30
    B_binary = [0] * 30

    def making_binary(num, num_binary):
        depth = 29
        while num > 0:
            if num >= (2 ** depth):
                num_binary[depth] = 1
                num -= (2 ** depth)
            depth -= 1
    making_binary(A, A_binary)
    making_binary(B, B_binary)

    for A_i in range(30):

        if not A_binary[A_i]:
            continue

        for B_i in range(30):
            if B_binary[B_i]:
                result[A_i + B_i] += 1
    cnt = 0
    for idx in range(60):
        if result[idx] > 1:
            temp = result[idx] // 2
            result[idx] %= 2
            result[idx + 1] += temp   
        
        if result[idx]:
            cnt += 1

    print(result)
    print(cnt)
    return cnt

solution(100000000, 100000000)
