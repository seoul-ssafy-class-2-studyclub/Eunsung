def is_pan(word):
    if word == reversed(word):
        return True
    return False

for rounds in range(1,11):
    board = []
    ro = int(input())
    for i in range(100):
        board.append(input())
    
    print(is_pan('stress'))

    # print(f'#{rounds} {count}')