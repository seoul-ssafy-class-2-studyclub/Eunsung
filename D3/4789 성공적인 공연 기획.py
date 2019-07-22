for rounds in range(int(input())):
    audi = list(map(int,input()))
    needs = []
    for i in range(len(audi)):
        needs.append(i - sum(audi[0:i]))
    need = max(needs)
    print(f'#{rounds + 1} {need}')
