for rounds in range(int(input())):
    numbers = list(map(int,input().split()))
    sums = list(set([numbers[x]+numbers[y]+numbers[z] for x in range(7) for y in range(x+1,7) for z in range(y+1,7)]))
    sums.sort(reverse=True)

    print(f'#{rounds + 1} {sums[4]}')
