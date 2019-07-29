from pprint import pprint
for rounds in range(1,11):
    ro = int(input())
    maze = []
    for i in range(16):
        maze.append(list(map(int,input())))

    start_index = [(y,x) for y in range(16) for x in range(16) if maze[y][x] == 2][0]
    end_index = [(y,x) for y in range(16) for x in range(16) if maze[y][x] == 3][0]
    
    y, x = start_index[0], start_index[1]
    
    path = []
    cross_section = (y, x)
    near = [(-1,0), (1,0), (0,-1), (0,1)]
    temp_path = []

    
    
    while True:

        maze[y][x] = 4
        near_path = [(i,l) for (i,l) in near if maze[y+i][x+l] == 0]
        
        if near_path.count(0) == 1:
            y += i; x += l
            path.append((y,x))
        
        elif near_path.count(0) > 1:
            cross_section = (y, x)
            
            for cross_num in range(near_path.count(0)):
                if maze[y+near_path[cross_num][0]][x+near_path[cross_num][1]] == 0:
                    y += near_path[cross_num[0]]; x += near_path[cross_num][1]
            path.append((y,x))
        
        elif near_path.count(0) == 0:
            path.append((y,x))
            y, x = cross_section





        

        





