def cal(a,b,eq):
    if eq == '-':
        return a - b

    elif eq == '+':
        return a + b

    elif eq == '*':
        return a * b

    elif eq == '/':
        return a // b

for ro in range(int(input())):
    sic = input().split()

    stack = []

    for letter in sic:
        if '0' <= letter <= '9':
            stack.append(int(letter))
        elif letter == '.':
            if len(stack) == 1:
                result = stack[-1]
            else:
                result = 'error'
                
        else:
            if len(stack) < 2:
                result = 'error'
                break
                
            else:

                b = stack.pop()
                a = stack.pop()
                re = cal(a, b, letter)
                stack.append(re)
    result = str(result)            
    print('#%d %s' %(ro + 1, result))