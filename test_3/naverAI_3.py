# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    check = [0, 0]
    total = len(A)
    for i in range(total):
        if not (i % 2):
            if A[i] == 1:
                check[0] += 1
            elif A[i] == 0:
                check[1] += 1
        else:
            if A[i] == 1:
                check[1] += 1
            elif A[i] == 0:
                check[0] += 1
    
    return (total - max(check))

print(solution([1,1,1]))