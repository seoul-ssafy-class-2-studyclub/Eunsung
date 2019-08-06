def binary_found(start, end, goal, count):
    middle = (start + end) //2
    if middle == goal:
        return count
    
    return binary_found(middle, end, goal, count + 1) if goal > middle else binary_found(start, middle, goal, count + 1)
    
result_list = []
for round in range(int(input())):
    page, pa, pb = map(int,input().split())

    result = 'A'

    A = binary_found(1, page, pa, 1)
    B = binary_found(1, page, pb, 1)

    if A > B:
        result = 'B'
    if A == B:
        result = '0'

    result_list.append('#%d %s' %(round + 1, result))

for value in result_list:
    print(value)
