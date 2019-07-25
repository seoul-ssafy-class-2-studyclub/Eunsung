for rounds in range(int(input())):
    row = input().split()

    for i in range(3):
        if row.count(row[i]) % 2:
            print(f'#{rounds + 1} {row[i]}')
            break