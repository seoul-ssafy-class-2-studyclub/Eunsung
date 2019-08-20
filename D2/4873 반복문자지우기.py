for ro in range(int(input())):
    words = input()
    stack = [words[0]]

    for num in range(1, len(words)):
        if len(stack) != 0 and words[num] == stack[-1]:
            stack.pop()
        else:
            stack.append(words[num])

    print('#%d %d' %(ro + 1, len(stack)))
