for rounds in range(int(input())):

    S = D = H = C = 0
    cards = []
    card_list = input()

    for i in range(len(card_list)//3):
        cards.append(card_list[3 * i : 3 * (i + 1)])

    if len(cards) != len(set(cards)):
        result = 'ERROR'

    else:
        for i in range(len(cards)):
            if cards[i][0] == 'S':
                S += 1
            elif cards[i][0] == 'D':
                D += 1
            elif cards[i][0] == 'H':
                H += 1
            elif cards[i][0] == 'C':
                C += 1
        result = f'{13 - S} {13 - D} {13 - H} {13 - C}'

    print(f'#{rounds + 1} {result}')
