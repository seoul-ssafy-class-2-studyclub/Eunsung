from pprint import pprint
def solution(key, lock):
    length2 = len(lock)
    length = len(key)

    def rotate(lock):
        board_90 = list(map(list,zip(*lock)))
        for i in range(length2):
            board_90[i].reverse()
        return board_90

    def check(key, lock):

        for gap_y in range(40):
            for gap_x in range(40):
                flag = 0
                for y in range(length2):
                    for x in range(length2):
                        if lock[y][x] == key[gap_y + y][gap_x + x]:
                            flag = 1
                            break
                    if flag:
                        break
                if not flag:
                    return True
        return False

    new_key = [0] * (60)
    for i in range(60):
        if i < length or i >= 2 * length:
            new_key[i] = [0] * (60)
        else:
            new_key[i] = [0] * (20) + key[i - length] + [0] * (40-length)
    lock_90 = rotate(lock)
    lock_180 = rotate(lock_90)
    lock_270 = rotate(lock_180)
    if check(new_key, lock) or check(new_key, lock_90) or check(new_key, lock_180) or check(new_key, lock_270):
        return True
    return False
    
print(solution([[1, 1, 1,0], [1, 1, 1,0], [1, 1, 1,0],[1, 1, 1,1]], [[0, 0, 0], [0, 0, 0], [1, 1, 1]]))