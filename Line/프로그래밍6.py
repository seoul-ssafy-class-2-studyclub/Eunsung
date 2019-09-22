from pprint import pprint

def garo(leng ,arr):
    for _ in range(leng):
        arr.append('#')
    return arr
def rightsero(leng, arr):
    for _ in range(leng - 1):
        arr.append('.')
    arr.append('#')
    return arr
def leftsero(leng, arr):
    arr.append('#')
    for _ in range(leng - 1):
        arr.append('.')
    return arr
def sidesero(leng, arr):
    arr.append('#')
    for _ in range(leng - 2):
        arr.append('.')
    arr.append('#')
    return arr
def alldot(leng, arr):
    for _ in range(leng):
        arr.append('.')
    return arr

numbers = {
    1: [1,1,1,1,1],
    2: [0,1,0,2,0],
    3: [0,1,0,1,0],
    4: [3,3,0,1,1],
    5: [0,2,0,1,0],
    6: [2,2,0,3,0],
    7: [0,1,1,1,1],
    8: [0,3,0,3,0],
    9: [0,3,0,1,1],
    0: [0,3,3,3,0],
}

draw = [garo, rightsero, leftsero, sidesero, alldot]
N, loc = input().split()
N = int(N)
words = []
max_length = 0
full_length = 0
for _ in range(N):
    temp = input().split()
    full_length += len(temp[1])
    temp = tuple(map(int,temp))
    words.append(temp)
    if temp[0] > max_length:
        max_length = temp[0]

letters = []
for word in words:
    for letter in str(word[1]):
        letters.append((word[0], int(letter)))

board = [[] for _ in range(full_length)]
for y in range(2 * max_length - 1):
    for idx in range(len(letters)):
        if y + 1 == 1:
            board[idx].append(draw[numbers[letters[idx][1]][0]](letters[idx][0], []))
        if 1 < y + 1 < letters[idx][0]:
            board[idx].append(draw[numbers[letters[idx][1]][1]](letters[idx][0], []))
        if y + 1 == letters[idx][0]:
            board[idx].append(draw[numbers[letters[idx][1]][2]](letters[idx][0], []))
        if letters[idx][0] < y < 2 * letters[idx][0] - 1:
            board[idx].append(draw[numbers[letters[idx][1]][3]](letters[idx][0], []))
        if y + 1 == 2 * letters[idx][0] - 1:
            board[idx].append(draw[numbers[letters[idx][1]][4]](letters[idx][0], []))

if loc == 'TOP':
    for idx in range(len(letters)):
        if letters[idx][0] < max_length:
            for _ in range(2 * (max_length - letters[idx][0])):
                board[idx].append(draw[4](letters[idx][0], []))

if loc == 'BOTTOM':
    for idx in range(len(letters)):
        if letters[idx][0] < max_length:
            for _ in range(2 * (max_length - letters[idx][0])):
                board[idx].insert(0, draw[4](letters[idx][0], []))


if loc == 'MIDDLE':
    for idx in range(len(letters)):
        if letters[idx][0] < max_length:
            for _ in range(max_length - letters[idx][0]):
                board[idx].insert(0, draw[4](letters[idx][0], []))
            for _ in range(max_length - letters[idx][0]):
                board[idx].append(draw[4](letters[idx][0], []))

for y in range(2 * max_length - 1):
    for num in board:
        print(''.join(num[y]), end = ' ')
    print('')