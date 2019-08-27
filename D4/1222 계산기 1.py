def cal(a,b,eq):
    if eq == '-':
        return a - b

    elif eq == '+':
        return a + b

    elif eq == '*':
        return a * b

    elif eq == '/':
        return a // b

seq = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
}

for ro in range(10):
    N = int(input())
    list_a = input()
    list_b = []

    stack = []

    for letter in list_a:
        if '0' <= letter <= '9':
            list_b.append(int(letter))
        
        else:
            if letter == '(':
                stack.append('(')
            
            elif letter == ')':
                while True:
                    temp = stack.pop()
                    if temp == '(':
                        break
                    list_b.append(temp)
            else:
                if stack:
                    if seq[stack[-1]] > seq[letter]:
                        temp2 = stack[-1]
                        while seq[temp2] > seq[letter]:
                            
                            list_b.append(stack.pop())
                            if not stack:
                                break
                            temp2 = stack[-1]
                        stack.append(letter)
                    else:
                        stack.append(letter)
                else:
                    stack.append(letter)
    for _ in range(len(stack)):
        list_b.append(stack.pop())
 
    result = 0
    stack2 = []

    for letter in list_b:
        if type(letter) == int:
            stack2.append(letter)
        
        else:
            b = stack2.pop()
            a = stack2.pop()

            re = cal(a,b,letter)
            stack2.append(re)
    print('#%d %d' %(ro + 1, re))
