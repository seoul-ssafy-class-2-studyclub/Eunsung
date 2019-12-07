# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C, D):
    numbers = [A, B, C, D]
    results = set()
    visited = [False] * 4
    def permu(now, arr):
        if len(arr) == 4:
            result = 1000 * arr[0] + 100 * arr[1] + 10 * arr[2] + arr[3]

            if 0 <= result < 2000:
                if arr[2] <= 6:
                    results.add(result)
        
            elif result <= 3000:
                if arr[1] < 4 and arr[2] <= 6:
                    results.add(result)

        for nxt in range(4):
            if visited[nxt]:
                continue
            visited[nxt] = True
            permu(nxt, arr + [numbers[nxt]])
            visited[nxt] = False
    
    for i in range(4):
        visited[i] = True
        permu(i, [numbers[i]])
        visited[i] = False
    
    return len(results)