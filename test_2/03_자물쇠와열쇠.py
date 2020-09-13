from pprint import pprint

def solution(key, lock):
    m = len(key)
    n = len(lock)
    LENGTH_OF_BACKGROUND = n + 2 * m - 2

    background = [[0] * (LENGTH_OF_BACKGROUND) for _ in range(LENGTH_OF_BACKGROUND)]

    for dy in range(n):
        for dx in range(n):
            background[m - 1 + dy][m - 1 + dx] = lock[dy][dx]

    def is_opened(tmp_background):

        for dy in range(n):
            for dx in range(n):
                if tmp_background[m - 1 + dy][m - 1 + dx] != 1:
                    return False
        return True
    
    def copy_lock(background):
        copied_background = []

        for i in range(LENGTH_OF_BACKGROUND):
            copied_background.append(background[i][:])

        return copied_background
    
    def check_key(key, background):

        for start_y in range(n + m - 1):
            for start_x in range(n + m - 1):

                tmp_background = copy_lock(background)

                for dy in range(m):
                    for dx in range(m):
                        tmp_background[start_y + dy][start_x + dx] += key[dy][dx]
                if is_opened(tmp_background): return True
        return False
    
    def rotate(key):
        tmp_key = [[0] * m for _ in range(m)]
        for y in range(m):
            for x in range(m):
                tmp_key[x][m - y - 1] = key[y][x]
        return tmp_key

    for _ in range(4):
        key = rotate(key)
        if check_key(key, background): return True

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))