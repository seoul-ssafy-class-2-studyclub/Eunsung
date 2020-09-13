def solution(A):
    combinations = []
    def bfs(idx, string):
        if idx >= len(A):
            combinations.append(string)
            return
        
        bfs(idx + 1, string + A[idx])
        bfs(idx + 1, string)
    
    bfs(0, '')
    max_length = 0
    for s in combinations:
        flag = 1
        result = [0] * 30

        for letter in s:
            result[ord(letter) - ord('a')] += 1
            if result[ord(letter) - ord('a')] > 1:
                flag = 0
                break
        
        if flag:
            if max_length < len(s):
                max_length = len(s)
    return max_length

print(solution(['aa']))
