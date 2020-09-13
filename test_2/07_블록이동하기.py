def solution(board):
    LENGTH_OF_BOARD = len(board)
    answer = 99999999999999999999
    visited = {}

    status = 0
    
    robot = [(1, 1), (1, 2), status]

    def make_robot_default(robot):
        if sum(robot[0]) > sum(robot[1]):
            robot[0], robot[1] = robot[1], robot[0]
        
    def rotate_when_0_down(robot):
        return [(robot[0][0] + 1, robot[0][1] + 1), robot[1], 1], [robot[0], (robot[1][0] + 1, robot[1][1] - 1), 1]
    def rotate_when_0_up(robot):
        return [(robot[0][0] - 1, robot[0][1] + 1), robot[1], 1], [robot[0], (robot[1][0] - 1, robot[1][1] - 1), 1]
    def rotate_when_1_right(robot):
        return [(robot[0][0] + 1, robot[0][1] + 1), robot[1], 0], [robot[0], (robot[1][0] - 1, robot[1][1] + 1), 0]
    def rotate_when_1_left(robot):
        return [(robot[0][0] + 1, robot[0][1] - 1), robot[1], 0], [robot[0], (robot[1][0] - 1, robot[1][1] - 1), 0]
    def step_when_1(robot):
        return [robot[0], (robot[1][0] - 2, robot[1][1]), 1], [(robot[0][0] + 2, robot[0][1]), robot[1], 1]
    def step_when_0(robot):
        return [robot[0], (robot[1][0], robot[1][1] - 2), 0], [(robot[0][0], robot[0][1] + 2), robot[1], 0]
    def check_when_0_down(robot):
        check_y = robot[0][0] + 1
        if check_y > LENGTH_OF_BOARD: return False
        if board[check_y - 1][robot[0][1] - 1] or board[check_y - 1][robot[1][1] - 1]:
            return False
        return True
    def check_when_0_up(robot):
        check_y = robot[0][0] - 1
        if check_y <= 0: return False
        if board[check_y - 1][robot[0][1] - 1] or board[check_y - 1][robot[1][1] - 1]:
            return False
        return True
    def check_when_1_right(robot):
        check_x = robot[0][1] + 1
        if check_x > LENGTH_OF_BOARD: return False
        if board[robot[0][0] - 1][check_x - 1] or board[robot[1][0] - 1][check_x - 1]:
            return False
        return True
    def check_when_1_left(robot):
        check_x = robot[0][1] - 1
        if check_x <= 0: return False
        if board[robot[0][0] - 1][check_x - 1] or board[robot[1][0] - 1][check_x - 1]:
            return False
        return True
    
    def check_now_location(robot):
        
        for i in range(2):
            robot_y, robot_x = robot[i]
            if not 0 < robot_x <= LENGTH_OF_BOARD or not 0 < robot_y <= LENGTH_OF_BOARD:
                return False
            if board[robot_y - 1][robot_x - 1]:
                return False
        return True 
    function_list = [(check_when_0_down, rotate_when_0_down, 0), (check_when_0_up, rotate_when_0_up, 0),
                    (check_when_1_left, rotate_when_1_left, 1), (check_when_1_right, rotate_when_1_right, 1)]

    queue = [(robot, 0)]
    step_list = [step_when_0, step_when_1]
    while queue:
        n_robot, time = queue.pop(0)
        location_robot = (n_robot[0], n_robot[1])
        if visited.get(location_robot):
            if visited[location_robot] <= time:
                continue
        visited[location_robot] = time
        if (LENGTH_OF_BOARD, LENGTH_OF_BOARD) in location_robot :
            answer = time
            break
        time += 1
        for check, rotate, c in function_list:
            if c != n_robot[2]:
                continue
            if check(n_robot):
                r1, r2 = rotate(n_robot)
                make_robot_default(r1)
                make_robot_default(r2)
                if check_now_location(r1):
                    queue.append((r1, time))

                if check_now_location(r2):
                    queue.append((r2, time))
        
        r1, r2 = step_list[n_robot[2]](n_robot)
        make_robot_default(r1)
        make_robot_default(r2)

        if check_now_location(r1):
            queue.append((r1, time))
        if check_now_location(r2):
            queue.append((r2, time))

    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))