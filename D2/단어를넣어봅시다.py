for i in range(int(input())):
    
    #보드를 만들자!
    board = []
    n, k = list(map(int,input().split()))
    for o in range(n):
        board.append(list(map(int,input().split())))

    #넣을수 있는 공간을 찾자
    #가로부터
    
    row_result = 0
    
    for l in range(n):
        row_count = 0 #가로줄에서 1을 셀 카운트
        for m in range(n):
            if board[l][m] == 1: #1이라면
                row_count += 1 #카운트 추가
            
            if m == n - 1 or board[l][m] == 0:   #벽에 부딪히거나, 0을만나면
                if row_count == k:                 #지금까지 있었던 1(빈공간)을세고 글자수와 맞다면
                    row_result += 1                 #가로 결과값에 1추가
                
                row_count = 0                  #가로 카운트 초기화 후 다음가로줄로 넘어감.

    #세로를찾자 가로줄과 마찬가지. 
    col_result = 0

    for m in range(n):
        col_count = 0
        for l in range(n):
            if board[l][m] == 1:
                col_count += 1

            if l == n - 1 or board[l][m] == 0:
                if col_count == k:
                    col_result += 1

                col_count = 0

    result = row_result + col_result
    print(f'#{i+1} {result}')