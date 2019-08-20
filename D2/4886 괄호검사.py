for ro in range(int(input())):
    words = input()
    stack = []

    set1 = ['{']
    result = 1

    for letter in words:
        if letter == '{' or letter == '(':
            stack.append(letter)
        

        elif letter == '}':
            if len(stack) == 0 or stack[-1] != '{':
                result = 0
                break
            else:
                stack.pop()
        elif letter == ')':
            if len(stack) == 0 or stack[-1] != '(':
                result = 0
                break
            else:
                stack.pop()
    if len(stack) != 0:
        result = 0

    print('#%d %d' %(ro + 1, result))
    
    