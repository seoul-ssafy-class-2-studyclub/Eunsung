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

for rounds in range(int(input())):
    T, N = input().split()
    words = input().split()

    words.sort(key=lambda x: numbers[x])

    print(f'{T}\n{" ".join(words)}')
        