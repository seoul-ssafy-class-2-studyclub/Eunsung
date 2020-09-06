
def devide(left, right, budgets, M):
    mid = (left + right) // 2
    if left >= right:
        return mid
    tmp = 0
    for budget in budgets:
        if mid > budget: tmp += budget
        else: tmp += mid
    if tmp > M: return devide(left, mid - 1, budgets, M)
    elif tmp == M: return mid
    else:
        tmp = 0
        for budget in budgets:
            if mid + 1> budget: tmp += budget
            else: tmp += mid + 1
        if tmp > M:
            return mid
        elif tmp == M:
            return mid + 1
        return devide(mid + 1, right, budgets, M)


def solution(budgets, M):

    left = 0
    right = max(budgets)
    
    answer = devide(left, right, budgets, M)
    return answer

print(solution([120, 110, 140, 150], 485))