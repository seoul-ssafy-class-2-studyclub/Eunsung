import sys
sys.stdin = open('input.txt', 'r')

result = []
for round in range(int(input())):
    number, K = input().split()
    K = int(K)

    numbers = {}
    for i in range(len(number)):
        numbers[i] = int(number[i])
    
    print(numbers)