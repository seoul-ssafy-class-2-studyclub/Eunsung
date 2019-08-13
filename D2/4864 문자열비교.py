for round in range(int(input())):
    str1 = input()
    str2 = input()

    result = 0

    for j in range(len(str2)-len(str1)+1):
        if str1[0] == str2[j]:
            for i in range(1,len(str1)):
                if str1[i] != str2[j + i]:
                    break
                elif i == len(str1) - 1:
                    result = 1
        if result == 1:
            break
    
    print('#%d %d' %(round + 1, result))
