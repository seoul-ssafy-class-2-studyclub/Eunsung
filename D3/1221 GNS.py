numbers = {
    'ZRO' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOR' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SVN' : 7,
    'EGT' : 8,
    'NIN' : 9,
}



def my_append(arr, atom):
    arr += [atom]
    return arr



for rounds in range(int(input())):
    T, N = input().split()
    words = input().split()

    number_set = [[] for _ in range(10)]

    for i in range(int(N)):
        number_set[numbers[words[i]]] = my_append(number_set[numbers[words[i]]], words[i])
    
    result = []
    for i in range(10):
        result += number_set[i]

    result_str = result[0]


    print('%s' %T)
    for i in range(1, int(N)):
        result_str += ' ' + result[i]
    print(result_str)
        

        