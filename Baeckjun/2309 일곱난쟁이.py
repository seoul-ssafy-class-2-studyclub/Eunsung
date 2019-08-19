shorts = []
keys = 0
for _ in range(9):
    key = int(input())
    keys += key
    shorts.append(key)
shorts.sort()

goal = keys - 100
    
a = 0
b = 0
for n1 in range(8):
    
    a = shorts[n1]
    for n2 in range(n1 + 1, 9):
        if a + shorts[n2] == goal:
            b = shorts[n2]
            break
    if b:
        break
for n in shorts:

    if n != a and n != b:
        print(n)


