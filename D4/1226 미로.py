
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def maze_adventure(y, x, maze):
    for dy, dx in near:
        if maze[y + dy][x + dx] == 3:
            return 1

    for dy, dx in near:
        if maze[y + dy][x + dx] == 0:
            maze[y + dy][x + dx] = 4
            return maze_adventure(y + dy, x + dx, maze)

    for i in range(4, 9):
        for dy, dx in near:
            if maze[y + dy][x + dx] == i:
                maze[y + dy][x + dx] += 1
                return maze_adventure(y + dy, x + dx, maze)

    return 0


from pprint import pprint

for rounds in range(1, 11):
    ro = int(input())
    maze = []
    for i in range(16):
        maze.append(list(map(int, input())))

    start_index = [(y, x) for y in range(16) for x in range(16) if maze[y][x] == 2][0]

    print('#%d %d' %(rounds,maze_adventure(start_index[0], start_index[1],maze)))
