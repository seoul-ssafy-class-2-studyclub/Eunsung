def solution(p):
    answer = ''
    aside = {'(' : ')', ')': '('}

    def devide(string):
        # 짝수의 str만 주어지므로 
        for i in range(1, len(string) // 2 + 1):
            if is_balanced(string[:2 * i]):
                return string[:2 * i], string[2 * i:]

    def return_str(string):
        if is_right(string):
            return string
        
        res_str = ''
        u, v = devide(string)
        if is_right(u):
            res_str = u + return_str(v)
            return res_str
        else:
            tmp_str = '('
            tmp_str += return_str(v)
            tmp_str += ')'

            for idx in range(1, len(u) - 1):
                tmp_str += aside[u[idx]]

            return tmp_str

    def is_balanced(string):
        cnt_left = 0
        cnt_right = 0

        for char in string:
            if char == '(':
                cnt_left += 1
            else:
                cnt_right += 1

        if cnt_left == cnt_right:
            return True
        else:
            return False
    
    def is_right(string):
        cnt = 0 
        for char in string:
            if char == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
        if cnt == 0:
            return True
        return False

    return return_str(p)

aside = {'(' : ')', ')': '('}

print("#1 (()())()")
print(solution("(()())()"))
print("#2 )(")
print(solution(")("))
print("#3 ()))((()")
print(solution("()))((()"))


