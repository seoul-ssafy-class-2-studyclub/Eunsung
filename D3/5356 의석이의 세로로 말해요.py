#글자보드에서 가장 긴 문자열의 길이를 구하는 함수
def max_check(testlist):
    lengthboard = []
    for i in range(len(testlist)):
        lengthboard.append(len(testlist[i]))
    return max(lengthboard)

for rounds in range(int(input())):
    result = []                     #읽은 결과를 넣을 보드
    board = []
    for i in range(5):
        board.append(list(input())) #보드를만들고
    longest = max_check(board)      #가장긴 문자열을 확인하자
    for i in range(5):
        if len(board[i]) < longest: #만약 글자가 가장 긴것이 아니라면
            for l in range(longest - len(board[i])): #가장 긴것과의 차이만큼
                board[i].append('') #''를 추가하여 빈공간을 만든다
    for i in range(longest):
        result.append(''.join(list(zip(*board))[i])) #result보드에 세로줄을 읽어서 넣어놓는다
    print(f'#{rounds + 1}', end=' ')
    print(''.join(result))
                