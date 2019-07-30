def is_pan(word):
    word = list(word)
    if word == list(reversed(word)):
        return True
    return False

def max_pan(board, board_col):

    for length in range(100,0,-1):
        for y in range(100):
            for x in range(100-length+1):
                if is_pan(board[y][x:x+length]):
                    return length
                    
                if is_pan(board_col[y][x:x+length]):
                    return length
                    


for rounds in range(1,11):
    board = []
    ro = int(input())
    for i in range(100):
        board.append(input())
    
    board_col = list(map(list,zip(*board)))
    for i in range(100):
        board_col[i] = ''.join(board_col[i])

    

    print(f'#{rounds} {max_pan(board, board_col)}')