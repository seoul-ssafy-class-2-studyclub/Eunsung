def quicksort(numbers):
    if len(numbers) <= 1: return numbers
    left = []
    right = []
    mid = []
    pivot = numbers[len(numbers) // 2]

    for number in numbers:
        if number > pivot:
            right.append(number)
        elif number == pivot:
            mid.append(number)
        else:
            left.append(number)
    
    return quicksort(left) + mid + quicksort(right)

def solution(number, k):
    answer = ''
    numbers = list(map(int, list(number)))
    sorted_numbers = quicksort(numbers)
    answer = [0] * (len(numbers) - k)
    goals = {}
    for i in range(k):
        if goals.get(sorted_numbers[i]): goals[sorted_numbers[i]] += 1
        else: goals[sorted_numbers[i]] = 1
    cnt = 0
    print(goals)
    for number in numbers:
        if goals.get(number):
            goals[number] -= 1
            continue
        else:
            answer[cnt] = f'{number}'
            cnt += 1        
    return ''.join(answer)

print(solution("4177252841", 4))