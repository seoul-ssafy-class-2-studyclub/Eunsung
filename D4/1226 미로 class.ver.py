#아이디어  SSAFY 2기 서울 2반 천재 김혜준

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class maze_road:
    
    #생성된다면 시작점의 y,x좌표를 받아서
    def __init__(self,y_index,x_index):
        self.y_index = y_index
        self.x_index = x_index
        
        #상하좌우 번갈아가면서 확인한다
        for y,x in near:
            #상하좌우에 0(길)이 있다면
            if maze[y_index + y][x_index + x] == 0:
                #그 길을 지나왔다는 표시로 4로 바꾸고
                maze[y_index + y][x_index + x] = 4
                #그 길의 좌표를 다시 class에 넣어서 전염병을 전염시킨다.
                maze[y_index + y][x_index + x] = maze_road(y_index + y,x_index + x)

                #만약 상하좌우에 3이있다면 도착한것이므로. 전역변수 result를 바꿔준다.            
            elif maze[y_index + y][x_index + x] == 3:
                result = 1




for rounds in range(1, 11):

    #미로를만듭니다.
    ro = int(input())
    maze = []
    result = 0
    for i in range(16):
        maze.append(list(map(int, input())))

    #2가 시작되는 곳을 찾아서 넣습니다.
    start_index = [(y, x) for y in range(16) for x in range(16) if maze[y][x] == 2][0]

    
    #2가 시작되는 곳을 class에 넣습니다.
    #전염병 처럼 퍼지기 시작합니다.
    maze[start_index[0]][start_index[1]] = maze_road(start_index[0],start_index[1])


    print('#%d %d' %(ro, result))
