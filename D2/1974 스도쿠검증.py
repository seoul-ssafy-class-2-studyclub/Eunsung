#해당 리스트에 1~9가 전부 들어있는지 확인하는 함수제작

def check(check_list):
    for num in range(1,10):
        result = True
        if check_list.count(num) == 0:
            result = False
            break
    return result

for rounds in range(int(input())):

    sdoku_result = 1
    #스도쿠 판을제작
    board = []
    for i in range(9):
        board.append(list(map(int,input().split())))

    #정사각형 모양 체크를 위하여 정사각형의 중심 모음만들기
    origin = []
    for i in [1, 4, 7]:
        for j in [1, 4, 7]:
            origin.append((i,j))

    #각각의 정사각형중심에서 정사각형의 내부의 숫자들 모으고 체크하기
    for y, x in origin:
        test = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                test.append(board[y + i][x + j])
        if not check(test):
            sdoku_result = 0
            break
    # 가로줄 하나하나 가면서 숫자들 모으고 체크하기
    for i in range(9):
        test = []
        for j in range(9):
            test.append(board[i][j])
        if not check(test) :
            sdoku_result = 0
            break
    # 세로줄 하나하나 가면서 숫자들 모으고 체크하기
    for j in range(9):
        test = []
        for i in range(9):
            test.append(board[i][j])
        if not check(test) :
            sdoku_result = 0
            break

    print(f&apos;#{rounds+1} {sdoku_result}&apos;)