def makebi(M):
    M = M.replace('0','0000')
    M = M.replace('1','0001')
    M = M.replace('2','0010')
    M = M.replace('3','0011')
    M = M.replace('4','0100')
    M = M.replace('5','0101')
    M = M.replace('6','0110')
    M = M.replace('7','0111')
    M = M.replace('8','1000')
    M = M.replace('9','1001')
    M = M.replace('A','1010')
    M = M.replace('B','1011')
    M = M.replace('C','1100')
    M = M.replace('D','1101')
    M = M.replace('E','1110')
    M = M.replace('F','1111')
    return M

for ro in range(int(input())):
    N, num = input().split()
    
    bi_num = makebi(num)

    print('#%d %s' %(ro + 1, bi_num))