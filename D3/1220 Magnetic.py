for rounds in range(10):
    size = int(input())
    board = [] #빈 보드를 만듭니다.
    for i in range(100):
        board.append(input().split()) #채워넣습니다.
    count = 0
    board = list(zip(*board)) #세로줄을 봐야하기에 세로줄과 가로줄을 바꿔주고
    for i in range(100):
        minus = 0
        temp_line = ''.join(board[i]).split('0') #0은 필요없으니 다 지워주고,
        temp_line = ''.join(temp_line).split('2') #(1,2)세트를 구분하기위하여 2로 스플릿해줍니다.
                                             
        if temp_line[len(temp_line) - 1] != '': #마지막에 1로끝나면 떨어지는애들이니 
            minus = 1                           #카운트를 하나줄여줄준비를하고
        count += len(temp_line) - temp_line.count('') - minus #1의 모음숫자를세줍니다
    print(f'#{rounds + 1 } {count}')
        