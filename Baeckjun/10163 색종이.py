N = int(input())
papers = [False for _ in range(N)]
papers_num = [False for _ in range(N)]
board = [[0 for _ in range(102)] for _ in range(102)]
for case in range(N):

    papers[case] = tuple(map(int,input().split()))

for i in range(N - 1, -1, -1):
    count = 0
    for y in range(papers[i][1], papers[i][1]+papers[i][3]):
        for x in range(papers[i][0], papers[i][0]+papers[i][2]):
            if board[y][x] == 0:
                board[y][x] = 1
                count += 1
    papers_num[i] = count


    
for i in range(len(papers)):
    print(papers_num[i])

    
    