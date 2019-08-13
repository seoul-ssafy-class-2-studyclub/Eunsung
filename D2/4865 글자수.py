for round in range(int(input())):
    str1 = input()
    str2 = input()

    length = len(str1)

    count = [0 for _ in range(length)]
    max_count = 0

    for i in range(length):
        for l in range(len(str2)):
            if str1[i] == str2[l]:
                count[i] += 1
        if max_count < count[i]:
            max_count = count[i]
                
    
    print('#%d %d' %(round + 1, max_count))