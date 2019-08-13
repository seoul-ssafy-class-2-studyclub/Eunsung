import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint

def find_route(dot_list, length, y):

    dot_list.append(y)

    if length == N:
        return length
    res = length
    
    for i in range(1, N+1):
        if not i in dot_list and board[y][i] == True :
            res = max(res, find_route(dot_list, length + 1, i))
    dot_list.pop()
    return res



result_list = []
for round in range(int(input())):
    N, M = map(int,input().split())
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        y, x = map(int,input().split())
        board[y][x] = True
        board[x][y] = True
    # pprint(board)

    result = 1
    for i in range(1,N + 1):
        result = max(result,find_route([], 1, i))
    result_list.append('#%d %d' %(round+ 1, result))
    
for value in result_list:
    print(value)

    
