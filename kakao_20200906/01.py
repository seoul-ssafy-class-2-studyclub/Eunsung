def solution(s):

    string_length = len(s)
    
    min_length = string_length
    res = '#'
    # 자를 수있는 범위에 대해서 반복, 전체길이의 절반이상을 자르면 의미가 없다
    for i in range(1, string_length // 2 + 1):

        tmp_str = []
        for start in range(string_length // i + 1):
            if not s[i * start : i * start+i] : continue
            tmp_str.append(s[i * start : i * start+i])

        result_str = ''
        before_word = tmp_str[0]
        same_word_cnt = 1
        for idx in range(1, len(tmp_str)):
            if tmp_str[idx] == before_word:
                same_word_cnt += 1
                if idx == len(tmp_str) - 1:
                    result_str += str(same_word_cnt) + tmp_str[idx]
                continue
            else:
                if same_word_cnt == 1:
                    result_str += before_word
                    before_word = tmp_str[idx]
                    if idx == len(tmp_str) - 1:
                        result_str += tmp_str[idx]
                    continue
                else:
                    result_str += str(same_word_cnt) + before_word
                    before_word = tmp_str[idx]
                    same_word_cnt = 1
                    if idx == len(tmp_str) - 1:
                        result_str += tmp_str[idx]
                    continue
        
        if min_length >= len(result_str):
            min_length = len(result_str)
            res = result_str
        
    return min_length


print("#1 aabbaccc")
print(solution("aabbaccc"))   
print("#2 ababcdcdababcdcd")
print(solution("ababcdcdababcdcd"))   
print("#3 abcabcdede")
print(solution("abcabcdede"))   
print("#4 abcabcabcabcdededededede")
print(solution("abcabcabcabcdededededede"))   
print("#5 xababcdcdababcdcd")
print(solution("xababcdcdababcdcd"))