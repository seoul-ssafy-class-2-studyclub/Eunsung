for rounds in range(int(input())):

    num = int(input())

    scores = list(map(int,input().split()))
    su = []

    for score in range(101):
        su.append(scores.count(score))

    for score in range(100,-1,-1):
        if scores.count(score) == max(su):
            result = score
            break

    print(f'#{num} {result}')

