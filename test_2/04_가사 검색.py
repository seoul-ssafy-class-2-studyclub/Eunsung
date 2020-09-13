def solution(words, queries):

    class Char:

        def __init__(self, char=''):
            self.char = char
            self.cnt = {}
            self.nexts = {}
        
        def append_next(self, char, remainder):
            
            if self.nexts.get(char):
                pass
            else:
                self.nexts[char] = Char(char)
                
            if self.cnt.get(remainder):
                self.cnt[remainder] += 1
            else:
                self.cnt[remainder] = 1

    start_of_forward = Char()
    start_of_backward = Char()

    for word in words:
        
        length = len(word)
        tmp_forward_char = start_of_forward
        tmp_backward_char = start_of_backward

        for idx in range(length):
            tmp_forward_char.append_next(word[idx], length - idx)
            tmp_forward_char = tmp_forward_char.nexts[word[idx]]
            
            tmp_backward_char.append_next(word[length - idx - 1], length - idx)
            tmp_backward_char = tmp_backward_char.nexts[word[length - idx - 1]]

    length_queries = len(queries)
    answer = [0] * length_queries
    dp = {}
    for qi in range(length_queries):
        query = queries[qi]
        if dp.get(query != None):
            answer.append(dp[query])
            continue
        

        start = ''
        query_length = len(query)
        goal_word = query

        if query[0] == '?':
            start = start_of_backward
            for i in range(query_length):
                c = goal_word[query_length - i - 1]
                if c != '?':
                    if start.nexts.get(c):

                        start = start.nexts[c]
                    else:
                        answer[qi] = 0
                        break
                else:
                    if start.cnt.get(query_length - i):
                        answer[qi] = (start.cnt[query_length - i])
                        dp[query] = answer[qi]
                    else:
                        answer[qi] = (0)
                        dp[query] = 0
                    break  

        else:
            start = start_of_forward
            for i in range(query_length):
                c = goal_word[i]
                if c != '?':
                    if start.nexts.get(c):

                        start = start.nexts[c]
                    else:
                        answer[qi] = 0
                        dp[query] = 0
                        break
                else:
                    if start.cnt.get(query_length - i):
                        answer[qi] = (start.cnt[query_length - i])
                        dp[query] = answer[qi]
                    else:
                        answer[qi] = (0)
                        dp[query] = 0
                    break    

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))